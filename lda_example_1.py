import nltk
import numpy as np
from nltk.stem.porter import *
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
import gensim
import pandas as pd

data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
data_text = data[['headline_text']]
data_text['index'] = data_text.index
documents = data_text

print(len(documents))

print(documents[:5])

# Data Pre-Processing
# Performing the following steps
#   - Tokenization : Split the words into sentences and the sentences into words.
#     Lowercase the words abd remove punctuation
#   - Words that have fewer than 3 characters are removed
#   - All stopwords are removed
#   - Words are lemmatized - words in third person are changed to first person and
#     verbs in past and future tenses are changed into present
#   - Words are stemmed - words are reduced to their root form

np.random.seed(2018)

nltk.download('wordnet')


def lemmatize_stemming(text):
    return PorterStemmer().stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


doc_sample = documents[documents['index'] == 4310].values[0][0]

print('original document: ')
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print('\n\n tokenized and lemmatized document: ')
print(preprocess(doc_sample))

# Preprocess the headline text, saving the results as 'processed_docs'
processed_docs = documents['headline_text'].map(preprocess)
print(processed_docs[:10])
