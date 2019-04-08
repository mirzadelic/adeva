from dateutil.parser import parse


def format_external_data(data):
    return [
        {
            'name': item['name'],
            'isbn': item['isbn'],
            'authors': item['authors'],
            'number_of_pages': item['numberOfPages'],
            'publisher': item['publisher'],
            'country': item['country'],
            'release_date': parse(item['released']).strftime("%Y-%m-%d"),

        }
        for item in data
    ]

