from datetime import datetime


class Document:

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        self.url = url
        self.texte = texte

    def afficher_infos(self):
        return print(
            f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nTexte: {self.texte}")

    def __str__(self):
        return self.titre
