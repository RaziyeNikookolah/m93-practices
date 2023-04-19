class InvalidAmountException(Exception):
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


class InvalidDateException(Exception):
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


class RequiredDateException(Exception):
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


class InvalidTypeException(Exception):
    """Exception raised for errors in the input type.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Invalid type input, enter (Expence or Income)",
    ):
        self.message = message
        super().__init__(self.message)


class InvalidCommandException(Exception):
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
