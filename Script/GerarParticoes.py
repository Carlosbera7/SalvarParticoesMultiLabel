from iterstrat.ml_stratifiers import MultilabelStratifiedKFold
import pickle
import logging

def gerar_particoes_multilabel(X_tfidf, y, n_splits=10, caminho = 'particoes.pkl'):
    """
    Gera partições estratificadas multilabel com IterativeStratification.
    """
    logging.info(f"📁 Gerando {n_splits} partições multilabel para validação cruzada...")

    mskf = MultilabelStratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    folds = []

    for train_idx, test_idx in mskf.split(X_tfidf, y):
        folds.append((train_idx, test_idx))

    with open(caminho, 'wb') as f:
        pickle.dump(folds, f)

    logging.info(f"✅ Partições salvas em {caminho}")
    
    
