# Maya Kurzman
# Comp11
# Project 1
# sentiment_4.py

"""
This program will get the name of a .txt file and a lexicon as command line 
arguments, and counts the number of words that are present in both the
.txt file and in the lexicon.
"""

from string import ascii_letters
import sys

def count_number_matched_words(text, lexicon):
    words = clean_word(text)
    list_words = words.split()
    list_lexicon = lexicon.split()
    number_matched_words = 0
    for word in list_words:
       string = word
       if string in list lexicon:
           number_matched_words += 1
    print(number_matched_words)
    
def clean_word(text):
    text = text.replace("\n", " ")
    return(''.join(char for char in text if char in
    ascii_letters or char == " ")).lower()em
    
def store_sentiment_score(list_words_and_scores):
    length_list = len(list_words_and_scores)
    while length_list != 0:
        keyword = list_words_and_scores[0]
        score = list_words_and_scores[1]
        print(keyword, score)
        del list_words_and_scores[0]
        del list_words_and_scores[0]
        length_list -= 2
       
def main():
    # for .txt file:
    with open(sys.argv[1], 'r') as textfile:
        text = textfile.read()
        
    # for lexicon:
    with open(sys.argv[2], 'r') as lexiconfile:
        lexicon = lexiconfile.read()
    count_number_matched_words(text, lexicon)
    
if __name__ == "__main__":
    main()
