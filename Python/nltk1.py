import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

en_stop = stopwords.words('english')
print(sorted(en_stop))

pos = nltk.pos_tag(['amazing'])
print(pos)
