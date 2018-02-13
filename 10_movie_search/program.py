import movie_service
import requests.exceptions


def main():
    print_header()
    search_movies()


def print_header():
    print('---------------------------')
    print('        movie search')
    print('---------------------------')


def search_movies():
    user_input = ''

    while user_input != 'x':
        try:
            user_input = input('search term: ')
            if user_input != 'x':
                search_results = movie_service.get_movies(user_input)

                print('{} movies found for search term: {}'.format(len(search_results), user_input))
                for each_movie in search_results:
                    print("{} -- {}".format(each_movie.year, each_movie.title))

        except ValueError:
            print('search broke')

        except requests.exceptions.ConnectionError:
            print('network broke')

        except Exception as exception:
            print('it broke {}'.format(type(exception)))


if __name__ == '__main__':
    main()
