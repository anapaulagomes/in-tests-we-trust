import requests


GENDERIZE_ENDPOINT = 'https://api.genderize.io/?name={}'

class EmptyName(Exception):
    pass


def find_by(name):
    if name == '' or name is None:
        raise EmptyName('The name is empty!')

    first_name = _extract_first_name(name)
    result = _search_on_api(first_name)

    data = {
        'first_name': first_name,
        'gender': result['gender'] if result['gender'] else 'unidentified'
    }
    return data

def _search_on_api(name):
    return requests.get(GENDERIZE_ENDPOINT.format(name)).json()

def _extract_first_name(name):
    return name.split(' ')[0]
