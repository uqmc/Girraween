#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Basic setup for root logger
"""

import logging

from config import Config

config = Config()


def setup():
    log_level = config.get_log_level().upper()

    logging.basicConfig(
        format='%(asctime)s: %(levelname)s: %(message)s',
        level=log_level
    )
