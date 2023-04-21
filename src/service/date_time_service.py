from datetime import datetime, date
from typing import List, Optional

from src.utils.enums import YEAR_MONTHS, MonthDays, Month, MONTH_DAYS_ALIAS
from src.utils.exceptions import InvalidDataException


class DateService:
    date_format: str = '%Y-%m-%d'
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    leap_year: bool = False

    def get_what_is_the_day_of_year(self, string_date: str) -> int:
        if not self.validate_datetime_string(string_date):
            raise InvalidDataException

        if self.month == Month.JANUARY:
            return self.day

        day = 0
        for month in range(Month.JANUARY, self.month):
            if month == Month.FEBRUARY and self.leap_year:
                day += MonthDays.LEAP_FEBRUARY
                continue

            day += MONTH_DAYS_ALIAS[month]

        day += self.day

        return day

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
        if month == Month.FEBRUARY:
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

        self.year = split_string_date[0]
        self.month = split_string_date[1]
        self.day = split_string_date[2]

        self.leap_year = MonthDays.is_leap_year(self.year)

        if self.month not in YEAR_MONTHS:
            return False

        return self.is_a_valid_day(self.year, self.month, self.day)

