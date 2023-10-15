import pandas as pd


docs = pd.read_csv("corpus.csv", sep='\t')


id2doc = docs['texte'].to_dict()

for clef, valeur in id2doc.items():
    print(clef)
    print(valeur)



