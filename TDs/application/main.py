# import des librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import praw
import json
import xmltodict
import urllib3 as urllib
import urllib.request as libreq
import datetime

# *********************************************************************************************************************
# ********************************** Explorer REDDIT ******************************************************************
# *********************************************************************************************************************
print("***************************** Explorer REDDIT *****************************************************************")

with open('config.json', 'r') as file:
    config = json.load(file)

reddit_client_id = config['REDDIT']['client_id']

reddit_client_secret = config['REDDIT']['client_secret']

reddit_user_agent = config['REDDIT']['user_agent']

with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()

# instance reddit
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

print("*********************** Explorer les subreddits  *************************************************************")
# instance de subreddit (exploration de ce qui existe)
subreddit = reddit.subreddit("covid19")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in new_posts:
    print('TITLE : \n', post.title)
    print('ID : \n', post.id)
    print('AUTHOR : \n', post.author)
    print('URL : \n', post.url)
    print('SCORE : \n', post.score)  # votes positifs mins votes negatifs
    print('COMMENTS COUNT : \n', post.num_comments)
    print('CREATED : \n', datetime.datetime.utcfromtimestamp(post.created_utc))  # convertir en format lisible
    print('\n')

# exploration par identifiant unique
print("*********************** Explorer un poste à identifiant unique ************************************************")

post_cible = reddit.submission(id='16ufp83')
commentaires = post_cible.comments
for commentaire in commentaires[:5]:
    print('Commantaire : \n')
    print('texte : \n', commentaire.body)
    print('auteur : \n', commentaire.author)
    print('\n')

# ***********************************************************************************************************************
# ********************************** Explorer ARXIV *********************************************************************
# ***********************************************************************************************************************

print("***************************************************************************************************************")

import urllib.request as libreq

cible = 'all'
contenu = 'covid19'
cible_exclusion = 'ti'
contenu_exclusion = 'raoult'
volume = 10
requete_arxiv = f"http://export.arxiv.org/api/query?search_query={cible}:{contenu}+ANDNOT+%28{cible_exclusion}:{contenu_exclusion}%29&start=0&max_results={volume}"

with libreq.urlopen(requete_arxiv) as url:
    r = url.read()

parsed = xmltodict.parse(r)

articles = parsed['feed']['entry']

for article in articles:
    title = article['title']
    summary = article['summary']
    print("Title:", title)
    print("Summary:", summary)
    print("--------")
