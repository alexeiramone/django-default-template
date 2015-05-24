# amdb-django-default-template
<<<<<<< HEAD
Default template for my personal/profissional Django projects
Useful if you develop in Windows and deploy in Linux

## Usage:

django-admin.py startproject --template= --db_pass=Dbpassword --site_name="Site Name" --site_domain="whatever.com"

## Run.bat
- We use mongoose 4.1 one folder above project to serve media to every project.
- Run.bat calls mongoose and django in two separate command windows and opens another one if you need to call some `manage.py shell` or something

### This will set (among many others):
- GRAPPELLI_ADMIN_TITLE = u'{{ site_name }}'
- DEFAULT_FROM_EMAIL = u'Webmaster <webmaster@{{ site_domain }}>'

## Manual Overrides
- local.py - MAILGUN_ACCESS_KEY


## TODO:
- Use env keys
- Chance FileCache to Memcached new config
- settings/remote.py - everything worth looking at
=======
My personal Django project template
>>>>>>> origin/master
