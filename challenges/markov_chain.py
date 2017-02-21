import file_reader
import sys
import random
from histogram import Statogram

def generate_sentence(state_machine, length):
    current_word = random.choice(state_machine.keys())
    sentence = current_word + " "

    for i in xrange(length - 1):
        next_word = state_machine[current_word].after_words.sample()
        sentence += next_word
        if i != length - 1:
            sentence += " "
        current_word = next_word

    return sentence

if __name__ == '__main__':
    file_path = sys.argv[1]
    length = int(sys.argv[2])
    words = file_reader.get_words_only(file_path)
    state_machine = Statogram(words);
    print generate_sentence(state_machine, length)
