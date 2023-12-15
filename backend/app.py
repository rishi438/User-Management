"""API ROUTES And Functioning"""

import json
import logging

from api.api import OPERATIONS
from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(
    filename="attendance.log",
    format="%(levelname)s: %(asctime)s - %(message)s",
    level=logging.DEBUG,
)
origins = [
    "http://localhost:3000",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api", tags=["api"])
logging.info("Logging initiated")

operations = OPERATIONS()


@app.get("/")
async def index():
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    return {"message": "Hello World!"}


@api_router.get("/courses")
@api_router.post("/courses")
async def get_or_post_status(request: Request):
    """Courses Route"""
    response = {}
    try:
        method = request.method
        if method == "GET":
            return {"status": "OK"}
        elif method == "POST":
            request_body = await request.body()
            request_data = json.loads(request_body)
            logging.info(f"request data {request_data}")
            response = operations.add_courses_api(payload=request_data)
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")
    except Exception as ex:
        response[" msg "] = "Error Occured Please Contact Adminstrator"
        logging.info(f"Error Occured Please Contact Adminstrator{ex}")
    return response


app.include_router(api_router)
