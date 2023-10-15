class Corpus:

    def __init__(self, nom):
        self.nom = nom
        self.authors = {}  # Dictionnaire des auteurs
        self.id2doc = {}  # Dictionnaire des documents
        self.ndoc = 0  # Comptage des documents
        self.naut = 0  # Comptage des auteurs

    def add_document(self, titre, auteur, date, url, texte):
        # Créer une nouvelle instance de Document
        doc = Document(titre, auteur, date, url, texte)

        # Incrémenter le comptage des documents
        self.ndoc += 1

        # Ajouter le document à id2doc
        self.id2doc[titre] = doc

        # Vérifier si l'auteur existe déjà dans authors