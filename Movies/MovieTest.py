import unittest
from Movie import Movie,getMovieRecommedation
import Seeder

class TestMovies(unittest.TestCase):

    def setUp(self):
        self.movieRepository = {}

        self.movieId = 1
        self.movieRating = 5.4
        self.movieSimilarMovies = []

        self.movie = Movie(self.movieId, self.movieRating, self.movieSimilarMovies, self.movieRepository)

    def test_movie_implement_the_interface(self):
        self.assertEqual(self.movieId, self.movie.getId())
        self.assertEqual(self.movieRating, self.movie.getRating())
        self.assertEqual(self.movieSimilarMovies, self.movie.getSimilarMovies())

    def test_similar_movies_works(self):
        movie = Movie(2, 3.3, [1], self.movieRepository)
        self.assertEqual([self.movie], movie.getSimilarMovies())

    def test_no_recommendations_when_not_similar_movies(self):
        number_recommendations = 1
        self.assertEqual([], getMovieRecommedation(self.movie, number_recommendations))

    def test_no_recommendations_when_amount_expected_is_zero(self):
        number_recommendations = 0
        movies = Seeder.movies(10, 1)
        self.assertEqual([], getMovieRecommedation(movies[0], number_recommendations))

    # '{"id": 1, "rating": 1.3, "similar_movies": [8, 10, 3, 4, 7]}',
    # '{"id": 2, "rating": 7.9, "similar_movies": []}',
    # '{"id": 3, "rating": 0.3, "similar_movies": [1, 10, 4, 5, 7]}',
    # '{"id": 4, "rating": 2.3, "similar_movies": [1, 10, 6, 9]}',
    # '{"id": 5, "rating": 3.8, "similar_movies": []}',
    # '{"id": 6, "rating": 0.3, "similar_movies": [5]}',
    # '{"id": 7, "rating": 5.0, "similar_movies": [3]}',
    # '{"id": 8, "rating": 2.2, "similar_movies": [1, 3]}',
    # '{"id": 9, "rating": 8.4, "similar_movies": [8, 2, 7]}',
    # '{"id": 10, "rating": 8.6, "similar_movies": []}'
    def test_get_highest_rating_in_recomendations(self):
        movies = Seeder.movies(10, 1)
        recomendations = getMovieRecommedation(movies[0], 1)
        self.assertEqual(1, len(recomendations))
        self.assertEqual(10, recomendations[0].getId())
