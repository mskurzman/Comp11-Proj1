# Maya Kurzman
# Comp11
# Project 1
# Sentiment_2.py

"""
This program will get the name of a lexicon as a command line argument,
read in the lexicon, and store each keyword (string) with its associated
sentiment score (float).

Looked up how to delete elements of a list
Looked up how to get file input from command line
Got both answers from stack overflow

I talked about the pseudocode with Sam Graber-Hahn
"""

from string import ascii_letters
import sys
# def store_words_in_list(filename):

def store_sentiment_score(list_words_and_scores):
    length_list - len(list_words_and_scores)
    while length_list != 0:
        keyword = list_words_and_scores[0]
        score = list_words_and_scores[1]
        print(keyword, score)
        del list_words_and_scores[0]
        del list_words_and_scores[0]
        length_list -= 2
        
def main()
    with open(sys.argv[1], 'r' as filename:
        text = filename.read()
    list_words = text.split()
    store_sentiment_score (list_words)
#    print(words, sep = " ")
    
if __name == "__main__":
    main()
