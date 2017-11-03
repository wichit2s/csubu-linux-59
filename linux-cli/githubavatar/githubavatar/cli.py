import click

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='wichit2s', required=False)
def main(name, as_cowboy):
    """Get Github Avatar"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    import requests
    api_user_url = 'https://api.github.com/users/{}'.format(name)
    j = requests.get(api_user_url).json()
    
    img_data = requests.get(j['avatar_url']).content
    avatarfilename = '{}-avatar.jpg'.format(name)
    with open(avatarfilename, 'wb') as fp:
        fp.write(img_data)
    import subprocess
    subprocess.call(['eog', avatarfilename])
