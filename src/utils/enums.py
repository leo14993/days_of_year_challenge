class MonthDays:
    JANUARY = 31
    FEBRUARY = 28
    LEAP_FEBRUARY = 29
    MARCH = 31
    APRIL = 30
    MAY = 31
    JUNE = 30
    JULY = 31
    AUGUST = 31
    SEPTEMBER = 30
    OCTOBER = 31
    NOVEMBER = 30
    DECEMBER = 31

    @classmethod
    def is_leap_year(cls, year: int = 0) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False



YEAR_MONTHS = list(range(1, 13))


class Year:
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


MONTH_DAYS_ALIAS = {
    Year.JANUARY: MonthDays.JANUARY,
    Year.FEBRUARY: MonthDays.FEBRUARY,
    Year.MARCH: MonthDays.MARCH,
    Year.APRIL: MonthDays.APRIL,
    Year.MAY: MonthDays.MAY,
    Year.JUNE: MonthDays.JUNE,
    Year.JULY: MonthDays.JULY,
    Year.AUGUST: MonthDays.AUGUST,
    Year.SEPTEMBER: MonthDays.SEPTEMBER,
    Year.OCTOBER: MonthDays.OCTOBER,
    Year.NOVEMBER: MonthDays.NOVEMBER,
    Year.DECEMBER: MonthDays.DECEMBER,
}