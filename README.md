# Django Default Template
Default template for my personal/profissional Django projects
Useful if you develop in Windows and deploy in Linux

## Usage:

django-admin.py startproject --template=https://github.com/alexeiramone/django-default-template/archive/master.zip whatever

## Run.bat
- We use mongoose 4.1 one folder above project to serve media to every project.
- Run.bat calls mongoose and django in two separate command windows and opens another one if you need to call some `manage.py shell` or something

### This will set (among many others):
- GRAPPELLI_ADMIN_TITLE = u'{{ project_name|capfirst }}'

## Manual Overrides
- local.py - MAILGUN_ACCESS_KEY


## TODO:
- Use env keys
- Chance FileCache to Memcached new config
- settings/remote.py - everything worth looking at

