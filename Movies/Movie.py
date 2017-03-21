class Movie:

    def __init__(self, id, rating, similar_movie_ids, movie_repository):
        if id in movie_repository:
            raise Exception('Cannot create movie witd id ' + id + ' if exists in repository')
        movie_repository[id] = self

        self._id = id
        self._rating = rating
        self._similar_movie_ids = similar_movie_ids
        self._movie_repository = movie_repository

    def getId(self):
        return self._id

    def getRating(self):
        return self._rating

    def getSimilarMovies(self):
        return map(lambda id: self._movie_repository[id], self._similar_movie_ids)

    def __repr__(self):
        return ('{'
                '"id": ' + str(self._id) + ', '
                '"rating": ' + str(self._rating) + ', '
                '"similar_movies": ' + str(self._similar_movie_ids) +
                '}')
                 
def getMovieRecommedation(movie, number):
    return []
