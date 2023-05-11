import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("person.log", mode="a", encoding=None, delay=False)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)  # handler can have set level
logger.addHandler(handler)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.debug("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("Invalid age!")
        self._age = 0
