from ._v_login import LoginView
from ._v_verify import VerifyView
from ._v_register import RegisterView
from ._v_forgetPass import PasswordResetView,  SendVerifyCodeView

__all__ = [
    'LoginView',
    'VerifyView',
    'RegisterView',
    'PasswordResetView',
    'SendVerifyCodeView',
]