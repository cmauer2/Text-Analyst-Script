# Project Notes: How many words has the text shown? How many vowels? 
# How many distinct words? 
# How many sentences? 
# How many paragraphs? 
# What are the frequencies of each letter? 
# What about each word? Each sentence? 
# Or each pair of words? 
# In the same sentence? In the same paragraph?

""" In the provided code, words are defined as sequences of characters separated by whitespace, 
sentences end with periods, and paragraphs are identified by double newlines. """

from collections import Counter # this imports a counter so i can count vowels, distinct words, etc.

# open the text file and read its contents
with open('pythonProj\war_and_peace.txt', 'r') as file:
    file_contents = file.read()

# count the vowels in the text, lowercase and upper
vowels = 'aeiouAEIOU'
num_vowels = sum(1 for char in file_contents if char in vowels)

words = file_contents.split()
num_words = len(words)
# count the distinct words in the text
num_distinct_words = len(set(words))

# count sentences and paragraphs
sentences = file_contents.split('.')
num_sentences = len(sentences)
paragraphs = file_contents.split('\n\n') 
# splits the text into paragraphs based on double new lines 
num_paragraphs = len(paragraphs)

# calculate the freq of letters, words, sentences, and pair of words
pair_of_words_frequencies = Counter(zip(words, words[1:]))
# lists all the words in the text and splits by white space
# the list [1:] slices starting from the second word
# 'zip' pairs each word with the next one
# 'counter' counts the pairs
letter_frequencies = Counter(file_contents.lower())
word_frequencies = Counter(words)
sentence_frequencies = Counter(sentences)

print("Number of words in the text:", num_words)
print("Number of vowels:", num_vowels)
print("Number of distinct words:", num_distinct_words)
print("Number of sentences:", num_sentences)
print("Number of paragraphs:", num_paragraphs)
print("Letter frequencies:", len(letter_frequencies))
print("Word frequencies:", len(word_frequencies))
print("Sentence frequencies:", len(sentence_frequencies))
print("Pair of words frequencies:", len(pair_of_words_frequencies))
