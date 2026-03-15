from fastapi import APIRouter
from endpoints.endpoints import ApiEndpoint
from models.response_model import MailHandlerResponse


router = APIRouter()
router.add_api_route(
    "/sent_mail",
    ApiEndpoint.mail_handle,
    methods=["POST"],
    response_model=MailHandlerResponse
)

router.add_api_route("/mail_logs",
                     ApiEndpoint.mail_logs,
                     methods=["GET"])