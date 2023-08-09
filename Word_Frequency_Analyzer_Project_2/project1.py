import re
from collections import Counter

class WordFrequencyAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self._read_words()

    def _read_words(self):
        with open(self.file_path, "r") as file:
            text = file.read()
            words = re.findall(r'\w+', text.lower())
            return words

    def analyze(self):
        word_count = Counter(self.words)
        return word_count

    def most_common(self, n=10):
        word_count = self.analyze()
        return word_count.most_common(n)

    def filter_by_length(self, min_length):
        word_count = self.analyze()
        filtered_words = {word: count for word, count in word_count.items() if len(word) >= min_length}
        return filtered_words

# Decorator for filtering common words
def ignore_common_words(func):
    common_words = set(["the", "and", "is", "in", "of", "it", "to", "a"])

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filtered_result = {word: count for word, count in result.items() if word not in common_words}
        return filtered_result

    return wrapper

@ignore_common_words
def analyze_and_filter(analyzer, min_length=5):
    return analyzer.filter_by_length(min_length)

if __name__ == "__main__":
    # file_path = "sample_text1.txt"
    file_path = "sample_text2.txt"
    analyzer = WordFrequencyAnalyzer(file_path)

    print("Top 10 Most Common Words:")
    print(analyzer.most_common())

    print("\nFiltered Words (Minimum Length = 5):")
    filtered_words = analyze_and_filter(analyzer)
    for word, count in filtered_words.items():
        print(f"{word}: {count}")
