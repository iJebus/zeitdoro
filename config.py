import os


class Config:
    DEBUG = False
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = True


class ApiConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SERVER_NAME = 'localhost:5001'
    BASE_URL = 'http://' + SERVER_NAME


class ApiDevelopmentConfig(ApiConfig):
    DEBUG = False  # Flask debugger does not like not being the main thread


api_config_option = {
    'development': ApiDevelopmentConfig
}
