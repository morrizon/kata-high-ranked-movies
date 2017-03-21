import unittest
from Movie import Movie,getMovieRecommedation

class TestMovies(unittest.TestCase):

    def setUp(self):
        self.movieId = 1
        self.movieRating = 5.4
        self.movieSimilarMovies = []
        self.movie = Movie(self.movieId, self.movieRating, self.movieSimilarMovies)

    def test_movie_implement_the_interface(self):
        self.assertEqual(self.movieId, self.movie.getId())
        self.assertEqual(self.movieRating, self.movie.getRating())
        self.assertEqual(self.movieSimilarMovies, self.movie.getSimilarMovies())

    def test_no_recommendations_when_not_similar_movies(self):
        number_recommendations = 1
        self.assertEqual([], getMovieRecommedation(self.movie, number_recommendations))
