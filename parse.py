from collections import Counter
import numpy as np
from nltk import word_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
import csv
import os
import ast


# with open('bnb_sample.csv', 'rb') as csvfile:
#     data = csvfile.readlines()
#     data = [line.rstrip() for line in data if line]

# reviews = open('reviews.csv', 'w')
# descriptions = open('descriptions.csv', 'w')
# counter = 0
# for line in data:
#     if line and line[:6].isdigit():
#         reviews.write(line)
#     elif line:


# gen = iter(data)
# while gen.next():
#     temp = ""
#     while not gen.next()[:6].isdigit():
#         temp = temp + gen.next()
#     descriptions.write(temp)
    # descriptions.write(temp)
    # reviews.write(gen.next())


def write_descriptions(data):
    gen = iter(data)
    try:
        while True:
            temp = ""
            while not gen.next()[:6].isdigit():
                temp = temp + gen.next()
            descriptions.write(temp)
            descriptions.write('\n')
    except StopIteration:
        print "iteration done"
        descriptions.close()



# def bracket_match(line):
#     try:
#         while True:



# def filter_descriptions(data):
#     gen = iter(data)
#     try:
#         while True:
#             if "[{" in gen.next():
#                 bracket_match(gen.next())


# with open('bnb_US_1000.csv', 'r') as raw:
#     rawbnb = raw.readlines()
# rawparse = open("raw_parse.csv", "w")

# def string_to_list(item):
#     try:
#         l = [n.strip() for n in ast.literal_eval(str(item))]
#     except Exception as e:
#         l = []
#     return l

# def string_to_description(item):
#     count = 1
#     l = []
#     try:
#         for n in ast.literal_eval(str(item)):
#             l.append('{} {}'.format(count,n.strip().lower()))
#             count += 1
#     except Exception as e:
#         l = []
#     return l

# for line in rawbnb:
#     rawparse.write(str(string_to_description(line)))

def freq_dist(data):
    """
    :param data: A string with sentences separated by '\n'
    :type data: str
    """
    ngram_vectorizer = CountVectorizer(analyzer='word', tokenizer=word_tokenize, ngram_range=(1, 1), min_df=1)
    X = ngram_vectorizer.fit_transform(data.split('\n'))
    vocab = list(ngram_vectorizer.get_feature_names())
    counts = X.sum(axis=0).A1
    return Counter(dict(zip(vocab, counts)))


# a = bnb_US['picture_captions'][0]
# a= ast.literal_eval(a)
# string =''
# for a in bnb_US['picture_captions'].head(1):
#     l = [n.strip().encode('ascii','ignore') for n in ast.literal_eval(a)]
#     print l
#     string += ' '.join(l)

# freq_dist(string)
