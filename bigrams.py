from nltk.corpus import stopwords
from collections import Counter
import string
import time

s_words = stopwords.words('english')
s_words = s_words + ['of', 'the', 'on', 'and', 'with', 'for']

caption_bigrams = open("bigrams_filtered_before.txt", "w")

def get_ngrams():
    with open("captions.txt", "r") as data:
        data = data.readlines()
    data = [line.strip().translate(None, string.punctuation) for line in data if line]
    bigrams = []
    start_time = time.time()
    for i in range(len(data)-1):
        line = data[i]
        line_list = line.split()
        line_filter = [word for word in line_list if word.lower() not in s_words]
        line = ' '.join(line_filter)

        next_line = data[i+1]
        next_line_list = next_line.split()
        next_line_filter = [word for word in next_line_list if word.lower() not in s_words]
        next_line = ' '.join(next_line_filter)
        line = [line] + [next_line]
        bigrams = bigrams + [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    end_time = time.time() - start_time
    caption_bigrams.write(' '.join([str(end_time), "\n\n"]))
    return bigrams


x = Counter(get_ngrams())
caption_bigrams.write(str(x.most_common(250)))
