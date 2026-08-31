from enum import StrEnum


class PaymentTestStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    AUTHORIZED = "AUTHORIZED"
    CAPTURED = "CAPTURED"
    REFUNDED = "REFUNDED"
    DECLINED = "DECLINED"
    FAILED = "FAILED"


class PaymentTestSystem(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"
