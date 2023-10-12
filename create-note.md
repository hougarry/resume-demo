
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

### modify admin.py in main/migrations
