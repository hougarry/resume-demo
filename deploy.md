```
root@ubuntu-s-2vcpu-2gb-sfo3-01:~# cd resume
root@ubuntu-s-2vcpu-2gb-sfo3-01:~/resume# python3 -m venv /root/resume/env
root@ubuntu-s-2vcpu-2gb-sfo3-01:~/resume# ls /root/resume/env
bin  include  lib  lib64  pyvenv.cfg
root@ubuntu-s-2vcpu-2gb-sfo3-01:~/resume# source /root/resume/env
-bash: source: /root/resume/env: is a directory
root@ubuntu-s-2vcpu-2gb-sfo3-01:~/resume# source /root/resume/env/bin/activate
(env) root@ubuntu-s-2vcpu-2gb-sfo3-01:~/resume# which python
/root/resume/env/bin/python



pip install django




```


Mistakes when deploy on VPS:
1. name method :
I both use resume_demo and resume-demo, but I should use resume_demo, it confused

my server_name : garyhou2023.top www.garyhou2023.top;

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')  # This is where collectstatic will place files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
, according to this, 

```shell

server {
    listen 80;
    server_name garyhou2023.top www.garyhou2023.top;
    charset utf-8;


    # Django media and static files
    location /media/ {
        alias /root/resume/resume_demo/media;
    }
    location /static/ {
        alias /root/resume/resume_demo/static_collected;
    }

    # Send all non-media requests to the Django server.
    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/root/resume/resume_demo/resume_demo.sock;
    }
}
```

rm -rf /etc/nginx/sites-available/resume_demo
vim /etc/nginx/sites-available/resume_demo
rm -rf /etc/nginx/sites-enabled/resume_demo
sudo ln -s /etc/nginx/sites-available/resume_demo /etc/nginx/sites-enabled/
systemctl restart nginx
-----------------

vim  /etc/nginx/uwsgi_params #create a file

uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;








```shell

pip install -r requirements.txt



pip install gcc python3-devel uwsgi


uwsgi --http :8000 --module resume_demo.wsgi

sudo apt install nginx



sudo nano /etc/nginx/sites-available/resume-demo 


sudo ln -s /etc/nginx/sites-available/resume_demo /etc/nginx/sites-enabled/




sudo nginx -t

sudo rm /etc/nginx/sites-enabled/default

uwsgi --socket resume_demo.sock --module resume_demo.wsgi --chmod-socket=666
sudo chown www-data:www-data /root/resume/resume_demo/resume_demo.sock




python manage.py collectstatic # collect all static files to static_collected


sudo etc/init.d/nginx restart   # restart nginx or use systemctl restart nginx





```















Or
    # Send all non-media requests to the Django server.
    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/root/resume/resume_demo/resume_demo.sock;
    }

proxy_pass:

This is used when Nginx acts as a reverse proxy and forwards the request to another HTTP server.
The server can be an application server, another web server, or any server that speaks the HTTP protocol.
When using proxy_pass, Nginx uses the HTTP protocol to communicate with the backend.
This is the most common scenario and is used when you want to serve dynamic content from an application server (like Django, Flask, or Node.js) or when you want to use Nginx as a load balancer for multiple application servers.

uwsgi_pass:

This is used when Nginx communicates directly with a uWSGI server, which is running a uWSGI-supported application (like a Django app using uWSGI as the application server).
The uwsgi_pass directive uses the uWSGI protocol, which is a fast binary protocol, to communicate with the backend.
It's specifically tailored for uWSGI and is more efficient than the standard HTTP protocol for this purpose.
The include /etc/nginx/uwsgi_params; line is crucial as it sets the necessary parameters for the uWSGI protocol.
This is the least common scenario and is used when you want to serve dynamic content from a uWSGI application server.





#Gunicorn

vim /etc/systemd/system/gunicorn.service
then input this:

```shell
echo "[Unit]
Description=gunicorn daemon for Django project
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/resume/resume_demo
ExecStart=/root/resume/env/bin/gunicorn --workers 3 --bind unix:/root/resume/resume_demo/resume_demo.sock resume_demo.wsgi:application

[Install]
WantedBy=multi-user.target" 

```
after that
```shell


sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn



```



Domain point to VPS:

add A name like this table:
Type	Name	Content	        Proxy Status	TTL
A	      @ 	159.223.207.23	DNS only	Auto
CNAME	www	     @	            DNS only	Auto
CNAME	Project	     @	            DNS only	Auto
Here @ means root domain, www means subdomain

my domain is garyhou2023.top, so I add A name @ means garyhou2023.top, and add CNAME www means www.garyhou2023.top, and add CNAME Project means Project.garyhou2023.top

then go to VPS and input this:
```shell
sudo apt-get update
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'Nginx HTTPS'
sudo ufw status
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
sudo systemctl stop nginx

vim /etc/hosts
```
then input this:
```shell
0.0.0.0       garyhou2023.top
0.0.0.0       www.garyhou2023.top



server {
    listen 80;
    server_name me.garyhou2023.info www.me.garyhou2023.info;
    charset utf-8;

    access_log /var/log/nginx/garyhou2023.top.access.log;
    error_log /var/log/nginx/garyhou2023.top.error.log;
    # Django media and static files
    location /media/ {
        alias /root/resume/resume_demo/media/;
    }
    location /static/ {
        alias /root/resume/resume_demo/static_collected/;
    }

    # Send all non-media requests to the Django server.
    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/root/resume/resume_demo/resume_demo.sock;
    }
}
