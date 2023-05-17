import builtins


class Indenter:
    def __init__(self) -> None:
        self.output = ""

    def __enter__(self):
        self.output += "    "
        return self  # its very important to return self since we can use other methode in the class on it

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.output += "\n    "

    def print(self, *args, **kwargs):
        return builtins.print(self.output, *args, **kwargs)

    def __str__(self):
        return self.output


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is cheap!")
        with indent:
            indent.print("Show me the code...")
    indent.print("Torvalds")
