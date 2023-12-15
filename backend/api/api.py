"""API Handling"""

import logging
from enum import IntEnum, unique

from api.courses.definitions import COURSES


@unique
class AlertType(IntEnum):
    SUCCESS = 0
    DANGER = 1
    WARNING = 2
    INFO = 3


DEFAULT_API_RESPONSE_OBJ = {
    "status": False,
    "msg": "",
    "state": AlertType.INFO.name,
}


class OPERATIONS:
    """API Routes"""

    def add_courses_api(self, payload):
        """add course API"""
        response = DEFAULT_API_RESPONSE_OBJ.copy()

        try:
            logging.info("API Route add_course_api")
            course = COURSES()
            response["status"] = course.add_courses(payload)
            if response["status"]:
                response["msg"] = "Created"
                response["state"] = AlertType.SUCCESS.name
            else:
                response["state"] = AlertType.INFO.name
                response["msg"] = "Error Occurred when creating courses"
        except Exception as ex:
            logging.info(f"Error Occurred when calling add courses api: {ex}")
            response["state"] = AlertType.DANGER.name
        return response
