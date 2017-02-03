import sys
import re
import file_reader

def histogram(word_list):
    histogram = {};

    for word in word_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

if __name__ == '__main__':
    words = file_reader.get_words_only('./sources/holmes.txt')
    histogram = histogram(words)
    print "Unique words: " + str(unique_words(histogram))
    print frequency('mystery', histogram)
