import builtins


class Indenter:
    INDENT_SPACES = 4 * " "

    def __init__(self) -> None:
        self.output = ""

    def __enter__(self):
        self.output += (
            self.__class__.INDENT_SPACES
        )  # it just determine the print position for enterance text
        # print("entrance...")
        return self  # its very important to return self since we can use other methode in the class

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("existance...")
        self.output = self.output[
            : -len(self.__class__.INDENT_SPACES)
        ]  # it just determine the print position for other texts

    def print(self, *args, **kwargs):
        # builtins.print("printing")
        return builtins.print(
            self.output[: -len(self.__class__.INDENT_SPACES)], *args, **kwargs
        )


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is cheap!")
        with indent:
            indent.print("Show me the code...")
    indent.print("Torvalds")
    # indent.print("Torvalds")  # added by me for test
