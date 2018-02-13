import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres'
)


def get_movies(search_term):
    if not search_term or not search_term.strip():
        print("nothing")
        raise ValueError('enter search term')

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_term)

    response = requests.get(url)

    movie_data = response.json()
    movie_list = movie_data.get('hits')

    print(type(movie_list), movie_list)

    # non pythonic way
    # movies = []
    # for each_movie in movie_list:
    #     each_movie_tuple = MovieResult(
    #         imdb_code=each_movie.get('imdb_code'),
    #         title=each_movie.get('title'),
    #         duration=each_movie.get('duration'),
    #         director=each_movie.get('director'),
    #         year=each_movie.get('year', 0),
    #         rating=each_movie.get('rating', 0),
    #         imdb_score=each_movie.get('imdb_score', 0),
    #         keywords=each_movie.get('keywords'),
    #         genres=each_movie.get('genres')
    #     )
    #
    #     movies.append(each_movie_tuple)

    # keyword arguments:
    # def keyword_argument(x, y, **kwargs):
    #     print('keyword arguments: ', kwargs)
    #
    # keyword_argument(1, 2, this='becomes', a='dictionary')
    #
    # KwargsTest = collections.namedtuple(
    #     'KwargsTest',
    #     'a, b, c, d, e'
    # )
    #
    # keywords = {
    #     'a': 'A',
    #     'b': 'B',
    #     'c': 'C',
    #     'd': 'D',
    #     'e': 'E'
    # }
    #
    # kwargs_test_result = KwargsTest(**keywords)
    #
    # print(kwargs_test_result) // KwargsTest(a='A', b='B', c='C', d='D', e='E')

    # use keyword arguments for slightly more pythonic way
    # movies = []
    # for each_movie in movie_list:
    #     each_movie_tuple = MovieResult(**each_movie) #
    #
    #     movies.append(each_movie_tuple)

    # use list comprehension for real pythonic way
    movies = [
        MovieResult(**each_movie)
        for each_movie in movie_list
    ]

    movies.sort(key=lambda each_movie: -each_movie.year)

    return movies
