#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.1.0'

import inject

from src.service.date_time_service import DateService
from src.use_case.day_of_year_use_case import DayOfYear


def configure_date_service(binder):
    binder.bind(DateService, DateService())


def configure_date_use_case(binder):
    binder.bind(DayOfYear, DayOfYear())


def configure(binder):
    configure_date_service(binder)
    configure_date_use_case(binder)


inject.configure_once(configure)
