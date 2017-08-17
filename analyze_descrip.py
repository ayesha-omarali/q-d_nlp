from collections import Counter
import numpy as np
from nltk import word_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
import csv
import os
import ast
from textblob import *

from textblob_wc.py import wc


word_count = sorted(d, key=lambda i: int(wc[i]))

# print word_count[2]
print wc.items()[2]
