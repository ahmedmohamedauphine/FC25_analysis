import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob

# Charger les données
@st.cache_data
def load_data():
    return pd.read_csv("reviews_with_sentiments.csv")

df = load_data()

# Titre de l'application
st.title("Analyse des Avis sur FC 25")
st.markdown("### Explorez les retours des joueurs et identifiez les points forts et les améliorations possibles du jeu FC 25.")

# Section : Statistiques générales
st.header("Statistiques générales")
st.markdown(
    """
    Cette section présente des statistiques globales sur les avis recueillis, 
    comme le nombre total d'avis, la répartition des sentiments, et la note moyenne.
    """
)
st.write(f"**Nombre total d'avis :** {len(df)}")

positive_count = (df['label_textblob'] == 'positif').sum()
negative_count = (df['label_textblob'] == 'négatif').sum()
neutral_count = (df['label_textblob'] == 'neutre').sum()
st.write(f"**Avis positifs :** {positive_count}")
st.write(f"**Avis négatifs :** {negative_count}")
st.write(f"**Avis neutres :** {neutral_count}")
st.write(f"**Plateformes analysées :** {df['platform'].nunique()}")
st.write(f"**Note moyenne :** {df['note'].mean():.2f}")

# Distribution des sentiments
st.subheader("Distribution des sentiments")
st.markdown(
    """
    L'analyse des sentiments permet de catégoriser les avis des joueurs en trois classes :
    - **Positif** : Avis favorables exprimant de la satisfaction.
    - **Neutre** : Avis intermédiaires sans jugement clair.
    - **Négatif** : Avis défavorables indiquant des points de déception.
    """
)
sentiment_counts = df['label_textblob'].value_counts()
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color=['green', 'gray', 'red'], ax=ax)
ax.set_title("Distribution des sentiments")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Nombre d'avis")
st.pyplot(fig)

# Section : Nuages de mots
st.header("Nuages de mots")
st.markdown(
    """
    Les nuages de mots mettent en évidence les termes les plus fréquents dans les avis en fonction des sentiments.
    Cela permet d'identifier rapidement les points qui ressortent dans les avis positifs, neutres et négatifs.
    """
)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

for sentiment in ['positif', 'neutre', 'négatif']:
    st.subheader(f"Nuage de mots pour les avis {sentiment}s")
    text = " ".join(df[df['label_textblob'] == sentiment]['review_cleaned'])
    if text.strip():
        wordcloud = generate_wordcloud(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.write(f"Pas assez de données pour générer un nuage de mots pour les avis {sentiment}s.")

# Section : Analyse des thèmes
st.header("Analyse des thèmes")
st.markdown(
    """
    Les thèmes représentent des regroupements d'avis basés sur des mots-clés similaires, identifiés via un modèle de type Topic Modeling. 
    Cette analyse aide à comprendre les grandes tendances des discussions autour de FC 25 et à identifier les sujets les plus débattus.
    """
)

st.subheader("Distribution des thèmes")
fig, ax = plt.subplots()
df['topic'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Distribution des thèmes")
ax.set_xlabel("Thème")
ax.set_ylabel("Nombre d'avis")
st.pyplot(fig)

st.subheader("Nuages de mots par thème")
for topic in sorted(df['topic'].unique()):
    st.write(f"### Thème {topic}")
    topic_text = " ".join(df[df['topic'] == topic]['review_cleaned'])
    if topic_text.strip():
        wordcloud = generate_wordcloud(topic_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.write(f"Pas assez de données pour générer un nuage de mots pour le thème {topic}.")

# Section : Prédiction de sentiment
st.header("Prédiction du sentiment d’un nouvel avis")
st.markdown(
    """
    Vous pouvez tester cette fonctionnalité en entrant un avis personnalisé sur FC 25.
    L'application analysera le sentiment global de cet avis pour déterminer s'il est **positif**, **neutre** ou **négatif**.
    """
)

# Exemple d'avis pour guider l'utilisateur
st.write("### Vous pouvez tester avec : Le gameplay est Horrible / Moyen / Cool.")
st.write("Les sentiments sont classés comme suit : **Positif**, **Neutre**, ou **Négatif**, selon la polarité calculée.")

# Zone de texte pour l'avis utilisateur
user_input = st.text_area("Saisissez un avis pour FC 25 :", "")
if st.button("Analyser l'avis"):
    if user_input.strip():
        # Analyse du sentiment avec TextBlob
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            sentiment = "Positif"
        elif polarity < -0.1:
            sentiment = "Négatif"
        else:
            sentiment = "Neutre"
        
        st.subheader(f"Le sentiment de l'avis est : {sentiment}")
    else:
        st.warning("Veuillez saisir un avis valide.")

# Section : Réponse à la problématique
st.header("Conclusion de l'analyse")
st.markdown(
    """
    ### Quels aspects de FC 25 plaisent ou déçoivent le plus les joueurs ?
    L'analyse des thèmes et des sentiments montre que plusieurs aspects du jeu FC 25 génèrent des retours variés :
    - **Points positifs** : Les éléments appréciés incluent souvent des améliorations perçues dans le gameplay ou certaines fonctionnalités spécifiques.
    - **Points négatifs** : Les critiques concernent principalement les bugs, les performances du jeu, ainsi que des attentes non satisfaites sur certains modes.
    
    ### Comment visualiser ces retours de manière claire et exploitable ?
    Grâce à l'utilisation de statistiques descriptives, d'analyses de sentiment et de thèmes, les retours sont présentés sous forme de graphiques interactifs, de nuages de mots et de résumés clairs. Ces outils permettent de mieux comprendre les attentes des joueurs et d'orienter les améliorations futures du jeu.
    
    Réalisée par **Romain LEPRETRE** & **Ahmed MOHAMED**
    """
)
