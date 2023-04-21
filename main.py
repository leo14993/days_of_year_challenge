import inject

from src import DateService

if __name__ == '__main__':
    date_service = inject.instance(DateService)

    date = input("Insert some date (yyyy-mm-dd): ")

    print(date_service.get_what_is_the_day_of_year(date))
