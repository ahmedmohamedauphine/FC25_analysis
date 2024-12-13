Analyse des Avis sur FC 25

Description du Projet

Ce projet vise à analyser les avis des joueurs sur le jeu FC 25 à l’aide de techniques de web scraping, de nettoyage de données, d’analyse de sentiments et de modélisation thématique. Les résultats sont présentés dans une application Streamlit interactive pour permettre une exploration claire et exploitable des retours des joueurs.

Structure des Fichiers

1. Code Principal

app.py : Contient le code de l’application Streamlit.

web_scraping_analysis.py : Inclut les fonctions de web scraping, de nettoyage, et d’analyse des données. Ce script est exécuté pour générer les fichiers CSV utilisés par l'application.

2. Fichiers de Données

all_reviews.csv : Fichier consolidé contenant tous les avis bruts collectés pour PS5, PC, et XBOX.

final_reviews_cleaned.csv : Fichier contenant les données nettoyées et préparées pour analyse.

reviews_with_sentiments.csv : Fichier final contenant les données enrichies avec les analyses de sentiments et les modèles thématiques.

3. Ressources

README.md : Document explicatif (ce fichier).

requirements.txt : Liste des dépendances nécessaires pour exécuter le projet.

Packages Utilisés

requests : Récupération des pages web via HTTP.

BeautifulSoup : Extraction et parsing des éléments HTML.

pandas : Manipulation et analyse de données tabulaires.

nltk : Nettoyage de texte, gestion des stop words, et analyse de sentiments.

TextBlob : Analyse de sentiments basée sur les polarités.

VADER (nltk.sentiment) : Analyse de sentiments adaptée aux textes informels.

matplotlib et seaborn : Visualisation des données.

wordcloud : Génération de nuages de mots.

scikit-learn : Modélisation thématique (Latent Dirichlet Allocation).

Accès à l'Application Streamlit

Prérequis

Git : Installer Git pour cloner le dépôt.

Python 3.8+ : Installer Python et pip.

Streamlit : Installer Streamlit avec pip install streamlit.

Procédure d’accès à l’application

Cloner le dépôt Git :

git clone <URL_du_depot_Git>
cd <nom_du_depot>

Installer les dépendances :

pip install -r requirements.txt

Lancer l'application Streamlit :

streamlit run app.py

Accès dans le navigateur : Ouvrir http://localhost:8501.

Accès à l’application déployée

URL publique : https://streamlit-fc25-analysis.streamlit.app

Authentification :

Identifiant : utilisateur_demo

Mot de passe : fc25_analysis

Instructions pour l’exécution locale

Exécuter le web scraping :
Lancer le script web_scraping_analysis.py pour collecter les avis et préparer les fichiers CSV.

python web_scraping_analysis.py

Lancer l'application Streamlit :
Une fois les fichiers CSV générés, utilisez la commande suivante pour démarrer l'application :

streamlit run app.py

Explorer les résultats :
Ouvrir l’URL http://localhost:8501 pour accéder à l’interface utilisateur.

Fonctionnalités Clés

Statistiques descriptives : Nombre d’avis, répartition des sentiments, et distribution des plateformes.

Analyse de sentiments : Identifie les avis positifs, neutres, et négatifs.

Modélisation thématique : Extraction de thèmes principaux à partir des avis.

Visualisations : Nuages de mots, graphiques interactifs pour l’analyse des données.

Prédiction de sentiment : Analyse du sentiment d’un avis personnalisé saisie par l'utilisateur.

Auteur : Romain LEPRETRE & Ahmed MOHAMED
