import sys
import re

def read_words():
    with open('./sources/holmes.txt') as f:
        text = f.read()
        words = re.findall(r'(?!\d+)(\w+)',text)
        return words

def histogram(source_text):
    histogram = {};

    for word in source_text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    if word in histogram:
        return histogram[word]

    return 0

if __name__ == '__main__':
    words = read_words()
    histogram = histogram(words)
    print "Unique words: " + str(unique_words(histogram))
    print frequency('mystery', histogram)
