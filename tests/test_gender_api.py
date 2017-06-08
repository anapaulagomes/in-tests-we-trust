from detector.genderapi import GenderDetector
from detector.genderapi import EmptyName
import mock
import pytest
import requests


@mock.patch('detector.genderapi.requests.get')
def test_should_return_female_when_the_first_name_is_from_female(mock_gender_api):
    expected_result = {'name':'Ana', 'gender':'female', 'probability':1, 'count':23}
    mock_gender_api.return_value.ok = True
    mock_gender_api.return_value.json.return_value = expected_result

    detector = GenderDetector()
    result = detector.run('Ana Ferreira')

    mock_gender_api.assert_called_once()
    assert result['gender'] == 'female'


@mock.patch('detector.genderapi.requests.get')
def test_should_return_male_when_the_first_name_is_from_male(mock_gender_api):
    expected_result = {'name':'Mateus', 'gender':'male', 'probability':1, 'count':23}
    mock_gender_api.return_value.ok = True
    mock_gender_api.return_value.json.return_value = expected_result

    detector = GenderDetector()
    result = detector.run('Mateus Costa')

    mock_gender_api.assert_called_once()
    assert result['gender'] == 'male'


@mock.patch('detector.genderapi.requests.get')
def test_should_return_unidentified_when_the_api_can_not_find_the_gender(mock_gender_api):
    expected_result = {'name':'Usineide', 'gender': None}
    mock_gender_api.return_value.ok = True
    mock_gender_api.return_value.json.return_value = expected_result

    detector = GenderDetector()
    result = detector.run('Usineide Ferreira')

    assert result['gender'] == 'unidentified'


@mock.patch('detector.genderapi.requests.get')
def test_should_get_just_first_name(mock_gender_api):
    expected_result = {'name':'Mateus', 'gender':'male', 'probability':1, 'count':23}
    mock_gender_api.return_value.ok = True
    mock_gender_api.return_value.json.return_value = expected_result

    detector = GenderDetector()
    result = detector.run('Mateus Costa')

    assert result['first_name'] == 'Mateus'


def test_should_throw_an_exception_when_the_name_is_none():
    detector = GenderDetector()

    with pytest.raises(EmptyName):
        detector.run(None)


def test_should_throw_an_exception_when_the_name_is_empty():
    detector = GenderDetector()

    with pytest.raises(EmptyName):#Exception eh muito generica!
        detector.run('')
