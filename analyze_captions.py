from nltk.corpus import stopwords
from collections import Counter



def get_caption_freq():
  swords = stopwords.words('english')

  with open("captions.txt", "r") as data:
    data = data.readlines()
    data = [line.strip() for line in data if line]

  word_list = []

  for line in data:
    line = line.split()
    for word in line:
      if not word in swords:
        word_list = word_list + [word]

  most_common_captions = open("most_common_captions.txt", "w")
  x = Counter(word_list)
  most_common_captions.write(str(x.most_common(250)))
  print x.most_common(50)
  return


def get_ngrams():
  with open("captions.txt", "r") as data:
    data = data.readlines()
    data = [line.strip() for line in data if line]

    bigrams = []
    for line in data:
      bigrams = bigrams + [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]

get_ngrams()
