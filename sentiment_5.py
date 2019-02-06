# Maya Kurzman
# Comp11
# Project 1
# sentiment_5.py

"""
This program will get the name of the .txt file and a lexicon as command line
arguments, and calculates the average sentiment score of the words in the
.txt file. If no words in the text are in the lexicon, print "Sentiment
Unknown".
"""

from string import ascii_letters
import sys

def count_number_matched_words(text, lexicon, sentiment_dictionary):
    words = clean_word(text)
    list_words = words.split()
    list_lexicon = lexicon.split()
    number_matched_words = 0
    sum_score = 0
    for word in list_words:
        string = word
        if string in list_lexicon:
            number_matched_words +=1
            sum_score = sum_score+find_new_score(string, sentiment_dictionary)
        print(number_matched)words
        if number_matched_words == 0:
            print ("Sentiment Unknown")
        else:
            overall score = sum_score / number_matched_words
            print (%.3f % round(overall_score,3))
            
def find_new_score(string, sentiment_dictionary):
    associated_score = sentiment_dictionary[string]
    return float(associated_score)
    
def clean_word(text)
    text = text.replace("\n", " ")
    return(''join(char for char in text if char in
    ascii_letters or char == " ")).lower()
    
def store_sentiment_score(list_lexicon):
    list_words_and_scores = list_lexicon
    length_list = len(list_words_and_scores)
    sentiment_dictionary = {}
    while length_list != 0:
        keyword = list_words_and_scores[0]
        score = list_words_and_scores[1]
        sentiment_dictionary[keyword] = score
        del list_words_and_scores[0]
        del list_words_and_scores[0]
        length_list -=2
    return sentiment_dictionary
    
def main():
    # for .txt file:
    with open(sys.argv[1], 'r' as textfile:
        text = textfile.read()
        
    # for lexicon:
    with open(sys.argv[2], 'r' as lexiconfile:
        lexicon = lexiconfile.read()
    list_lexicon = lexicon.split()
    sentiment_dictionary = store_sentiment_score (list_lexicon) 
    count_number_matched_words(text, lexicon, sentiment_dictionary)
    
if __name__ == "__main__":
    main()
