import random


class Iterator:

    def __init__(self, quantity, *args, randomness_source=random.randint):
        self.randomness_source = randomness_source
        self.quantity = quantity
        self.args = args

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == self.quantity:
            raise StopIteration
        self.counter += 1
        return self.randomness_source(*self.args)


def generator(quantity, *args, randomness_source=random.randint):
    counter = 0
    while counter != quantity:
        counter += 1
        yield randomness_source(*args)
