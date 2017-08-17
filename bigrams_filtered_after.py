from nltk.corpus import stopwords
from collections import Counter
import string

s_words = stopwords.words('english')
s_words = s_words + ['of', 'the', 'on', 'and', 'with', 'for']

def get_ngrams():
    with open("captions.txt", "r") as data:
        data = data.readlines()
    data = [line.strip().translate(None, string.punctuation) for line in data if line]
    result = []
    for i in range(len(data)-1):
        line = data[i]
        next_line = data[i+1]
        line = [line] + [next_line]
        bigrams = [i for i in [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]]
        result = result + [i for i in bigrams if i[0] not in s_words if i[1] not in s_words]
    return result

x = Counter(get_ngrams())
caption_bigrams = open("bigrams_filtered_after.txt", "w")
caption_bigrams.write(str(x.most_common(250)))
