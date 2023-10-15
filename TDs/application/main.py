import pandas as pd
import numpy as np
from Corpus import Corpus

# récupérer notre enregistrement corpus (l'ensemble de nos docs)
docs = pd.read_csv("corpus.csv", sep='\t')

# instancier un objet Corpus pour y stocker sous forme d'instances d'autres objets les articles acquis
corpus_articles = Corpus("arxiv et reddit")

for _ , doc in docs.iterrows():
    corpus_articles.add_document(doc['titre'], doc['auteur'],doc['date'],doc['url'],doc['texte'])

corpus_articles.save('corpus_articles.pkl')

bbbb = Corpus.load('corpus_articles.pkl')








