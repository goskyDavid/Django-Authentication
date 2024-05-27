from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User


class TokenService:
    def __init__(self, user: User) -> None:
        self.user = user

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
