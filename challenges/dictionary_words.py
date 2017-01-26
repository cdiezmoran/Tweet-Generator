import sys
import random

def get_random_word():
    words_to_return = int(sys.argv[1])

    with open('/usr/share/dict/words') as f:
        lines = f.read().splitlines()

        words = []
        for num in xrange(words_to_return):
            rand_index = random.randint(0, len(lines) - 1)
            words.append(lines[rand_index])

        return words


if __name__ == '__main__':
    print ' '.join(get_random_word())
