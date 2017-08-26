from nltk.tokenize import sent_tokenize
import pickle
import os

def article_scorer(text):
	sent_tokenize_list = sent_tokenize(text)
	clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))
	bias = 0
	partisan = 0
	for sentence in sent_tokenize_list:
		label, probab = clf.predict(sentence), clf.predict_proba(sentence)
		if label[0] = 0:
			bias += 1
			bias_prob += probab
		else:
			partisan += 1
			partisan_probab += probab

	norm_bias, norm_partisan = bias_prob/bias, partisan_probab/partisan_probab 
