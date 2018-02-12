import csv
import os
import statistics

import property


def main():
    print_header()
    filename = get_data()
    print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('----------------------------')
    print('         real estate')
    print('----------------------------')


def get_data():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        property_list = []
        fin_reader = csv.DictReader(fin)

        for each_row in fin_reader:
            each_property = property.Property.create_property(each_row)
            property_list.append(each_property)
        print(property_list[0].__dict__)

    return property_list


# def get_each_property_price(property):
#     return property.price


def query_data(data):
    # data.sort(key=get_each_property_price)
    data.sort(key=lambda property: property.price)

    property_price_list = [
        each_property.price
        for each_property in data
    ]

    print('price list: ', property_price_list)

    averave_price = int(statistics.mean(property_price_list))

    print('average price: ${:,}'.format(averave_price))

    most_expensive_property = data[-1]

    least_expensive_property = data[0]

    print('most expensive: ${:,}'.format(most_expensive_property.price))
    print('least expensive: ${:,}'.format(least_expensive_property.price))

    two_bed_property_list = [
        each_property
        for each_property in data
        if each_property.beds == 2
    ]

    print('average for 2 beds: ${:,}, {}sqft'
          .format(int(statistics.mean([each_property.price for each_property in two_bed_property_list])),
                  round(statistics.mean([each_property.sq__ft for each_property in two_bed_property_list]))
                  )
          )

    two_baths_property_list = (
        each_property
        for each_property in data
        if each_property.baths == 2
    )

    first_5_two_baths = []

    for each_two_baths in two_baths_property_list:
        if len(first_5_two_baths) < 5:
            first_5_two_baths.append(each_two_baths)

    print('average for 2 baths: ${:,}, {}sqft'
          .format(int(statistics.mean((each_property.price for each_property in first_5_two_baths))),
                  round(statistics.mean((each_property.sq__ft for each_property in first_5_two_baths)))
                  )
          )


if __name__ == '__main__':
    main()
