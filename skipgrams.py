from nltk import skipgrams

from nltk.corpus import stopwords
from nltk import skipgrams
from collections import Counter
import string
import time

s_words = stopwords.words('english')
s_words = s_words + ['of', 'the', 'on', 'and', 'with', 'for']
caption_bigrams = open("skipgrams_filtered_before.txt", "w")

def get_skipgrams():
    with open("captions.txt", "r") as data:
        data = data.readlines()
    data = [line.strip().translate(None, string.punctuation) for line in data if line]
    skippers = []
    start_time = time.time()
    for i in range(len(data)-1):
        line = data[i]
        line_list = line.split()
        line_filter = [word for word in line_list if word.lower() not in s_words]
        line = ' '.join(line_filter)

        skip = list(skipgrams(line.split(), 2, 2))
        skippers = skippers + skip
    end_time = time.time() - start_time
    caption_bigrams.write(' '.join([str(end_time), "\n\n"]))
    return skippers

x = Counter(get_skipgrams()).most_common(250)
caption_bigrams.write(str(x))
