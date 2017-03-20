#!/usr/bin/python

class Movie:

    def __init__(self, id, rating, connections):
        self.id = id
        self.rating = rating
        self.connections = connections

    def getId(self):
        return self.id

    def getRating(self):
        return self.rating

    def getSimilarMovies(self):
        return self.connections
