import collections
import string

# file=open('/Users/mahsa/Downloads/word_cloud/98-0.txt', encoding="utf8")
with open('/Users/mahsa/Downloads/word_cloud/98-0.txt', encoding="utf8") as file:
    text = file.read()

# If you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('/Users/mahsa/Downloads/word_cloud/stopwords'))

# Create your data structure here.
wordcount = {}

# Instantiate a dictionary, and for every word in the file, add to
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation,
words = text.lower().split()
translator = str.maketrans('', '', string.punctuation)
words = [word.translate(translator) for word in words]
# and use case delimiters. The functions lower() and split() will be useful!

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

# After building your wordcount, you can then sort it and return the first
# n words. If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)

# Print the top 10 most common words and their frequencies
for word, count in d.most_common(10):
    print(word, ": ", count)
