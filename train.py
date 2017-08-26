import re
import numpy as np
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

fname = open("Political-media-DFE.csv")
df = pd.read_csv(fname, error_bad_lines=False)
new_df = pd.DataFrame()

def cleaner(text):
	try:
	    text = re.sub('<[^>]*>', ' ', text)    # removes HTML from tweets
	    text = re.sub('(http|https)://[^ ]+ ', '', text)    # removes all the hyperlinks
	    text = re.sub('\s\s+', '', text)    # removes all the extra whitespaces
	    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P|[^T_T])', text)    #find all emoticons
	    text = re.sub('[\W]+', ' ', text.lower()) + ''.join(emoticons).replace('-', '')  # appends emmoticons at the end.
	except:
		text = text

	return text

new_df['embed'] = df['embed'].apply(cleaner)

def type_to_token(tag):
	if tag=='neutral':
		return 0
	else:
		return 1

new_df['bias'] = df.embed.apply(type_to_token)

# Processing into tokens
porter = PorterStemmer()

def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
#     return [porter.stem(word) for word in text.split()]
    for word in text.split():
        try:
            return porter.stem(word)
        except Exception:
            return word

tokenizer_porter(new_df.ix[3000, "embed"])
nltk.download("stopwords")
from nltk.corpus import stopwords
stop = stopwords.words('english')

X_train, X_test, y_train, y_test = train_test_split(new_df['embed'], new_df['bias'], test_size=0.33, random_state=42) 

print(X_test)

classes = np.array([0,1])
vect = HashingVectorizer(decode_error='ignore',
                         n_features = 2**21,
                         preprocessor = None,
                         tokenizer=tokenizer
                        )
clf = SGDClassifier(loss='log', random_state=1, n_iter=1)
X_train = vect.transform(X_train)
clf.partial_fit(X_train, y_train, classes=classes)	

def token_to_type(num):
	if num == 1:
		return "partial"
	return "bias"

# print("The prediction : {}".format(token_to_type(clf.predict(X_test[]))))
X_test = vect.transform(X_test)
print('Accuracy: {:.2f}%'.format(clf.score(X_test, y_test)*100))

clf.partial_fit(X_test, y_test)

import pickle, os

dest = os.path.join('pkl_objects')
if not os.path.exists(dest):
	os.makedirs(dest)

pickle.dump(
	clf, open(os.path.join(dest, 'classifier.pkl'), 'wb')
	)

