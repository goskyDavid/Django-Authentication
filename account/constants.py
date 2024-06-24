from enumfields import Enum


SECURITY_EXCLUDE_MODEL_NAMES = [
    "logentry",
    "permission",
    "group",
    "contenttype",
    "session",
    "useremailverification",
    "useraudit",
    "sockettoken",
]


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    UNKNOWN = 0

    def __str__(self):
        if self == Gender.MALE:
            return "Male"
        elif self == Gender.FEMALE:
            return "Female"
        else:
            return "Unknown"


class UserRoles(Enum):
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    UPDATER = "updater"

    def __str__(self):
        if self == Gender.MALE:
            return "Admin"
        elif self == Gender.FEMALE:
            return "Supervisor"
        else:
            return "Updater"


class UserAuditTypes(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    SOFT_DELETE = "soft_delete"
    RESTORE = "restore"
    EXCEL_EXPORT = "excel_export"


class DataRequestStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
