# วิธีการเขียน CLI ด้วย Python
## 1. ติดตั้ง
```sh
pip install --user cookiecutter
pip install --user virtualenv
```

## 2. สร้างโปรแกรมใหม่จาก template บน github
```sh
cookiecutter https://github.com/nvie/cookiecutter-python-cli.git
```
... จากนั้น กรอกข้อมูลเกี่ยวกับโปรแกรมใหม่ จนครบ
```sh
Cloning into 'cookiecutter-python-cli'...
remote: Counting objects: 64, done.
remote: Total 64 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (64/64), done.
Checking connectivity... done.
full_name (default is "Vincent Driessen")? Name LastName
email (default is "vincent@3rdcloud.com")? xxx.yy.59@ubu.ac.th
github_username (default is "nvie")? xxxyy
project_name (default is "My Tool")? Get Github Avatar
repo_name (default is "python-mytool")? githubavatar
pypi_name (default is "mytool")? githubavatar
script_name (default is "my-tool")? githubavatar
package_name (default is "my_tool")? githubavatar
project_short_description (default is "My Tool does one thing, and one thing well.")? Get Github Avatar
release_date (default is "2014-09-04")? 2017-11-02
year (default is "2014")? 2017
version (default is "0.1.0")?
```

## 3. เริ่มเขียนโปรแกรม 
(remove virtualenv)

```sh
cd githubavatar
```

- ติดตั้ง package ที่จำเป็น
```sh
pip install --user click requests Pillow
```

- เปิดไฟล์ เพื่อทำการแก้ไขคำสั่ง
```sh
gedit githubavatar/githubavatar/cli.py &
```

- แก้ไขคำสั่งเป็น
```python
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
```

- บันทึกแล้วปิด
- ติดตั้ง
```sh
pip install --user .
```
- ทดสอบ
```sh
githubavatar wichit2s
githubavatar joinshena
```

# Links
## IMDB API
* http://www.omdbapi.com/ $\to$ https://pypi.python.org/pypi/omdb
* https://imdbpy.sourceforge.io/ 
* https://github.com/msaqib4203/IMDB-API
* https://www.themoviedb.org/

