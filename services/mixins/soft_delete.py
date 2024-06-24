from rest_framework.mixins import DestroyModelMixin


class SoftDeleteModelMixin(DestroyModelMixin):
    def perform_destroy(self, instance):
        return instance.soft_delete()
