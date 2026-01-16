import pandas as pd 
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("tmdb_5000_movies.csv")
movies = df[['id', 'title','overview', 'vote_average', 'vote_count', 'popularity', 'genres']].copy()
df['vote_average'] = movies['vote_average'].fillna(0)

# C is the mean rating across the whole dataset
C = movies['vote_average'].mean()

# m is the minimum votes required.
m = movies['vote_count'].quantile(0.70)
#print(f"Average Rating (C): {C:.2f}")
#print(f"Minimum votes required (m): {m}")

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # The Formula
    return (v/(v+m) * R) + (m/(m+v) * C)

qualified_movies = movies.copy().loc[movies['vote_count'] >= m]
qualified_movies['score'] = qualified_movies.apply(weighted_rating, axis=1)

# Sort movies by score
qualified_movies = qualified_movies.sort_values('score', ascending=False)

# Let's look at the top 10 "High Quality" movies regardless of popularity
#print("Top Rated based on Weighted Score:")
#print(qualified_movies[['title', 'vote_count', 'vote_average', 'score']].head(10))

def convert_json_to_list(obj):
    """
    This function takes a string that looks like a list of dictionaries 
    and returns a clean list of just the 'name' values.
    Example: '[{"name": "Action"}]' -> ['Action']
    """
    L = []
    # We add a try-except block here because sometimes data is messy/empty
    try:
        for i in ast.literal_eval(obj):
            L.append(i['name'])
    except:
        return [] 
    return L

# Apply the function to genres and keywords
movies['genres'] = movies['genres'].apply(convert_json_to_list)

def collapse_spaces(L):
    """
    Removes spaces between words in a list of strings.
    Example: ['Science Fiction', 'Cillian Murphy'] -> ['ScienceFiction', 'CillianMurphy']
    """
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies['genres'] = movies['genres'].apply(collapse_spaces)

# Convert the overview string into a list of words so we can combine it with the other lists
movies['overview'] = movies['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])

# Create the 'tags' column by adding all the lists together
movies['tags'] = movies['overview'] + movies['genres']

# Convert the list of tags back into a single string (sentences)
# Machine Learning models (Vectorizers) prefer one long string per movie.
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

# Make everything lowercase to avoid 'Action' and 'action' being treated differently
movies['tags'] = movies['tags'].apply(lambda x: x.lower())

cv = CountVectorizer(max_features=5000, stop_words="english")
vector = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vector)

def recommend_hidden_gems(movie_title):
    #find the index
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        return "Movie not found. Please check the spelling!"
    #get the similarity scores
    distances = similarity[movie_index]
    #Create a list of (index, similarity_score) and sort it
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:100]
    print(f"Found {len(movie_list)} similar movies. Checking for Gems...") 
    #Filter these 100 similar movies
    recommendations = []
    for i in movie_list:
        idx = i[0]
        movie_data = movies.iloc[idx]

        if movie_data['vote_average'] > 6.0: 
            if movie_data['popularity'] < movies['popularity'].quantile(0.70): 
                recommendations.append({
                    'title': movie_data['title'],
                    'rating': movie_data['vote_average'],
                    'pop': round(movie_data['popularity'], 2),
                    'genres': movie_data['genres']
                })

        if len(recommendations) == 5: 
            break
    return recommendations[:5]            

print("If you liked 'The Dark Knight Rises', check out these Hidden Gems:")
gems = recommend_hidden_gems('The Dark Knight Rises')

# Check if gems is a list (success) or a string (error message)
if isinstance(gems, list):
    for gem in gems:
        print(f"- {gem['title']} (Rating: {gem['rating']} | Popularity Score: {gem['pop']})")
else:
    print(gems)