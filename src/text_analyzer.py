import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA

class TextAnalyzer:
    """
    Extracts keywords and identifies the nature of conversation using TF-IDF and LDA.
    """
    
    def __init__(self, chat_parser):
        self.initialize()    
    
        self.chat_parser = chat_parser
        self.documents = chat_parser.get_messages()
        self.stop_words = set(stopwords.words('english'))
        
    def initialize(self):
        try:
            stopwords.words('english')
        except LookupError:
            nltk.download('stopwords')
        try:
            wordnet.synsets('test')
        except LookupError:
            nltk.download('wordnet')
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
    def clean_text(self):
        self.documents = self.documents.lower()
        self.documents = re.sub(r'[^a-z0-9\s]', '', self.documents)  # Keep only alphanumeric characters
        
        tokens = nltk.word_tokenize(self.documents)
        tokens = [word for word in tokens if word not in self.stop_words]
        
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        return lemmas
    
    def find_keywords(self, n=5):
        cleaned_text = " ".join(self.clean_text())
        
        vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([cleaned_text])
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]
        
        top_indices = scores.argsort()[::-1][:n]  # highest scores first
        top_keywords = [feature_names[i] for i in top_indices]
        return ", ".join(top_keywords)
    
    def conversation_topic(self):
        lemmas = self.clean_text()
        count_vec = CountVectorizer(analyzer=lambda x: x)
        term_matrix = count_vec.fit_transform([lemmas])
        feature_names = count_vec.get_feature_names_out()
        
        lda = LDA(n_components=1, random_state=42, max_iter=100)
        lda.fit(term_matrix)
        
        topic_distribution = lda.components_[0]
        total_topics = min(2, len(feature_names))
        top_indices = topic_distribution.argsort()[:-total_topics - 1:-1]
        topic_keywords = [feature_names[i] for i in top_indices]

        if len(topic_keywords) == 1:
            return topic_keywords[0]
        else:
            keywords = ", ".join(topic_keywords[:-1]) + " and " + topic_keywords[-1]
            return keywords