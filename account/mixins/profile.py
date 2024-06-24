from django.conf import settings
from django.utils.timezone import now

from rest_framework.mixins import UpdateModelMixin

from services import Base64ToFileService


class UpdateProfileMixin(UpdateModelMixin):
    def perform_update(self, serializer):
        data = self.request.data
        additional_args = dict()
        if "picture_base64" in data:
            avatar_base64 = data["picture_base64"]
            folder_path = "avatars/"

            tmp = avatar_base64.split(",")
            timestamp = str(int(now().timestamp() * 1000))
            extension = (((tmp[0].split("/"))[1]).split(";"))[0]
            base64_string = tmp[1]
            file_name = f"{timestamp}.{extension}"

            base64_to_file = Base64ToFileService(base64_string, folder_path, file_name)
            base64_to_file()

            file_url = f"{settings.BACKEND_BASE_URL}/media/{folder_path}{file_name}"
            additional_args["picture"] = file_url

        return serializer.save(**additional_args)
