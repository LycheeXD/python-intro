import os
import subprocess

import cat_service


def main():
    print_header()
    cat_folder = get_or_create_output_folder()

    print('found or created cat folder: {}'.format(cat_folder))

    download_cats(cat_folder)

    display_cats(cat_folder)


def print_header():
    print('-------------------------')
    print('          lolcat')
    print('-------------------------')


def get_or_create_output_folder():
    folder = 'cat_pictures'

    base_folder = os.path.dirname(__file__)

    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('new cat folder {}'.format(full_path))

        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('contacting cat server...')
    cat_count = 8

    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    subprocess.call(['open', folder])


if __name__ == '__main__':
    main()
