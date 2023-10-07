import collections
import string

with open('/Users/mahsa/Downloads/word_cloud/98-0.txt', encoding="utf8") as file:
    text = file.read()

stopwords = set(line.strip() for line in open('/Users/mahsa/Downloads/word_cloud/stopwords'))


wordcount = {}


words = text.lower().split()
translator = str.maketrans('', '', string.punctuation)
words = [word.translate(translator) for word in words]


for word in words:
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("\"", "")
    word = word.replace("“", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

d = collections.Counter(wordcount)


for word, count in d.most_common(10):
    print(word, ": ", count)
