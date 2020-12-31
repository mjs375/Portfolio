def filter_long_words(sentence, n):
    sentence = sentence.split(" ")
    answer = []
    for word in sentence:
        if len(word) > n:
            answer.append(word)
    return answer

"""
Write a function filter_long_words that takes a string sentence and an integer n. Return a list of all words that are longer than n.
Example:
  filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']
"""
