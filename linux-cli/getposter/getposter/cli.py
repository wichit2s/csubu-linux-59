import sys
import click
import requests
import json
import re

from PIL import Image
try:
    from StringIO import StringIO
except: # when using python3.x
    from io import BytesIO, StringIO

from bs4 import BeautifulSoup

#IMDBSEARCHURL = 'http://www.imdb.com/search/title?title=The%20Godfather&page=1&ref_=adv_nxt'

IMDBSEARCHURL = 'http://www.imdb.com/search/title?title={}&page={}&ref_=adv_nxt'

def extractmovieinfo(div):
    data = {}

    # id & title & runtime
    img = div.find_next('img')
    data['id'] = img['data-tconst']
    data['title'] = img['alt']
    try:
        data['runtime'] = div.find_next('span', attrs={'class':'runtime'}).text
    except: pass

    # url & year
    h3 = div.find_next('h3')
    data['url'] = 'http://www.imdb.com{}'.format(h3.find_next('a')['href'])
    year = h3.find_next('span', attrs={'class': ['lister-item-year',
    'text-muted unbold']}).text
    data['year'] = re.findall(r'\d+', year)[0]

    # gross
    try:
        p = div.find_all('span')
        data['gross'] = int(p[-1]['data-value'].replace(',',''))
    except: pass

    # rating
    try:
        rate = div.find_next('div', attrs={'class':['rating']}).find_all('meta')
        data['rate'] = float(rate[0]['content'])
        data['total'] = int(rate[1]['content'])
        data['vote'] = int(rate[2]['content'])
    except: pass

    return data

def searchmovies(title):
    b = BeautifulSoup(requests.get(IMDBSEARCHURL.format(title, 1)).text, 'lxml')
    return b.find_all('div', attrs={'class': ['lister-item', 'mode-advanced']})
    
@click.command()
@click.option('--search', '-s', is_flag=True, help='search all result from text.')
@click.argument('title', required=False)
def main(title, search):
    """Search and show movie poster from search."""
    if title:
        movies = [ extractmovieinfo(div) for div in searchmovies(title) ]
        if search: 
            click.echo('seaching for title = {}'.format(title))
            print('{:10} {:30} {:^6} {:^5} {:>15}'.format(
                    'id', 'title', 'year', 'rate', 'gross'))
            for m in movies:
                try:
                    print('{:10} {:30} {:6} {:6} {:15}'.format(
                        m['id'], m['title'][:30], m['year'], m['rate'], m['gross']))
                except: pass
        else:
            movie = movies[0]
            click.echo('showing poster "{}"'.format(movie['title']))
            try:
                print('{:10} {:30} {:^6} {:^5} {:>15}'.format(
                    'id', 'title', 'year', 'rate', 'gross'))
                print('{:10} {:30} {:6} {:6} {:15}'.format(
                    movie['id'], movie['title'][:30], movie['year'], movie['rate'], movie['gross']))
            except: pass
            b = BeautifulSoup(requests.get(movie['url']).text, 'lxml')
            poster = b.find_all('div', attrs={'class':'poster'})[0]
            imgurl = poster.find_next('img')['src']
            req = requests.get(imgurl)
            if sys.version_info >= (3,0): 
                img = Image.open(BytesIO(req.content)) 
                img.show() 
            else: 
                img = Image.open(StringIO(req.content)) 
                img.show()
    else:
        click.echo('usage: getposter "The Movie Title"')

