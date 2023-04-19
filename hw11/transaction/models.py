from datetime import datetime
from enum import Enum
from decimal import Decimal
from core.exceptions import (
    InvalidTypeException,
    InvalidAmountException,
    InvalidDateException,
)
import re


class TransactionType(Enum):
    EXPENCE = "Expence"
    INCOME = "Income"


class Transaction:
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
        return self._type

    @type.setter
    def type(self, value: TransactionType):
        if not value in (TransactionType.INCOME, TransactionType.EXPENCE):
            raise InvalidTypeException()
        self._type = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: str):
        if not re.match(r"^\d+(\.\d{1,2})?$", value):
            raise InvalidAmountException()
        self._amount = Decimal(value)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not re.match(
            r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", value
        ):
            raise InvalidDateException()
        self._date = datetime.strptime(value, "%Y-%m-%d").date()

    def __str__(self) -> str:
        return f"type: {self.type.value}, date: {self.date}, amount: {self.amount}, category: {self.category}, description: {self.description}"
