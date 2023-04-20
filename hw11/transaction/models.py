"""
This module contains a Transaction class which represents a single financial transaction.

It also contains an enum class TransactionType which has two members, EXPENCE and INCOME, representing the type of transaction.

This class raises the following exceptions:
    - InvalidTypeException: If an invalid transaction type is provided.
    - InvalidAmountException: If an invalid amount is provided.
    - InvalidDateException: If an invalid date format is provided.

Attributes:
    TransactionType (Enum): An enum class with two members, EXPENCE and INCOME, representing the type of transaction.

"""

from datetime import datetime
from enum import Enum
from decimal import Decimal
from core.exceptions import InvalidTypeError

from core.util import amount_validation, date_validation


class TransactionType(Enum):
    EXPENCE = "Expence"
    INCOME = "Income"


class Transaction:

    """
    Represents a single financial transaction.

    Args:
        type (TransactionType): The type of the transaction. Must be either EXPENCE or INCOME.
        amount (str): The amount of the transaction as a string. Must be a positive decimal number with up to two decimal places.
        date (str): The date of the transaction as a string in the format "YYYY-MM-DD".
        category (str): The category of the transaction.
        description (str): A description of the transaction.

    Attributes:
        amount (Decimal): The amount of the transaction as a Decimal.
        date (datetime.date): The date of the transaction as a datetime.date object.
        type (TransactionType): The type of the transaction.
        category (str): The category of the transaction.
        description (str): A description of the transaction.
        id (float): The timestamp of the transaction as a float.

    Raises:
        InvalidTypeException: If an invalid transaction type is provided.
        InvalidAmountException: If an invalid amount is provided.
        InvalidDateException: If an invalid date format is provided.

    """

    def __init__(
        self,
        type: TransactionType,
        amount: str,
        date: str,
        category: str,
        description: str,
    ) -> None:
        self.amount = amount
        self.date = date
        self.type = type
        self.category = category
        self.description = description
        dt = datetime.now()
        self.id = datetime.timestamp(dt)

    @property
    def type(self):
        """
        The type of the transaction.

        Returns:
            TransactionType: The type of the transaction.
        """
        return self._type

    @type.setter
    def type(self, value: TransactionType):
        """
        Setter method for the type attribute.

        Args:
            value (TransactionType): The type of the transaction.

        Raises:
            InvalidTypeException: If an invalid transaction type is provided.
        """
        if not value in (TransactionType.INCOME, TransactionType.EXPENCE):
            raise InvalidTypeError()
        self._type = value

    @property
    def amount(self):
        """
        The amount of the transaction.

        Returns:
            Decimal: The amount of the transaction as a Decimal.
        """
        return self._amount

    @amount.setter
    def amount(self, value: str):
        """
        Setter method for the amount attribute.

        Args:
            value (str): The amount of the transaction as a string.

        Raises:
            InvalidAmountException: If an invalid amount is provided.
        """
        amount_validation(value)
        self._amount = Decimal(value)

    @property
    def date(self):
        """Getter method for the transaction date.

        Returns:
            date: The date of the transaction.
        """
        return self._date

    @date.setter
    def date(self, value):
        """Setter method for the transaction date.

        Args:
            value (str): The date of the transaction in "YYYY-MM-DD" format.

        Raises:
            InvalidDateException: If the date is not in the correct format.

        Returns:
            None
        """
        date_validation(value)
        self._date = datetime.strptime(value, "%Y-%m-%d").date()

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction, including its type, date, amount, category, and description.

        Returns:
            str: A string representation of the transaction.
        """
        return f"type: {self.type.value}, date: {self.date}, amount: {self.amount}, category: {self.category}, description: {self.description}"
