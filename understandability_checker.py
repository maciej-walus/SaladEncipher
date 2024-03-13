import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import words

nltk.download('words')

def is_understandable(sentence):


    words_in_the_sentence = word_tokenize(sentence)
    pos_tags = pos_tag(words_in_the_sentence)
    english_word_count = sum(1 for word, pos in pos_tags if word.lower() in words.words())

    # Setting a threshold for the percentage of valid English words in the sentence
    threshold_percentage = 0.5
    percentage_valid_words = english_word_count / len(words_in_the_sentence)

    if percentage_valid_words >= threshold_percentage:
        return 1

    else:
        return 0