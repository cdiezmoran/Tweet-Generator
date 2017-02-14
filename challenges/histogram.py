import file_reader

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
        for item in iterable:
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1

        self.types = len(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self.get(item, 0)
