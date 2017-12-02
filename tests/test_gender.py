from detector import gender
from detector.gender import EmptyName
from unittest import mock
import pytest


@pytest.fixture
def mock_requests(mocker):
    return mocker.patch('detector.gender.requests.get')


@mock.patch('detector.gender.requests.get')
def test_should_return_female_when_the_first_name_is_from_female_with_mocks(mock_requests):
    expected_result = {
        'name':'Ana',
        'gender':'female',
        'probability':1,
        'count':23
    }
    mock_requests.return_value.json.return_value = expected_result

    result = gender.find_by('Ana Ferreira')

    mock_requests.assert_called_once()
    assert result['gender'] == 'female'


def test_should_return_male_when_the_first_name_is_from_male_with_mocks(mock_requests):
    expected_result = {
        'name':'Mateus',
        'gender':'male',
        'probability':1,
        'count':23
    }
    mock_requests.return_value.json.return_value = expected_result

    result = gender.find_by('Mateus Costa')

    mock_requests.assert_called_once()
    assert result['gender'] == 'male'


def test_should_return_unidentified_when_the_api_can_not_find_the_gender(mock_requests):
    expected_result = {'name':'Usineide', 'gender': None}
    mock_requests.return_value.json.return_value = expected_result

    result = gender.find_by('Usineide Ferreira')

    assert result['gender'] == 'unidentified'


def test_should_get_just_first_name(mock_requests):
    expected_result = {'name':'Mateus', 'gender':'male', 'probability':1, 'count':23}
    mock_requests.return_value.json.return_value = expected_result

    result = gender.find_by('Mateus Costa')

    assert result['first_name'] == 'Mateus'


def test_should_throw_an_exception_when_the_name_is_none():
    with pytest.raises(EmptyName):
        gender.find_by(None)


def test_should_throw_an_exception_when_the_name_is_empty():
    with pytest.raises(EmptyName):  # apenas Exception eh generico demais!
        gender.find_by('')


@pytest.mark.skip
def test_should_return_female_when_the_first_name_is_from_female_without_mocks():
    expected_result = {
        'name':'Ana',
        'gender':'female',
        'probability':1,
        'count':23
    }
    result = gender.find_by('Ana Ferreira')

    assert result['gender'] == 'female'


@pytest.mark.skip
def test_should_return_male_when_the_first_name_is_from_male_without_mocks():
    expected_result = {
        'name':'Mateus',
        'gender':'male',
        'probability':1,
        'count':23
    }
    result = gender.find_by('Mateus Costa')

    assert result['gender'] == 'male'
