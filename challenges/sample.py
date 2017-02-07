import sys
import random
import operator
import word_analyzer
import file_reader

def get_sample_from(histogram):
    sorted_histogram = sorted(histogram.items(), key=operator.itemgetter(1))

    total_sum = sum([tup[1] for tup in sorted_histogram])
    frequency_sum = 0

    random_number = random.randint(1, total_sum)

    for tup in sorted_histogram:
        frequency_sum += tup[1]
        if random_number <= frequency_sum:
            print "The frequency is %d\nThe random number is %d" % (frequency_sum, random_number)
            return tup[0]

if __name__ == '__main__':
    file_path = sys.argv[1]
    words = file_reader.get_words_only(file_path)
    histogram = word_analyzer.histogram(words)
    print get_sample_from(histogram)
