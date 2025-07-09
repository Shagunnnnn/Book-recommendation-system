import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load CSVs
books = pd.read_csv("Books.csv", on_bad_lines='skip', low_memory=False)
ratings = pd.read_csv("Ratings.csv")
users = pd.read_csv("Users.csv")

# Merge books and ratings
merged = ratings.merge(books, on='ISBN')

# Filter: Only popular books
book_counts = merged['Book-Title'].value_counts()
popular_books = book_counts[book_counts >= 200].index
filtered = merged[merged['Book-Title'].isin(popular_books)]

# Pivot Table
pt = filtered.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
pt.fillna(0, inplace=True)

# Similarity
similarity_scores = cosine_similarity(pt)

# Save as Pickle
pickle.dump(pt, open('pt.pkl', 'wb'))
pickle.dump(similarity_scores, open('similarity_scores.pkl', 'wb'))
print("✅ create_pickle.py ran successfully.")



