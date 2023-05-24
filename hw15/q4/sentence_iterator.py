import re
from time import time, sleep


class SentenceIterator:
    # it was 60 in question i make it 5 to test it sooner
    NEXT_CALL_TIME = 5

    def __init__(self, sentence):
        self.index = 0
        self.sentence = sentence
        self.entrace_time = time()

    def __iter__(self):
        return self

    def __next__(self):
        self.next_time = time()
        words = re.sub(r"[^\w\s]", "", self.sentence.lower()).split()
        if (
            self.index >= len(words)
            or self.next_time - self.entrace_time >= self.__class__.NEXT_CALL_TIME
        ):
            raise StopIteration
        word = words[self.index]
        self.index += 1
        return word

    def get_words_count(self):
        return len(self.sentence.split())


sntncItrtr = SentenceIterator("jhg hghg 76jhgjhg y:bbj? :jgj")

print(next(sntncItrtr))
print(next(sntncItrtr))
sleep(SentenceIterator.NEXT_CALL_TIME)
print(next(sntncItrtr))
