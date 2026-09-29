import re

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
TIME_PATTERN = r"^(?:[01]\d|2[0-3]):[0-5]\d$"


def validate_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


def validate_login_time(login_time):
    return re.fullmatch(TIME_PATTERN, login_time) is not None


def validate_record(record):

    parts = record.strip().split()


    if len(parts) != 3:
        return False

    username, email, login_time = parts

    return (
        username != ""
        and validate_email(email)
        and validate_login_time(login_time)
    )