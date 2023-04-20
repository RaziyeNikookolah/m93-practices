from transaction.models import TransactionType


class InvalidAmountError(  # keyword Error is better than Exception for the name
    Exception
):  # TODO best practice is to put every exception in file its module
    """Exception raised for errors in the input amount.

    Attributes:
        amount -- input amount which caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        # amount,
        message="Amount should be a positive numeric input",
    ):
        # self.amount = amount # here can make special error for every condition of amount
        self.message = message
        super().__init__(self.message)


class InvalidDateError(Exception):
    """Exception raised for errors in the input date.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Invalid input for date, Date should be like 2023-02-13",
    ):
        self.message = message
        super().__init__(self.message)


class RequiredDateError(Exception):
    """Exception raised for errors in the input date.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Dates required",
    ):
        self.message = message
        super().__init__(self.message)


class InvalidTypeError(Exception):
    """Exception raised for errors in the input type.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message=f"Invalid type input, enter ({TransactionType.EXPENCE} or {TransactionType.INCOME})",  # TODO use Enum value
    ):
        self.message = message
        super().__init__(self.message)


class InvalidCommandError(Exception):
    """Exception raised for errors in the input command.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Invalid command input, enter (add or view or report)",
    ):
        self.message = message
        super().__init__(self.message)
