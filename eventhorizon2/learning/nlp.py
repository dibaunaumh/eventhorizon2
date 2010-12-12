import nltk
from nltk.stem.porter import PorterStemmer

__author__ = 'vlad'


def clean_text(text,language='english'):
    stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    stemed_tokens = stemmer.stem(tokens)
    stopwords = nltk.corpus.stopwords.words(language)
    content = [w for w in stemed_tokens if w.lower() not in stopwords]

    



