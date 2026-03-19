from fastapi import APIRouter
from endpoints.endpoints import ApiEndpoint, AuthServiceEndpoint
from models.response_model import MailHandlerResponse, AuthServiceResponseModel

# create api router
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

router.add_api_route("/login", AuthServiceEndpoint.login,
                     methods=["POST"],
                     response_model=AuthServiceResponseModel)

router.add_api_route("/signup", AuthServiceEndpoint.signup,
                     methods=["POST"],
                     response_model=AuthServiceResponseModel)

router.add_api_route("/reset_password", AuthServiceEndpoint.reset_password,
                     methods=["POST"],
                     response_model=AuthServiceResponseModel)

router.add_api_route("/refresh_token", AuthServiceEndpoint.refresh_token,
                     methods=["POST"],
                     response_model=AuthServiceResponseModel)
