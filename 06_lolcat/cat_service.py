import os
import shutil

import requests


def get_cat(folder, name):
    # print(name)

    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)

    save_cat(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)

    return response.raw


def save_cat(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')

    print('downloading {}'.format(file_name))

    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
