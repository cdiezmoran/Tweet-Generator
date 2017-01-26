from itertools import permutations
import sys
import dictionary_words

def generate_anagrams():
    word = sys.argv[1]

    perms = [''.join(p) for p in permutations(word)]
    possible_words = set(perms)

    dict_words = dictionary_words.read_words()
    all_words = set(dict_words)

    return possible_words & all_words

if __name__ == '__main__':
    print ' '.join(generate_anagrams())
