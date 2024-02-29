import enum


class CompStatusType(enum.Enum):
    pending = "PENDING"
    reject = "REJECT"
    approved = "APPROVED"
    unverified_account = "Unverified Account"

