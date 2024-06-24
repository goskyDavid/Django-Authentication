from enumfields import Enum


NOTIFICATION_GROUP_NAME = "notification"


class NotificationTypes(Enum):
    NEW_USER = "new_user"
    UPDATE_USER = "update_user"
    NEW_COMPANY = "new_company"
    UPDATE_COMPANY = "update_company"
    NEW_PERSON = "new_person"
    UPDATE_PERSON = "update_person"
    NEW_EXECUTIVE = "new_executive"
    UPDATE_EXECUTIVE = "update_executive"
    NEW_ACTIVITY = "new_activity"
    UPDATE_ACTIVITY = "update_activity"
    NEW_DATA_REQUEST = "new_data_request"
