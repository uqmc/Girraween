#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main project routine
"""

from flask import Flask
from flask_restful import Api

from config import Config
from utils import logging_setup
from api.ping import PingResource

config = Config()

app = Flask(__name__)
api = Api(app)

api.add_resource(PingResource, "/api/ping")


def main():
    logging_setup.setup()
    app.run(
        host="0.0.0.0",
        port=3000,
        debug=not config.get_is_production()
    )


if __name__ == "__main__":
    main()
