import unittest
import Seeder

class TestMovies(unittest.TestCase):

    def setUp(self):
        self.seed = 1
        self.total_movies = 10

    def test_seeding(self):
        movies = Seeder.movies(self.total_movies, self.seed)
        expected_movies = [
            '{"id": 1, "rating": 1.3, "similar_movies": [8, 10, 3, 4, 7]}',
            '{"id": 2, "rating": 7.9, "similar_movies": []}',
            '{"id": 3, "rating": 0.3, "similar_movies": [1, 10, 4, 5, 7]}',
            '{"id": 4, "rating": 2.3, "similar_movies": [1, 10, 6, 9]}',
            '{"id": 5, "rating": 3.8, "similar_movies": []}',
            '{"id": 6, "rating": 0.3, "similar_movies": [5]}',
            '{"id": 7, "rating": 5.0, "similar_movies": [3]}',
            '{"id": 8, "rating": 2.2, "similar_movies": [1, 3]}',
            '{"id": 9, "rating": 8.4, "similar_movies": [8, 2, 7]}',
            '{"id": 10, "rating": 8.6, "similar_movies": []}'
        ]
        self.assertEquals(expected_movies, map(lambda m: str(m), movies))
        self.assertEquals(1, movies[0].getId())
        self.assertEquals(1.3, movies[0].getRating())
        self.assertEquals(5, len(movies[0].getSimilarMovies()))
        self.assertEquals(8, movies[0].getSimilarMovies()[0].getId())
