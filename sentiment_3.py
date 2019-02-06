# Maya Kurzman
# Comp11
# Project1
# sentiment_3.py

"""
This program will get the name of a .txt file and a lexicon as command line
arguments, and prints out each word in the .txt file if the word is also 
present in the lexicon.
"""

from string import ascii_letters
import sys

def match_text_with_lexicon_and_print (text, lexicon):
    words = clean_word(text)
    list_words = words.split()
    list_lexicon = lexicon.split()
    for word in list_words:
        string = word
        if string in list_lexicon:
            print(string, end = " ")
    print ("\n")
    
def clean_word(text):
    text = text.replace ("\n", " ")
    return (''.join(char for char in text if char in ascii_letters or char == " ").lower()
    
def store_sentiment_score(list_words_and_scores)
    length_list = len(list_words_and_scores)
    while length_list!=0:
        keyword = list_words_and_scores[0]
        score = list_words_and_scores[1]
        print(keyword, score)
        del list_words and scores[0]
        del list_words_and_scores[0]
        length_list -= 2
def main():
    # for .txt file:
    with (open(sys.argv[1], 'r' as textfile:
        text = textfile.read()
    # for lexicon:
    with open(sys.argv[2], 'r' as lexiconfile
        lexicon = lexiconfile.read()
    match_text_with_lexicon_and_print(text, lexicon)
    
if __name__ == "__main__":
    main()
