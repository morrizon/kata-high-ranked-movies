import random
from Movie import Movie

# based in https://github.com/Huertix/katas/blob/518ed54d35c64765fffec104710e7196f5164b5a/python/amazon_movies/main.py#L7
def movies(total_movies, seed):
    random.seed(seed)
    movie_ids = range(1, total_movies+1)
    movie_repository = {}
    for id in movie_ids:
        rating = round(random.uniform(0, 10), 1)
        movie = Movie(id, rating, _similarMovieIds(id, movie_ids), movie_repository)
    return movie_repository.values()

def _similarMovieIds(current_id, candidate_ids):
    total_similar = random.randint(0,5)
    is_not_current_id = lambda id: id!=current_id
    similar_movie_ids = random.sample(candidate_ids, total_similar)
    # remove current and duplicates
    return list(set(filter(is_not_current_id, similar_movie_ids)))
