from nltk.corpus import stopwords
from collections import Counter
from textblob import TextBlob
import string
import time

s_words = stopwords.words('english')
s_words = s_words + ['of', 'the', 'on', 'and', 'with', 'for']
caption_bigrams = open("noun_phrases_tb.txt", "w")

def get_ngrams():
    with open("captions.txt", "r") as data:
        data = data.readlines()
    data = [line.strip().translate(None, string.punctuation) for line in data if line]
    nouns = []
    start_time = time.time()
    for i in range(len(data)-1):
        line = data[i]
        line_list = line.split()
        line_filter = [word for word in line_list if word.lower() not in s_words]
        line = ' '.join(line_filter)
        nouns = nouns + list(TextBlob(line).noun_phrases)
    end_time = time.time() - start_time
    caption_bigrams.write(' '.join([str(end_time), "\n\n"]))
    return nouns


x = Counter(get_ngrams())
caption_bigrams.write(str(x.most_common(250)))
