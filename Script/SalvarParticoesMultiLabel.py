import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from skmultilearn.model_selection import iterative_train_test_split
from nltk.corpus import stopwords
import logging
import os

nltk.download('stopwords')

# Configurações de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PartitionSaver:
    def __init__(self, file_path, output_dir, min_label_count=10):
        self.file_path = file_path
        self.output_dir = output_dir
        self.min_label_count = min_label_count
        self.vectorizer = None

    @staticmethod
    def clean_text(text):
        text = re.sub(r'[^\w\s]', '', str(text).lower())
        stop_words = set(stopwords.words('portuguese'))
        words = [word for word in text.split() if word not in stop_words]
        return ' '.join(words)

    def load_and_prepare_data(self):
        logging.info("Carregando os dados...")
        data = pd.read_csv(self.file_path)
        data['text'] = data['text'].apply(self.clean_text)
        X = data['text']
        y = data.drop(columns=['text'])
        label_counts = y.sum(axis=0)
        valid_labels = label_counts[label_counts >= self.min_label_count].index
        y = y[valid_labels]
        return X, y

    def partition_data(self, X, y, test_size=0.3):
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words=stopwords.words('portuguese'))
        X_tfidf = self.vectorizer.fit_transform(X)

        X_train, y_train, X_test, y_test = iterative_train_test_split(X_tfidf, y.values, test_size=test_size)
        os.makedirs(self.output_dir, exist_ok=True)
        pd.DataFrame(X_train.toarray()).to_csv(os.path.join(self.output_dir, 'X_train.csv'), index=False)
        pd.DataFrame(X_test.toarray()).to_csv(os.path.join(self.output_dir, 'X_test.csv'), index=False)
        pd.DataFrame(y_train).to_csv(os.path.join(self.output_dir, 'y_train.csv'), index=False)
        pd.DataFrame(y_test).to_csv(os.path.join(self.output_dir, 'y_test.csv'), index=False)
        logging.info(f"Partições salvas em {self.output_dir}")

    def run(self):
        X, y = self.load_and_prepare_data()
        self.partition_data(X, y)
        
if __name__ == "__main__":
    # Etapa 1: Salvar as partições
    partition_saver = PartitionSaver(
        file_path='2019-05-28_portuguese_hate_speech_hierarchical_classification.csv',
        output_dir='./partitions',
        min_label_count=10
    )
    partition_saver.run()    