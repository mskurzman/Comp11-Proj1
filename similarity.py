# Maya Kurzman
# Comp11
# Project 1
# similarity.py

"""
this program will get the name of two .txt files and a lexicon as command line 
arguments, and determine the five most common words between the .txt files
that are also present in their lexicon and their frequencies.
"""

from string import ascii_letters
import sys
import heapq

def count_number_matched_words(text_1, text_2, lexicon)
    words_1 = clean_word(text_1)
    list_words_1 = words_1.split()
    words_2 = clean_word(text_2)
    list_words_2 = words_2.split()
    list_lexicon = lexicon.split()
    list_common_words = []
    frequency_dictionary = {}
    list_common_words = create_list_common_words(list_words_1, list_words_2, \
    list_lexicon, list_common_words)
    for word in list_common_words:
        frequency_dictionary[word] = 0
    frequency_dictionary = store_word_and_frequency(list_words_1, list_common_words, \
    frequency_dictionary)
    frequency_dictionary = store_word_and_frequency(list_words_2, list_common_words, \
    frequency_dictionary)
    print_common_words(list_common_words)
    print_top_5(frequency_dictionary)
    
def create_list_common_words(list_words_1, list_words_2, list_lexicon, list_common_words):
    for word in list_words_1:
        string = word
        if string in list_lexicon and string in list_words_2:
            if string not in list_common_words:
                list_common_words = list_common_words + [string]
    return list_common_words

def clean_word(text)
    text = text.replace("\n", " ")
    return(''.join(char for char in text if char in
    ascii_letters or char == " ").lower()
    
def store_word_and_frequency(list_words, list_common_words, frequency_dictionary):
    for word in list_words:
        if word in list_common_words:
            frequency_dictionary[word] += 1
    return frequency_dictionary

def print_common_words(list_common_words)
    print('Common words:", end = " ")
    length_list = 0
    while length_list < len(list_common_words)-1:
        length_list_ +=1
    print(list_common_words[length_list])
    
def print_top_5(frequency_dictionary):
    most_common_words = heapq.nlargest(5, frequency_dictionary, \
    key = frequency_dictionary.get)
    print("Most common words: ", end = "")
    for key in most_common_words:
        print(key, '(', frequency_dictionary[key], ')', sep = "", end = " ")
    print()
    
def main():
    # for first.txt file:
    with open(sys.argv[1], 'r') as textfile_1:
        text_1 = textfile_1.read()
    
    # for second .txt file:
    with open (sys.argv[2], 'r') as textfile_2:
        text_2 = textfile_2.read()
        
    # for lexicon:
    with open (sys.argv[3], 'r') as textfile_3:
        text_3 = textfile_3.read()

    count_number_matched_words(text_1, text_2, lexicon)
    
if __name__ == "__main__":
    main()
