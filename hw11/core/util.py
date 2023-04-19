import re
from core.exceptions import InvalidDateException, InvalidAmountException


def date_validation(input_date: str):
    if not re.match(
        r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", input_date
    ):
        raise InvalidDateException()


def amount_validation(input_amount: str):
    if not re.match(r"^\d+(\.\d{1,2})?$", input_amount):
        raise InvalidAmountException()
