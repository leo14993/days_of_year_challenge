import inject

from src.service.date_time_service import DateService


class DayOfYear:

    date_transformer = inject.attr(DateService)

    def get_day_of_year(self, string_date: str):

        date = self.date_transformer.get_datetime_by_string(string_date)
