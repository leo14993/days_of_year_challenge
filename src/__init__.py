#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0'

import inject

from src.service.date_time_service import DateService


def configure_date_service(binder):
    binder.bind(DateService, DateService())


def configure(binder):
    configure_date_service(binder)


inject.configure_once(configure)
