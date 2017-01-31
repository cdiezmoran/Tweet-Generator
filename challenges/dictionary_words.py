import sys
import random

def read_words():
    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()
        return lines

def get_random_words():
    words_to_return = int(sys.argv[1])

    lines = read_words()

    words = []
    for num in xrange(words_to_return):
        rand_index = random.randint(0, len(lines) - 1)
        words.append(lines[rand_index])

    return words

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    if isInt(sys.argv[1]):
        print ' '.join(get_random_words())
    else:
        print 'Please input an int as an argument'
