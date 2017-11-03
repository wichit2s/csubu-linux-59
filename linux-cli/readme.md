# วิธีการเขียน CLI ด้วย Python
## 1. ติดตั้ง
```sh
sudo apt install curl
curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
pipsi install cookiecutter
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
```sh
cd githubavatar
```
- เตรียม virtualenv สำหรับพัฒนาโปรแกรม
```sh
virtualenv .env
source .env/bin/activate
```


- ติดตั้ง package 'requests' สำหรับต่อเว็บ
```sh
pip install click requests
```

- เปิดไฟล์ เพื่อทำการแก้ไขคำสั่ง
```sh
gedit githubavatar/githubavatar/cli.py &
```

- แก้ไขคำสั่งเป็น
```python
import click

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='wichit2s', required=False, help='login name for github')
def main(name, as_cowboy):
    """Get Github Avatar"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    import requests
    api_user_url = 'https://api.github.com/users/{}'.format(name)
    j = requests.get(api_user_url).json()
    
    img_data = requests.get(j['avatar_url']).content
    avatarfilename = '{}-avatar.png'.format(name)
    with open(avatarfilename, 'wb') as fp:
        fp.write(img_data)
    import subprocess
    subprocess.call(['eog', avatarfilename])

```

- บันทึกแล้วปิด
- ติดตั้งแล้วทดสอบ
```sh
pip install --editable .
githubavatar wichit2s
```
