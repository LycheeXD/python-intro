import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport',
                                       'condition, temperature, scale, location')

test_tuple = 'a', 2, [1, 2, 3]
n0, n1, n2 = test_tuple

print('tuple', test_tuple, 'unpacked tuple', n0, n1, n2)


def main():
    print_header()

    zipcode = input('enter zip code: ')

    html = get_html(zipcode)

    report = get_weather_from_html(html)

    print('it is {}{} and {} at {}'.format(
        report.temperature,
        report.scale,
        report.condition,
        report.location
    ))


def print_header():
    print('------------------------')
    print('         weather')
    print('------------------------')


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather/us/ca/los-angeles/{}'.format(zipcode)

    response = requests.get(url)

    print(response.status_code)

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')

    location = trim_text(soup.find(class_='region-content-header').find('h1').get_text())
    condition = trim_text(soup.find(class_='condition-icon').get_text())
    temperature = trim_text(soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text())
    scale = trim_text(soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text())

    report = WeatherReport(location=location, condition=condition, temperature=temperature, scale=scale)

    # print(location, condition, temperature, scale)

    return report


def trim_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()