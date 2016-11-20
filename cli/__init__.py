import click
import requests

from config import api_config_option

from api import create_api
from cli.decorators import api


api_config = None


@click.group()
@click.option('-ae', '--api-environment', default='development',
              help='Specify api environment configuration to use.')
def cli(api_environment):
    global api_config
    api_config = api_config_option[api_environment]
    pass


@cli.command(name='api')
@click.option('-d', '--debug', is_flag=True, help='Enable Flask debugger')
@click.option('-h', '--host', default='127.0.0.1',
              help='Api listen address')
@click.option('-p', '--port', default=5001, help='Api port')
def run_api(debug, host, port):
    api_app = create_api()
    api_app.run(debug=debug, host=host, port=port)


@cli.command()
@api
def hello():
    r = requests.get(api_config.BASE_URL)
    data = r.json()
    click.echo(data)
