There is a network of similar movies which are attributed by a unique identifier and a rating. Each movie in the network is related to one or more movies in the network through a direct connection.

Design a way to find the N highest rated movies for a given movie in the network of related movies. The original movie should not be considered as a potential recommendation. If the number of requested movies is greater than the total number of movies, then output all the related movies

Input
The input to the function/method consists of two arguments - movie, representing the node of the origianl movie in the movie network and N, an integer representing the number of requested movies.

Output
Return a list containing the nodes of the N highest rated movies.

Constraints
0 <= N

__Note__:

```
        A(7.0)
         /\
        /  \
   B(6.2)  C(6.0)
        \  / 
         \/
       D(6.4)
```
       
Input:
movie = A
N = 10

Output:
B,C,D

Explanation:
Although 10 movies are requested, but only 3 related movies are available. So, the ouput is B, C, D.

Input:
movie = A
N = 2

Output:
B,D

Explanation:
2 movies are requested so the ouput is B,D (the two with highest rank).

Helper Description
The following interface must be defined for a movie object:

```
class Movie:
    def getId(self):
    def getRating(self):
    def getSimilarMovies(self):
```
The following function must resolve the task:
```
# RETURN AN EMPTY LIST IF NO SIMILAR MOVIE TO THE GIVEN MOVIE IS FOUND
def getMovieRecommedation(movie, N):
```

Run the tests:
```
python -m unittest Movies.test_movies
```
