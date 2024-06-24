from django.urls import path
from account.views import (
    RegisterView,
    LoginView,
    VerifyView,
    SendVerifyCodeView,
    PasswordResetView,
    # ----------------------------------------------------------------
    UserAllView,
    UserListView,
    UserDetailView,
    UserRestoreView,
    UserPasswordResetView,
    UserAuditListView,
    # ----------------------------------------------------------------
    CheckUserEmailView,
    UserProfileView,
    DataRequestListView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="account.auth.register"),
    path("login/", LoginView.as_view(), name="account.auth.login"),
    path("verify/", VerifyView.as_view(), name="account.auth.verify"),
    path("send-code/", SendVerifyCodeView.as_view(), name="account.auth.send_code"),
    path("reset-password/", PasswordResetView.as_view(), name="account.auth.reset_password"),
    path("all-users/", UserAllView.as_view(), name="account.user.all"),
    path("users/", UserListView.as_view(), name="account.user.list"),
    path("user/<str:email>/", UserDetailView.as_view(), name="account.user.detail"),
    path("user/<str:email>/restore/", UserRestoreView.as_view(), name="account.user.restore"),
    path("user/<str:email>/reset-password/", UserPasswordResetView.as_view(), name="account.user.reset-password"),
    path("user/<str:email>/user-audits/", UserAuditListView.as_view(), name="auth.user.user_audit.list"),
    path("check-email/", CheckUserEmailView.as_view(), name="account.util.check_email"),
    path("profile/", UserProfileView.as_view(), name="account.profile"),
    path("data-requests/", DataRequestListView.as_view(), name="account.data_request.list"),
]