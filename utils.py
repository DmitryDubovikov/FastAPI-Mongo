import re
from datetime import datetime


def validate_date(value):
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return True
    except ValueError:
        pass

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        pass

    return False


def validate_phone(value):
    phone_pattern = re.compile(r"^\+7\d{10}$")
    return phone_pattern.match(value)


def validate_email(value):
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return email_pattern.match(value)


def validate_text(value):
    return isinstance(value, str)


def validate_form_value(field_type, value):
    validators = {
        "date": validate_date,
        "phone": validate_phone,
        "email": validate_email,
        "text": validate_text,
    }

    return validators[field_type](value)


def typehint_dict(d):
    for k in d.keys():
        if validate_date(d[k]):
            d[k] = "date"
        elif validate_phone(d[k]):
            d[k] = "phone"
        elif validate_email(d[k]):
            d[k] = "email"
        else:
            d[k] = "text"
    return d
