from datetime import datetime, date
from typing import List

from src.utils.enums import YEAR_MONTHS, MonthDays, Year, MONTH_DAYS_ALIAS
from src.utils.exceptions import InvalidDataException


class DateService:
    date_format = '%Y-%m-%d'

    def get_datetime_by_string(self, string_date: str) -> date:
        if not self.validate_datetime_string(string_date):
            raise InvalidDataException
        return datetime.strptime(string_date, self.date_format).date()

    def validate_datetime_string(self, string_date: str) -> bool:
        if not isinstance(string_date, str):
            return False
        return self.validate_datetime_values(string_date)

    def datetime_string_has_all_params(self, split_string_date: List[str]) -> bool:
        return len(split_string_date) == len(self.date_format.split('-'))

    def verify_date_params_type(self, split_string_date: List[str]) -> bool:
        """This funcion verify if each one of date is numeric"""
        return all(list(map(lambda i: i.isnumeric(), split_string_date)))

    def is_a_valid_day(self, year: int, month: int, day: int) -> bool:
        if month == Year.FEBRUARY:
            if MonthDays.is_leap_year(year):
                return day <= MonthDays.LEAP_FEBRUARY
            return day <= MonthDays.FEBRUARY
        return day <= MONTH_DAYS_ALIAS[month]

    def validate_datetime_values(self, string_date: str) -> bool:
        split_string_date = string_date.split('-')

        if not self.datetime_string_has_all_params(split_string_date):
            return False

        if not self.verify_date_params_type(split_string_date):
            return False

        split_string_date = [int(x) for x in split_string_date]

        year = split_string_date[0]
        month = split_string_date[1]
        day = split_string_date[2]

        if month not in YEAR_MONTHS:
            return False

        if not self.is_a_valid_day(year, month, day):
            return False

        return True
