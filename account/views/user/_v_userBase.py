from django.http import Http404
from account.models import User
from services.views import ModelPermissionRequiredView


class BaseUserView(ModelPermissionRequiredView):
    def get_user(self):
        user = User.objects.filter(email=self.kwargs["email"]).first()
        if user:
            return user
        raise Http404()
