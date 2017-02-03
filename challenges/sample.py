import sys
import random
import operator
import word_analyzer
import file_reader

def get_sample_from(histogram):
    sorted_histogram = sorted(histogram.items(), key=operator.itemgetter(1))

    distribution_dict = {}
    frequency_sum = 0
    for tup in sorted_histogram:
        key = tup[1] + frequency_sum
        distribution_dict[key] = tup[0]
        frequency_sum += tup[1]

    random_number = random.randint(1, frequency_sum)

    while not random_number in distribution_dict:
        random_number += 1;

    return distribution_dict[random_number]

if __name__ == '__main__':
    file_path = sys.argv[1]
    words = file_reader.get_words_only(file_path)
    histogram = word_analyzer.histogram(words)
    print get_sample_from(histogram)
