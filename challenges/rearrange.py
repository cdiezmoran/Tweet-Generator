import sys
import random

def random_word_order():
    words = sys.argv[1:len(sys.argv)]

    iteration_times = random.randint(1, 15)

    for num in range(iteration_times):
        first_index = random.randint(0, len(words) - 1)
        second_index = random.randint(0, len(words) - 1)

        temp = words[first_index]
        words[first_index] = words[second_index]
        words[second_index] = temp

    return words

if __name__ == '__main__':
    rearraged_words = random_word_order()
    print ' '.join(rearraged_words)
