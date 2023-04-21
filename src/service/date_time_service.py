from datetime import datetime, date
from typing import List

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


    def validate_datetime_values(self, string_date: str) -> bool:
        split_string_date = string_date.split('-')

        if not self.datetime_string_has_all_params(split_string_date):
            return False

        return True


    def datetime_string_has_all_params(self, split_string_date: List[str]) -> bool:
        return len(split_string_date) == len(self.date_format.split('-'))
