import numpy as np
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class movie_recommend:
  def __init__(self):
    self.movies = pd.read_csv('main_data.csv')
    Tfidf = joblib.load('temp/vector.pkl')
    self.movies['comb'] = self.movies['comb'].fillna('')
    overview_matrix = Tfidf.fit_transform(self.movies['comb'])
    self.similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
    self.mapping = pd.Series(self.movies.index,index = self.movies['movie_title'])
		
  def recommend_movies_based_on_plot(self,movie_input):
   movie_index = self.mapping[movie_input]
   similarity_score = list(enumerate(self.similarity_matrix[movie_index]))
   similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
   similarity_score = similarity_score[1:15]
   movie_indices = [i[0] for i in similarity_score]
   return (self.movies['movie_title'].iloc[movie_indices].values[0:10])