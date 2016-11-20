import logging
import requests
from flask import Flask
from flask_restful import Api
from multiprocessing import Process

import cli
from api.resources import HelloWorld, Shutdown


def create_api(config_name='default'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(cli.api_config)

    api.add_resource(HelloWorld, '/')
    api.add_resource(Shutdown, '/shutdown')

    return app


def start_api(config_name='default'):
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    # log.disabled = True

    api_app = create_api()

    p = Process(target=api_app.run)
    p.start()

    while True:
        try:
            requests.get(cli.api_config.BASE_URL, timeout=0.1)
            return
        except requests.exceptions.ConnectionError:
            pass


def stop_api(config_name='default'):
    requests.post(cli.api_config.BASE_URL + '/shutdown')
