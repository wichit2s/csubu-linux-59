import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-author', '-c', is_flag=True, help='Computer Science at UBU')
@click.argument('name', default='wichit2s', required=False)
def main(name, as_author):
    """Get Github Avatar"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    api_user_url = 'https://api.github.com/users/{}'.format(name)
    json = requests.get(api_user_url).json()
    req = requests.get(json['avatar_url'])
    img = Image.open(StringIO(req.content))
    img.show()
