from ._v_login import UserLoginView
from ._v_profile import UserProfileView
from ._v_register import UserRegistrationView
from ._v_forget_pass import UserPasswordResetView

__all__ = [
    'UserLoginView',
    'UserProfileView',
    'UserRegistrationView',
    'UserPasswordResetView',
]