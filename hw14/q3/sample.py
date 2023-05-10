from person import Person
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("sample.log", mode="a", encoding=None, delay=False)
formatter = logging.Formatter(
    f"%(asctime)s %(name)s %(levelname)s %(msecs)03d %(message)s"
)

# format='{asctime}.{msecs:0<3.0f} {name} {threadName} {levelname}: {message}'

handler.setFormatter(formatter)
logger.addHandler(handler)


def sub(a, b):
    if b != 0:
        result = a / b
        logger.debug("a/b=" + str(result))
        return result

    logging.error("Divide by zero!")


sub(2, 3)
sub(2, 0)

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
