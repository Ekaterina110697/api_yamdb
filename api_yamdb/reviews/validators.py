from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть me.'),
            params={'value': value},
        )


def year_validator(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError('Год не может быть позже текущего года.')
