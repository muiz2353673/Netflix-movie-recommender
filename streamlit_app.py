import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df.dropna(subset=['title', 'type', 'director', 'cast', 'description'], inplace=True)
    df['combined'] = df['type'] + ' ' + df['director'] + ' ' + df['cast'] + ' ' + df['description'] + ' ' + df['listed_in']
    df['combined'] = df['combined'].str.lower()
    return df

df = load_data()

# Vectorize and compute similarity
@st.cache_resource
def create_similarity(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df.index, index=df['title'].str.lower())
    return cosine_sim, indices

cosine_sim, indices = create_similarity(df)

# Recommendation function
def recommend(title, cosine_sim, indices, df):
    title = title.lower()
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# Streamlit UI
st.title("🎬 Netflix Movie Recommendation System")
st.write("Enter a movie title and get recommendations based on similar content.")

movie_input = st.text_input("Enter a movie title:")

if movie_input:
    recommendations = recommend(movie_input, cosine_sim, indices, df)
    if recommendations:
        st.subheader("You might also like:")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
    else:
        st.warning("Movie not found in the database.")
