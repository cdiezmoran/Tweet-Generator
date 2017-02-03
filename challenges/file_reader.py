import re

def get_lines(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
        return lines


def get_words_only(file_path):
    with open(file_path) as f:
        text = f.read()
        words = re.findall(r'(?!\d+)(\w+)',text)
        return words
