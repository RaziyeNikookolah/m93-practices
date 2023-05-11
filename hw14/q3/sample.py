from person import Person
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("sample.log", mode="a", encoding=None, delay=False)
formatter = logging.Formatter(
    "%(asctime)s %(name)-10s %(levelname)s %(msecs)03d %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)


rootLogger = logging.getLogger()
rootLogger.setLevel(logging.ERROR)
consoleHandler = logging.StreamHandler()
logFormatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def sub(a, b):
    if b != 0:
        result = a / b
        logger.debug("a/b=" + str(result))
        rootLogger.error("a/b=" + str(result))
        return result

    logging.error("Divide by zero!")
    rootLogger.error("Divide by zero!")


sub(2, 3)
sub(2, 0)

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
