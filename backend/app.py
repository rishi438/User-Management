"""API ROUTES And Functioning"""

import json
import logging

from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

logging.basicConfig(
    filename="attendance.log",
    format="%(levelname)s: %(asctime)s - %(message)s",
    level=logging.DEBUG,
)
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api", tags=["api"])

logging.info("Logging initiated")


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
    """_summary_

    Args:
        request (Request): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    try:
        method = request.method
        if method == "GET":
            return {"status": "OK"}
        elif method == "POST":
            request_body = await request.body()
            request_data = json.loads(request_body)
            logging.info(f"request data {request_data}")
            return {"status": "Created"}
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")
    except Exception as ex:
        logging.info(f"Error Occured Please Contact Adminstrator{ex}")


app.include_router(api_router)
