from datetime import datetime
import pandas as pd


import pickle

########################################################################################################################
class Author:

    def __init__(self, name):
        self.name = name
        self.ndoc = 0  # Nombre de documents publiés par l'auteur
        self.production = {}  # Dictionnaire des documents écrits par l'auteur

    def add(self, doc):
        """
        Ajoute un document à la production de l'auteur
        """
        self.ndoc += 1
        self.production[doc.titre] = doc

    def __str__(self):
        return f"{self.name} - {self.ndoc} document(s) publié(s)"

########################################################################################################################

class Document:

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        self.url = url
        self.texte = texte


    def afficher_infos(self):
        return print(f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nTexte: {self.texte}")

    def __str__(self):
        return self.titre



class RedditDocument(Document):

    def __init__(self, source, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires
        self.type = source

    def get_nb_commentaires(self):
        return self.nb_commentaires

    def set_nb_commentaires(self, nb_commentaires):
        self.nb_commentaires = nb_commentaires

    def get_type(self):
        return self.type

    def afficher_infos(self):
        print(f"Source: {self.type}")
        super().afficher_infos()
        print(f"Nombre de commentaires: {self.nb_commentaires}")


class ArxivDocument(Document):

    def __init__(self, source, titre, auteur, date, url, texte, co_auteurs):
        super().__init__(titre, auteur, date, url, texte)
        self.co_auteurs = co_auteurs
        self.type = source

    def get_co_auteurs(self):
        return self.co_auteurs

    def set_co_auteurs(self, co_auteurs):
        self.co_auteurs = co_auteurs

    def get_type(self):
        return self.type

    def afficher_infos(self):
        print(f"Source: {self.type}")
        super().afficher_infos()
        print(f"Co-auteurs: {self.co_auteurs}" if self.co_auteurs else "Co_auteurs: aucun")



class DocumentFactory:

    @staticmethod
    def create_document(source,titre, auteur, date, url, texte, co_auteurs, nb_commentaires):
        if source == "reddit":
            return RedditDocument(source, titre, auteur, date, url, texte, nb_commentaires)
        elif source == "arxiv":
            return ArxivDocument(source, titre, auteur, date, url, texte, co_auteurs)
        else:
            raise ValueError(f"Type de document {source} non reconnu")

    def create_corpus(chemin_donnees_acquises, nom_corpus):
        # récupérer notre enregistrement corpus (l'ensemble de nos docs)
        docs = pd.read_csv(chemin_donnees_acquises, sep='\t')

        # instancier un objet Corpus pour y stocker sous forme d'instances d'autres objets les articles acquis
        corpus_articles = Corpus(nom_corpus)

        for _, doc in docs.iterrows():
            corpus_articles.add_document(doc['source'],
                                         doc['titre'],
                                         doc['auteur'],
                                         doc['date'],
                                         doc['url'],
                                         doc['texte'],
                                         doc['co_auteurs'],
                                         doc['nombre_commentaires'])
        return corpus_articles

########################################################################################################################

class Corpus:

    def __init__(self, nom):
        self.nom = nom
        self.authors = {}  # Dictionnaire des auteurs
        self.id2doc = {}  # Dictionnaire des documents
        self.ndoc = 0  # Comptage des documents
        self.naut = 0  # Comptage des auteurs

    def add_document(self,source ,titre, auteur, date, url, texte, co_auteurs, nb_commentaires=0):
        # Créer une nouvelle instance de Document

        doc = DocumentFactory.create_document(source ,titre, auteur, date, url, texte, co_auteurs, nb_commentaires)

        # Ajouter le document à id2doc
        self.id2doc[titre] = doc

        # Incrémenter le comptage des documents
        self.ndoc += 1

        # Vérifier si l'auteur existe déjà dans authors
        if auteur not in self.authors:
            # Si l'auteur n'existe pas, créer une nouvelle instance et l'ajouter au dictionnaire
            current_auteur = Author(auteur)
            self.authors[auteur] = current_auteur
            self.naut += 1
        else:
            # Si l'auteur existe déjà, récupérer l'instance existante
            current_auteur = self.authors[auteur]

        # Utiliser la méthode "add" de l'instance pour ajouter le document à sa production
        current_auteur.add(doc)

    def __repr__(self):
        return print(f"Corpus '{self.nom}' contenant {self.ndoc} documents et {self.naut} auteurs.")

    def documents_par_date(self, n):
        # Trier les documents par date puis par titre
        sorted_docs = sorted(self.id2doc.values(), key=lambda x: (x.date), reverse = True)

        # Afficher les n premiers documents triés
        for doc in sorted_docs[:n]:
            print(f"Titre: {doc.titre}, Date: {doc.date}, Auteur: {doc.auteur}")

    def documents_par_titre(self, n):
        # Trier les documents par date puis par titre
        sorted_docs = sorted(self.id2doc.values(), key=lambda x: (x.titre))

        # Afficher les n premiers documents triés
        for doc in sorted_docs[:n]:
            print(f"Titre: {doc.titre}, Date: {doc.date}, Auteur: {doc.auteur}")

    def documents_par_date_et_titre(self, n):
        # Trier les documents par date puis par titre
        sorted_docs = sorted(self.id2doc.values(), key=lambda x: (x.date, x.titre))

        # Afficher les n premiers documents triés
        for doc in sorted_docs[:n]:
            print(f"Titre: {doc.titre}, Date: {doc.date}, Auteur: {doc.auteur}")

    def save(self, filename):
        """
        Sauvegarde l'objet Corpus dans un fichier.

        Args:
            filename (str): Le nom du fichier où sauvegarder l'objet.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename):
        """
        Charge un objet Corpus à partir d'un fichier.

        Args:
            filename (str): Le nom du fichier depuis lequel charger l'objet.

        Returns:
            Corpus: L'objet Corpus chargé.
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
