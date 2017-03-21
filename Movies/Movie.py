class Movie:

    def __init__(self, id, rating, connections):
        self._id = id
        self._rating = rating
        self._connections = connections

    def getId(self):
        return self._id

    def getRating(self):
        return self._rating

    def getSimilarMovies(self):
        return self._connections
