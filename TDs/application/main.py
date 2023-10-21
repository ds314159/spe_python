import pandas as pd
import numpy as np
from Corpus import Corpus
from Document import *

# récupérer notre enregistrement corpus (l'ensemble de nos docs)
docs = pd.read_csv("corpus.csv", sep='\t')

# instancier un objet Corpus pour y stocker sous forme d'instances d'autres objets les articles acquis
corpus_articles = Corpus("arxiv et reddit")

for _ , doc in docs.iterrows():
    corpus_articles.add_document(doc['titre'], doc['auteur'],doc['date'],doc['url'],doc['texte'])

corpus_articles.save('corpus_articles.pkl')

bbbb = Corpus.load('corpus_articles.pkl')

arx = ArxivDocument("nnnn", "nnnnn", "2016-11-02 19:48:34", "ggggg", "vvvv")

arx.afficher_infos()

red = RedditDocument("nnnn", "nnnnn", "2016-11-02 19:48:34", "ggggg", "vvvv", nb_commentaires=13)

red.afficher_infos()

print(red.get_type())
print(arx.get_type())






