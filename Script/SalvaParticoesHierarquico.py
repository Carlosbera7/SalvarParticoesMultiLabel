import pandas as pd
import numpy as np
from skmultilearn.model_selection import iterative_train_test_split
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('stopwords')

# Carrega a base de dados
data = pd.read_csv('Data/2019-05-28_portuguese_hate_speech_hierarchical_classification_reduzido.csv')

# Divide os dados em texto e rótulos
X = data['text']  # Coluna com o texto
y = data.drop(columns=['text'])  # Todas as colunas exceto o texto

# Vetorização do texto usando TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
portuguese_stopwords = stopwords.words('portuguese')
vectorizer = TfidfVectorizer(max_features=5000, stop_words=portuguese_stopwords)
X_tfidf = vectorizer.fit_transform(X)

# Estratificação hierárquica com 30% para o conjunto de teste
X_train, y_train, X_test, y_test = iterative_train_test_split(
    X_tfidf, y.values, test_size=0.3
)

# Salva as partições em arquivos CSV
train_data = pd.DataFrame(X_train.toarray(), columns=vectorizer.get_feature_names_out())
train_labels = pd.DataFrame(y_train, columns=y.columns)
test_data = pd.DataFrame(X_test.toarray(), columns=vectorizer.get_feature_names_out())
test_labels = pd.DataFrame(y_test, columns=y.columns)

# Combina dados e rótulos para exportação
train = pd.concat([train_data, train_labels], axis=1)
test = pd.concat([test_data, test_labels], axis=1)

# Salva os dados em arquivos CSV
train.to_csv('Data/train_data_hierarquico.csv', index=False)
test.to_csv('Data/test_data_hierarquico.csv', index=False)

print("Partições de treino e teste geradas e salvas com sucesso!")

import matplotlib.pyplot as plt
import seaborn as sns

# Calcula a soma de instâncias para cada rótulo
train_class_distribution = train_labels.sum(axis=0)
test_class_distribution = test_labels.sum(axis=0)

# Configura o estilo do Seaborn
sns.set(style="whitegrid")

# Cria o gráfico para a partição de treino
plt.figure(figsize=(12, 6))
sns.barplot(x=train_class_distribution.index, y=train_class_distribution.values, palette="viridis")
plt.title("Distribuição das Classes - Treino", fontsize=16)
plt.xlabel("Classes", fontsize=12)
plt.ylabel("Número de Instâncias", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Cria o gráfico para a partição de teste
plt.figure(figsize=(12, 6))
sns.barplot(x=test_class_distribution.index, y=test_class_distribution.values, palette="coolwarm")
plt.title("Distribuição das Classes - Teste", fontsize=16)
plt.xlabel("Classes", fontsize=12)
plt.ylabel("Número de Instâncias", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

