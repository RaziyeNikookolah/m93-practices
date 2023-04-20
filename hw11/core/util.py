import re
from core.exceptions import InvalidDateError, InvalidAmountError
from datetime import datetime


def date_validation(input_date: str):
    """Validates if the input date string is in the format YYYY-MM-DD.

    Args:
        input_date (str): A string representing the date in the format YYYY-MM-DD.

    Raises:
        InvalidDateException: If the input date string is not in the format YYYY-MM-DD.

    Returns:
        None
    """
    if not re.match(
        r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", input_date
    ):
        raise InvalidDateError()

    if datetime.strptime(input_date, "%Y-%m-%d").date() > datetime.date().now():
        raise InvalidDateError("Date shuold not be in future..")


def amount_validation(input_amount: str):
    """Validates if the input amount string is in the format X.XX or XXX.

    Args:
        input_amount (str): A string representing the amount in the format X.XX or XXX.

    Raises:
        InvalidAmountException: If the input amount string is not in the format X.XX or XXX.

    Returns:
        None
    """
    if not re.match(r"^\d+(\.\d{1,2})?$", input_amount):
        raise InvalidAmountError()
