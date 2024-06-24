from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST


HTTP_450_USER_IS_NOT_ACTIVATED = 450


class BadRequest(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "Solicitud incorrecta"
    default_code = "BAD_REQUEST"


class AccountNotActivated(APIException):
    status_code = HTTP_450_USER_IS_NOT_ACTIVATED
    default_detail = "La cuenta no está activada"
    default_code = "ACCOUNT_NOT_ACTIVATED"
