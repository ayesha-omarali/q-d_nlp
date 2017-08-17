from textblob import TextBlob
from nltk.corpus import stopwords
from collections import Counter
import string
import time

s_words = stopwords.words('english')
s_words = s_words + ['of', 'the', 'on', 'and', 'with', 'for']

def get_ngrams(ngram_size):
    with open("captions.txt", "r") as data:
        data = data.readlines()
    data = [line.strip().translate(None, string.punctuation) for line in data if line]
    start_time = time.time()
    grams = []
    start = time.time()
    for i in range(len(data)-1):
        line = data[i]
        line_list = line.split()
        line_filter = [word for word in line_list if word.lower() not in s_words]
        line = ' '.join(line_filter)
        grams = grams + list(TextBlob(line).ngrams(ngram_size))
    end_time = time.time() - start_time
    return grams, end_time

ngrams = open("textblob_get_trigrams.txt", "w")
x, time = get_ngrams(3)
ngrams.write(' '.join([str(time), "\n\n"]))

x = Counter(x)
ngrams.write(str(x.most_common(250)))
