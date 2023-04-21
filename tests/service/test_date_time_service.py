from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock

import inject
import pytest

from src.service.date_time_service import DateService

DATE_TIME_SERVICE_PATH = 'src.service.date_time_service'


@pytest.fixture
def date_time_service() -> DateService:
    offer_service: DateService = inject.instance(DateService)
    return offer_service


@mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_string')
def test_validate_date_time_when_string_is_a_valid_datetime(validate_datetime_string_mock: MagicMock,
                                                            date_time_service: DateService):
    # Arrange
    input_string = '2019-09-14'
    validate_datetime_string_mock.return_value = True
    expected_datetime = datetime.strptime(input_string, date_time_service.date_format).date()

    # Act
    validated_date_time = date_time_service.get_datetime_by_string(input_string)

    # Assert
    assert validated_date_time == expected_datetime
    validate_datetime_string_mock.assert_called_once_with(input_string)

