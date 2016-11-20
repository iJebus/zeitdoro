from flask import request
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Shutdown(Resource):
    def post(self):
        request.environ.get('werkzeug.server.shutdown')()
