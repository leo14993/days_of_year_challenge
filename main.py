import inject

from src.use_case.day_of_year_use_case import DayOfYear

if __name__ == '__main__':
    day_of_year = inject.instance(DayOfYear)
    input("Your name: ")
