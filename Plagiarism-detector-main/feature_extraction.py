from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def bow_features(texts):
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(texts)
    return features, vectorizer

def tfidf_features(texts):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(texts)
    return features, vectorizer
