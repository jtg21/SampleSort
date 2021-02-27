import pickle


#Stores the list of keywords
def storeKeywords(KEYWORDS):
	file = open("keywords", "ab")
	pickle.dump(KEYWORDS, file)
	file.close()


#Fetches saved keywords and returns a list containing the strings
def fetchKeywords():
	file = open("keywords", "rb")
	keywords = pickle.load(file)
	return keywords
