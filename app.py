import streamlit as st
import random

# Page config
st.set_page_config(page_title="Movie Recommendation", page_icon="🎬", layout="centered")

# Title
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Find movies by genre, search them, or get a random suggestion!</h4>", unsafe_allow_html=True)

# Movie database
movies = {
    "🔥 Action": [
        {
            "name": "John Wick",
            "rating": "⭐ 8.0",
            "desc": "An action-packed revenge story of a legendary hitman.",
            "image": "https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg"
        },
        {
            "name": "Mad Max: Fury Road",
            "rating": "⭐ 8.1",
            "desc": "A high-speed post-apocalyptic desert chase.",
            "image": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"
        },
        {
            "name": "The Dark Knight",
            "rating": "⭐ 9.0",
            "desc": "Batman faces the Joker in Gotham City.",
            "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
        }
    ],

    "😂 Comedy": [
        {
            "name": "The Mask",
            "rating": "⭐ 6.9",
            "desc": "A shy banker gains magical powers from a mysterious mask.",
            "image": "https://image.tmdb.org/t/p/w500/uc9qG7q9lL5mRrE2h2c6v2X7R3E.jpg"
        },
        {
            "name": "Superbad",
            "rating": "⭐ 7.6",
            "desc": "Two friends try to enjoy their last days of high school.",
            "image": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg"
        },
        {
            "name": "Home Alone",
            "rating": "⭐ 7.7",
            "desc": "A boy defends his home from burglars during Christmas.",
            "image": "https://image.tmdb.org/t/p/w500/9wSbe4CwObACCQvaUVhWQyLR5Vz.jpg"
        }
    ],

    "🚀 Sci-Fi": [
        {
            "name": "Interstellar",
            "rating": "⭐ 8.6",
            "desc": "A space mission to save humanity.",
            "image": "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg"
        },
        {
            "name": "Inception",
            "rating": "⭐ 8.8",
            "desc": "A thief steals secrets through dreams.",
            "image": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"
        },
        {
            "name": "The Matrix",
            "rating": "⭐ 8.7",
            "desc": "Reality is not what it seems.",
            "image": "https://image.tmdb.org/t/p/w500/aOIuZAjPaRIE6CMzbazvcHuHXDc.jpg"
        }
    ],

    "👻 Horror": [
        {
            "name": "The Conjuring",
            "rating": "⭐ 7.5",
            "desc": "A terrifying paranormal investigation.",
            "image": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg"
        },
        {
            "name": "It",
            "rating": "⭐ 7.3",
            "desc": "A terrifying clown haunts children.",
            "image": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg"
        },
        {
            "name": "A Quiet Place",
            "rating": "⭐ 7.5",
            "desc": "A family must live in silence to survive monsters.",
            "image": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg"
        }
    ]
}

# Sidebar menu
menu = st.sidebar.selectbox(
    "📂 Select Option",
    ["🎭 Recommend by Genre", "🔎 Search Movie", "🎲 Random Movie"]
)

# ---------------- GENRE ----------------

if menu == "🎭 Recommend by Genre":

    genre = st.selectbox("🎬 Select Genre", list(movies.keys()))

    if st.button("🍿 Show Movies"):

        st.success("Here are your movie recommendations!")

        for movie in movies[genre]:

            col1, col2 = st.columns([1,3])

            with col1:
                st.image(movie["image"], width=150)

            with col2:
                st.markdown(f"### 🎬 {movie['name']}")
                st.write(movie["rating"])
                st.write(movie["desc"])
                st.write("---")

# ---------------- SEARCH ----------------

elif menu == "🔎 Search Movie":

    search = st.text_input("🔍 Enter movie name")

    if search:

        found = False

        for genre in movies:
            for movie in movies[genre]:

                if search.lower() in movie["name"].lower():

                    st.success("✅ Movie Found!")

                    st.markdown(f"### 🎬 {movie['name']}")
                    st.image(movie["image"], width=220)
                    st.write(movie["rating"])
                    st.write(movie["desc"])

                    found = True

        if not found:
            st.error("❌ Movie not found")

# ---------------- RANDOM ----------------

elif menu == "🎲 Random Movie":

    if st.button("🎁 Suggest a Movie"):

        genre = random.choice(list(movies.keys()))
        movie = random.choice(movies[genre])

        st.markdown("## 🎉 Your Random Movie Pick")

        st.info(f"🎭 Genre: {genre}")

        st.markdown(f"### 🎬 {movie['name']}")
        st.image(movie["image"], width=220)
        st.write(movie["rating"])
        st.write(movie["desc"])