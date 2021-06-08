"""
created by Nagaj at 08/06/2021
"""

BLOOD_TYPES = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
STATUS = ("PENDING", "APPROVED", "REJECTED")


def validate_blood_type(function):
    """
        validate blood type
        :param function: value of blood type
        :return: valid blood type else raise an error
    """

    def wrapper(*arg, **kwargs):
        blood_type = function(*arg, **kwargs)
        if blood_type not in BLOOD_TYPES:
            raise ValueError(f"Invalid Blood Type {blood_type}. Allowed: {BLOOD_TYPES}")
        return blood_type

    return wrapper


def validate_status(function):
    """
        validate request status , allowed are "PENDING", "APPROVED", "REJECTED"
        :param function: request status value
        :return: valid value for status
    """

    def wrapper(*arg, **kwargs):
        status = function(*arg, **kwargs)
        if status not in STATUS:
            raise ValueError(f"Invalid Status {status}. Allowed: {STATUS}")
        return status

    return wrapper
