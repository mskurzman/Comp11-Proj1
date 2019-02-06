# Maya Kurzman
# Comp11
# Project 1
# Sentiment_1.py

"""
This program will remove the punctuation and other formatting for text
in a file, store each word into a list, and print out the text.

I talked about the pseudocode with Sam Graber-Hahn
"""

from string import ascii_letters
import sys
# def store)wirds_in_list(filename):

def clean_word(text):
    return(''.join(char for char in text if char in
    ascii_letters or car == " ")).lower()
    
def main():
    with open(sys.argv[1], 'r') as filename:
        text - filename.read()
    text = text.replace("\n", " ")
    words = clean_word(text)
    list_words = words.split()
    print(words, sep = " ")
    
if __name__ == "__main__:
    main()
