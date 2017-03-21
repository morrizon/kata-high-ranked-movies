class Movie:

    def __init__(self, id, rating, connections):
        self._id = id
        self._rating = rating
        self._similar_movies = connections

    def getId(self):
        return self._id

    def getRating(self):
        return self._rating

    def getSimilarMovies(self):
        return self._similar_movies

    def __repr__(self):
        return ('{'
                '"id": ' + str(self._id) + ', '
                '"rating": ' + str(self._rating) + ', '
                '"similar_movies": ' + str(self._similar_movies) +
                '}')
                 
def getMovieRecommedation(movie, number):
    return []
