import re

def analyze_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    palindromes = [word for word in frequency if word == word[::-1]]

    print("Total words:", len(words))
    print("Word Frequency:", frequency)
    print("Palindromes:", palindromes)

text = """Python is easy to learn.
Level is a palindrome.
Python is powerful and easy."""

analyze_text(text)
