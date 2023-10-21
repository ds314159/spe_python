from datetime import datetime


class Document:

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        self.url = url
        self.texte = texte
        self.type = self.__class__.__name__

    def afficher_infos(self):
        return print(f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nTexte: {self.texte}")

    def __str__(self):
        return self.titre



class RedditDocument(Document):

    def __init__(self, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires
        self.type = self.__class__.__name__

    def get_nb_commentaires(self):
        return self.nb_commentaires

    def set_nb_commentaires(self, nb_commentaires):
        self.nb_commentaires = nb_commentaires

    def get_type(self):
        return self.type

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Nombre de commentaires: {self.nb_commentaires}")

class ArxivDocument(Document):

    def __init__(self, titre, auteur, date, url, texte, co_auteurs=None):
        super().__init__(titre, auteur, date, url, texte)
        self.co_auteurs = co_auteurs
        self.type = self.__class__.__name__

    def get_co_auteurs(self):
        return self.co_auteurs

    def set_co_auteurs(self, co_auteurs):
        self.co_auteurs = co_auteurs

    def get_type(self):
        return self.type

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Co-auteurs: {self.co_auteurs}" if self.co_auteurs else "Co_auteurs: aucun")


class DocumentFactory:

    @staticmethod
    def create_document(doc_type, *args, **kwargs):
        if doc_type == "Reddit":
            return RedditDocument(*args, **kwargs)
        elif doc_type == "Arxiv":
            return ArxivDocument(*args, **kwargs)
        else:
            raise ValueError(f"Type de document {doc_type} non reconnu")