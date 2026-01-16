import streamlit as st 
st.set_page_config(page_title="GemFinder AI", page_icon="💎", layout="wide")

from recommender import movies,recommend_hidden_gems

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .movie-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
    }
    .genre-tag {
        background-color: #3e3f4b;
        color: #ff4b4b;
        padding: 2px 8px;
        border-radius: 5px;
        margin-right: 5px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Hidden Gem Movie Finder")
st.caption("Discover high-quality movies that everyone else missed.")

if 'num_results' not in st.session_state:
    st.session_state.num_results = 5

# SEARCH 
selected_movie = st.selectbox("Select a movie you love:", movies['title'].values)

if st.button('Find Recommendations'):
    st.session_state.num_results = 5 # Reset when a new search starts
    st.session_state.recommendations = recommend_hidden_gems(selected_movie)

# DISPLAY 
if 'recommendations' in st.session_state:
    results = st.session_state.recommendations
    
    # Show results up to the current count
    for res in results[:st.session_state.num_results]:
        with st.container():
            st.markdown(f"""
                <div class="movie-card">
                    <h3 style='margin-bottom:0;'>{res['title']}</h3>
                    <p style='color: #888;'>⭐ Rating: {res['rating']} | 📈 Pop Score: {res['pop']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Display Genre Tags
            tag_html = ""
            for g in res['genres']:
                tag_html += f'<span class="genre-tag">{g}</span>'
            st.markdown(tag_html, unsafe_allow_html=True)
            st.write("") # Spacer
            st.divider()

    if st.session_state.num_results < len(results):
        if st.button("Load More 🔽"):
            st.session_state.num_results += 5
            st.rerun()