from nltk.tokenize import sent_tokenize
import pickle
import os
import numpy as np
import random
import sys

def article_scorer(text):
	sent_tokenize_list = sent_tokenize(text)
	# sys.path.append(os.getcwd())
	clf = pickle.load(open('classifier.pkl', 'rb'))
	bias = 0
	partisan = 0
	for sentence in sent_tokenize_list:
		label, probab = clf.predict(sentence), clf.predict_proba(sentence)
		if label[0] == 0:
			bias += 1
			bias_prob += probab
		else:
			partisan += 1
			partisan_probab += probab

	norm_bias, norm_partisan = bias_prob/bias, partisan_probab/partisan_probab 

	if norm_bias<0.3:
		return random.uniform(0.2, 0.3)
	return norm_bias 