import requests


class EmptyName(Exception):
    pass

class GenderDetector(object):

    def run(self, name):
        if name == '' or name is None:
            raise EmptyName('The name is empty!')

        first_name = self.__extract_first_name(name)
        result = self.__search_on_api(first_name)

        return {'first_name': first_name, 'gender': result['gender'] if result['gender'] else 'unidentified'}

    def __search_on_api(self, name):
        return requests.get('https://api.genderize.io/?name={}'.format(name)).json()

    def __extract_first_name(self, name):
        return name.split(' ')[0]
