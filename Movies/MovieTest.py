from Movies.Movie import Movie
import unittest

class TestMovies(unittest.TestCase):

    def setUp(self):
        self.movieId = 1
        self.movieRating = 5.4
        self.movieSimilarMovies = []

    def test_movie_implement_the_interface(self):
        movie = Movie(self.movieId, self.movieRating, self.movieSimilarMovies)
        self.assertEqual(self.movieId, movie.getId())
        self.assertEqual(self.movieRating, movie.getRating())
        self.assertEqual(self.movieSimilarMovies, movie.getSimilarMovies())
