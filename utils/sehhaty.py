"""
created by Nagaj at 08/06/2021
"""

BLOOD_TYPES = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")


def validate_blood_type(func):
    def wrapper(*arg, **kwargs):
        blood_type = func(*arg, **kwargs)
        if blood_type not in BLOOD_TYPES:
            raise ValueError(f"Invalid Blood Type {blood_type}. Allowed: {BLOOD_TYPES}")
        return blood_type

    return wrapper
