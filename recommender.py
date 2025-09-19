import pandas as pd

# Load ratings and movies
ratings = pd.read_csv("ml-latest-small/ratings.csv")
movies = pd.read_csv("ml-latest-small/movies.csv")

print("Ratings sample:")
print(ratings.head())

print("\nMovies sample:")
print(movies.head())

# Merge ratings with movie titles
data = ratings.merge(movies, on="movieId")
print("\nMerged dataset:")
print(data.head())
