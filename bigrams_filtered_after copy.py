from nltk.corpus import stopwords
from collections import Counter

s_words = stopwords.words('english')

def get_ngrams():
  with open("captions.txt", "r") as data:
    data = data.readlines()
  data = [line.strip() for line in data if line]
  bigrams = []
  for i in range(len(data)-1):
    line = data[i]
    next_line = data[i+1]
    line = [line] + [next_line]
    print "before", line
    print "after", [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    bigrams = bigrams + [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    result = [i for i in bigrams if any(not (word in i) for word in s_words)]
  return result

x = Counter(get_ngrams())
caption_bigrams = open("bigrams_filtered_after.txt", "w")
caption_bigrams.write(str(x.most_common(250)))
