from django.core.exceptions import ValidationError
from datetime import date


def validate_deadline(value):
    if value < date.today():
        raise ValidationError(
            '%(date)s is too early',
            params={'value': value},
        )
    else:
        return value
