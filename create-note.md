
sudo apt-get update
sudo apt-get install python3
#make dir
mkdir resume-demo



python3 -m venv virt
source virt/bin/activate
pip install django Pillow django-ckeditor

#check
pip freeze
#build
django-admin startproject resume_demo

python manage.py startapp main

## upload to github

## open settings.py
add main to INSTALLED_APPS

step 1-4

### create context_processors.py

### modify urls.py in resume_demo

### create urls.py in main

### modify models.py in main

### modify admin.py in main/  !!!important 
from .models import *

### create signals.py in main

### connect signals.py in apps.py in main


### create models forms.py in main

### create views.py in main

### create templates folder in main
create a folder called main in templates folder, this is where we put all the html files

### run pip freeze
run pip freeze to check if we have all the packages we need
```
pip freeze > requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```