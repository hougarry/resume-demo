#steps to make a new django app

```bash

mkdir env
pwd
python3 -m venv /root/env/md
source /root/env/md/bin/activate
pip install django
django-admin startproject microdomains
cd microdomains
vim microdomains/settings.py
sudo apt-get install python3.8-dev
apt-get install gcc
pip install uwsgi

vim test.py
#input this
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3




uwsgi --http :8000 --wsgi-file test.py
uwsgi --http :8000 --module microdomains.wsgi
sudo apt-get nginx

