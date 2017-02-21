import operator
import random

class Histogram(dict):
    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Histogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for index, item in enumerate(iterable):
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self.get(item, 0)

    def sample(self):
        sorted_histogram = sorted(self.items(), key=operator.itemgetter(1))

        total_sum = sum([tup[1] for tup in sorted_histogram])
        frequency_sum = 0

        random_number = random.randint(1, total_sum)

        for tup in sorted_histogram:
            frequency_sum += tup[1]
            if random_number <= frequency_sum:
                return tup[0]

class Statogram(Histogram):
    def __init__(self, iterable=None):
        super(Statogram, self).__init__()
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for index, item in enumerate(iterable):
            self.tokens += 1

            next_item = None
            if index + 1 != len(iterable):
                next_item = iterable[index + 1]

            if item in self:
                if next_item:
                    self[item].update(next_item)
            else:
                self[item] = State(next_item)
                self.types += 1

class State():
    def __init__(self, item=None):
        self.after_words = Histogram()
        if item:
            self.frequency = 0
            self.update(item)
        else:
            self.frequency = 1

    def update(self, item):
        self.frequency += 1
        self.after_words.update([item])
