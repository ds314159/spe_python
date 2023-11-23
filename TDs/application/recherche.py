from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Supposons que vous avez une liste de textes de documents
documents = [doc.texte for doc in corpus_articles.id2doc.values()]

# Initialisation du vectoriseur TF-IDF
vectorizer = TfidfVectorizer()

# Vectorisation des documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Fonction pour traiter la requête et trouver les documents pertinents
def rechercher_documents(requete):
    # Nettoyer et vectoriser la requête
    requete_vectorisee = vectorizer.transform([requete])

    # Calculer la similarité cosinus
    cos_similarities = cosine_similarity(requete_vectorisee, tfidf_matrix)

    # Récupérer les scores de similarité pour chaque document
    scores = cos_similarities[0]

    # Créer un DataFrame pour afficher les résultats
    resultats = pd.DataFrame({
        'Document': corpus_articles.id2doc.keys(),
        'Score': scores
    })

    # Trier les résultats par score de similarité
    resultats_ordonnes = resultats.sort_values(by='Score', ascending=False)

    return resultats_ordonnes

# Interface en ligne de commande
if __name__ == "__main__":
    mot_cle = input("Entrez votre mot-clé de recherche : ")
    resultats = rechercher_documents(mot_cle)
    print(resultats.head(10))  # Afficher les 10 premiers résultats
