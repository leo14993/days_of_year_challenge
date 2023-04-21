import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock

import inject

from src.service.date_time_service import DateService
from src.utils.exceptions import InvalidDataException

DATE_TIME_SERVICE_PATH = 'src.service.date_time_service'


class TestDateTimeService(unittest.IsolatedAsyncioTestCase):
    date_time_service: DateService = inject.instance(DateService)

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_string')
    def test_validate_date_time_when_string_is_a_valid_datetime_then_return_converted_datetime(self,
                                                                                               validate_datetime_string_mock: MagicMock):
        # Arrange
        input_string = '2019-09-14'
        validate_datetime_string_mock.return_value = True
        expected_datetime = datetime.strptime(input_string, self.date_time_service.date_format).date()

        # Act
        validated_date_time = self.date_time_service.get_datetime_by_string(input_string)

        # Assert
        assert validated_date_time == expected_datetime
        validate_datetime_string_mock.assert_called_once_with(input_string)

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_string')
    def test_validate_date_time_when_string_is_not_valid_datetime_then_raise_invalid_data_exception(self,
                                                                                                    validate_datetime_string_mock: MagicMock):
        # Arrange
        input_string = '2019-09-14'
        validate_datetime_string_mock.return_value = False

        # Act/Assert
        with self.assertRaises(InvalidDataException):
            self.date_time_service.get_datetime_by_string(input_string)

        validate_datetime_string_mock.assert_called_once_with(input_string)

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_values')
    def test_validate_datetime_string_when_is_string_and_datetime_values_is_valid_then_returns_true(self,
                                                                                                    validate_datetime_values_mock: MagicMock):

        # Arrange
        input_string = '2019-09-14'
        validate_datetime_values_mock.return_value = True

        # Act / Assert
        self.assertTrue(self.date_time_service.validate_datetime_string(input_string))
        validate_datetime_values_mock.assert_called_once_with(input_string)


    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_values')
    def test_validate_datetime_string_when_is_input_value_is_not_string_then_returns_false(self,
                                                                                                validate_datetime_values_mock: MagicMock):

        # Arrange
        input_string = 1234
        validate_datetime_values_mock.return_value = True

        # Act / Assert
        self.assertFalse(self.date_time_service.validate_datetime_string(input_string))
        validate_datetime_values_mock.assert_not_called()

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.validate_datetime_values')
    def test_validate_datetime_string_when_is_input_value_is_string_but_is_not_valid_then_returns_false(self,
                                                                                           validate_datetime_values_mock: MagicMock):
        # Arrange
        input_string = '2019-09-44'
        validate_datetime_values_mock.return_value = False

        # Act / Assert
        self.assertFalse(self.date_time_service.validate_datetime_string(input_string))
        validate_datetime_values_mock.assert_called_once_with(input_string)


    def test_datetime_string_has_all_params_when_splitted_string_has_all_params_then_return_true(self):

        # Arrange
        input_string = '2019-09-14'
        split_input_string = input_string.split('-')

        # Act / Assert
        self.assertTrue(self.date_time_service.datetime_string_has_all_params(split_input_string))


    def test_datetime_string_has_all_params_when_splitted_string_has_not_all_params_then_return_false(self):

        # Arrange
        input_string = '2019-09'
        split_input_string = input_string.split('-')

        # Act / Assert
        self.assertFalse(self.date_time_service.datetime_string_has_all_params(split_input_string))



    def test_verify_date_params_type_when_all_params_is_numeric_then_returns_true(self):
        # Arrange
        input_string = '2019-09-14'
        split_input_string = input_string.split('-')

        #Act / Assert
        self.assertTrue(self.date_time_service.verify_date_params_type(split_input_string))

    def test_verify_date_params_type_when_one_of_params_is_not_numeric_then_returns_false(self):
        # Arrange
        input_string = '2019-setembro-14'
        split_input_string = input_string.split('-')

        # Act / Assert
        self.assertFalse(self.date_time_service.verify_date_params_type(split_input_string))


    def test_is_a_valid_day_when_is_valid_then_returns_true(self):
        # Arrange

        dates = [
            (2019, 9, 14),
            (2019, 2, 28),
            (2020, 2, 29),
            (0, 2, 29),
            (5001, 8, 31),
            (5001, 7, 31),
        ]

        # Act / Assert
        for date in dates:
            self.assertTrue(self.date_time_service.is_a_valid_day(date[0], date[1], date[2]))

    def test_is_not_a_valid_day_when_is_valid_then_returns_false(self):
        # Arrange
        dates = [
            (2019, 9, 45),
            (2019, 2, 29),
            (2020, 2, 30),
            (0, 2, 31),
            (1500, 1, 32),
            (1500, 12, 32),
            (5001, 6, 31),
        ]

        # Act / Assert
        for date in dates:
            self.assertFalse(self.date_time_service.is_a_valid_day(date[0], date[1], date[2]))

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.datetime_string_has_all_params')
    def test_validate_datetime_values_when_string_have_not_all_date_params_then_returns_false(self,
                                                                                              datetime_string_has_all_params_mock: MagicMock):
        # Arrange
        input_string = '2019-09'
        split_input_string = input_string.split('-')
        datetime_string_has_all_params_mock.return_value = False

        # Act / Assert
        self.assertFalse(self.date_time_service.validate_datetime_values(input_string))
        datetime_string_has_all_params_mock.assert_called_once_with(split_input_string)

    @mock.patch(f'{DATE_TIME_SERVICE_PATH}.DateService.datetime_string_has_all_params')
    def test_validate_datetime_values_when_string_have_all_date_params_then_returns_true(self,
                                                                                              datetime_string_has_all_params_mock: MagicMock):
        # Arrange
        input_string = '2019-09-14'
        split_input_string = input_string.split('-')
        datetime_string_has_all_params_mock.return_value = True

        # Act / Assert
        self.assertTrue(self.date_time_service.validate_datetime_values(input_string))
        datetime_string_has_all_params_mock.assert_called_once_with(split_input_string)

