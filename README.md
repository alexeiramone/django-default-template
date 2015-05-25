# Django Default Template
Default template for my personal/profissional Django projects
Useful if you develop in Windows and deploy in Linux

## Usage:

django-admin.py startproject --template=https://github.com/alexeiramone/django-default-template/archive/master.zip whatever

## Run.bat
- We use mongoose 4.1 one folder above project to serve media to every project.
- Run.bat calls mongoose and django in two separate command windows and opens another one if you need to call some `manage.py shell` or something

### Features
- Postgresql database
- Mailgun Backend config via django_mailgun
- Database Name and Database Username are the project name's first 8 chars
- Grappelli
- Filebrowser
- Some Filebrowser configurations based on largest Bootstrap 3 column widths

## Manual Overrides
- settings/local.py - MAILGUN_ACCESS_KEY
- settings/remote.py - Tons o' configs

## TODO:
- Use env keys
- Chance FileCache to Memcached new config
- settings/remote.py - everything worth looking at

