import json
import logging
import uuid
import falcon
import falcon.asgi
from pymongo import MongoClient

# Replace with your MongoDB connection details
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
MONGO_DATABASE_NAME = "attendance_db"
logging.basicConfig(
    filename='attendance.log',
    format='%(levelname)s: %(asctime)s - %(message)s',
    level=logging.DEBUG
)

# Auth logic and JWT token generation (Replace with your actual auth code)
def authenticate(username, password):
    # Implement your authentication logic
    return username == "demo" and password == "password"

def generate_jwt_token(user_id):
    # Implement your JWT token generation logic
    return "your-generated-token"

class StorageEngine:

    def __init__(self, db):
        self.db = db

    async def get_things(self, marker, limit):
        collection = self.db['things']  
        cursor = collection.find().limit(limit)
        result = []
        for doc in cursor:
            result.append(doc)
        return result

    async def add_thing(self, thing):
        collection = self.db['things'] 
        result = collection.insert_one(thing)
        thing['_id'] = str(result.inserted_id)
        return thing

# Existing code for StorageError and other middleware components
class StorageError(Exception):

    @staticmethod
    async def handle(ex, req, resp, params):
        # TODO: Log the error, clean up, etc. before raising
        raise falcon.HTTPInternalServerError()



class RequireJSON:

    async def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                description='This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json')

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    description='This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/')


class JSONTranslator:
    # NOTE: Normally you would simply use req.get_media() and resp.media for
    # this particular use case; this example serves only to illustrate
    # what is possible.

    async def process_request(self, req, resp):
        # NOTE: Test explicitly for 0, since this property could be None in
        # the case that the Content-Length header is missing (in which case we
        # can't know if there is a body without actually attempting to read
        # it from the request stream.)
        if req.content_length == 0:
            # Nothing to do
            return

        body = await req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(title='Empty request body',
                                        description='A valid JSON document is required.')

        try:
            req.context.doc = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            description = ('Could not decode the request body. The '
                           'JSON was incorrect or not encoded as '
                           'UTF-8.')

            raise falcon.HTTPBadRequest(title='Malformed JSON',
                                        description=description)

    async def process_response(self, req, resp, resource, req_succeeded):
        if not hasattr(resp.context, 'result'):
            return

        resp.text = json.dumps(resp.context.result)

def max_body(limit):

    async def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('The size of the request is too large. The body must not '
                   'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPPayloadTooLarge(
                title='Request body is too large', description=msg)

    return hook

class ThingsResource:

    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger('attendance' + __name__)
        self.logger.setLevel(logging.DEBUG)

    async def on_get(self, req, resp, user_id):
        marker = req.get_param('marker') or ''
        limit = req.get_param_as_int('limit') or 50

        try:
            result = await self.db.get_things(marker, limit)
        except Exception as ex:
            self.logger.error(ex)

            description = ('Aliens have attacked our base! We will '
                           'be back as soon as we fight them off. '
                           'We appreciate your patience.')

            raise falcon.HTTPServiceUnavailable(
                title='Service Outage',
                description=description,
                retry_after=30)
            
        resp.context.result = result

        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200

    @falcon.before(max_body(64 * 1024))
    async def on_post(self, req, resp, user_id):
        self.logger.info('on_post method called')  # Add this line to log the method call
        try:
            doc = req.context.doc
            self.logger.info('Received data: %s', doc)  # Log the received data
        except AttributeError:
            self.logger.info('AttributeError occurred')
            raise falcon.HTTPBadRequest(
                title='Missing thing',
                description='A thing must be submitted in the request body.')

        proper_thing = await self.db.add_thing(doc)
        self.logger.info('Proper thing added: %s', proper_thing)  # Log the added thing

        resp.status = falcon.HTTP_201
        resp.location = '/%s/things/%s' % (user_id, proper_thing['_id'])

class RootResource:
    async def on_get(self, req, resp):
        resp.content_type = "text/plain"
        resp.body = "Welcome to the Attendance System API!"

# The app instance is an ASGI callable
app = falcon.asgi.App(middleware=[
    # AuthMiddleware(),
    RequireJSON(),
    JSONTranslator(),
])


if __name__ == "__main__":
    import uvicorn
    mongo_client = MongoClient(MONGO_CONNECTION_STRING)
    db = mongo_client[MONGO_DATABASE_NAME]
    storage_engine = StorageEngine(db)
    things = ThingsResource(storage_engine)
    app.add_route('/{user_id}/things', things)
    root_resource = RootResource()
    app.add_route('/', root_resource)
    app.add_error_handler(StorageError, StorageError.handle)
    uvicorn.run(app, host="0.0.0.0", port=8000)
