# Django Default Template
Default template for my personal/profissional Django projects
Useful if you develop in Windows and deploy in Linux

## Usage:

    django-admin.py startproject --template=https://github.com/alexeiramone/django-default-template/archive/master.zip **whatever**

Where `whatever` is the projectname.

This will create (where you ran `django-admin.py`):

    \whatever
    \whatever\.gitignore
    \whatever\LICENSE
    \whatever\manage.py
    \whatever\README.md
    \whatever\run.bat
    \whatever\settings
    \whatever\whatever
    \whatever\_cache
    \whatever\_log
    \whatever\_media
    \whatever\settings\base.py
    \whatever\settings\local.py
    \whatever\settings\remote.py
    \whatever\settings\__init__.py
    \whatever\whatever\context_processors.py
    \whatever\whatever\urls.py
    \whatever\whatever\wsgi.py
    \whatever\whatever\__init__.py
    \whatever\_cache\void.txt
    \whatever\_log\default.log
    \whatever\_media\uploads
    \whatever\_media\_versions
    \whatever\_media\uploads\void.txt
    \whatever\_media\_versions\void.txt

### Features
- We use Mongoose 4.1 one folder above project_folder to serve media to every project. It's light, it works, it's standalone and Norton Antivirus nags like hell if try to use Mongoose 5.x
- Postgresql database
- Mailgun Backend config via django_mailgun
- Database Name and Database Username are the project name's first 8 chars
- Grappelli
- Filebrowser
- Some Filebrowser configurations based on largest Bootstrap 3 column widths

## Run.bat
- Spawns Mongoose preconfigured to this project's default media path
- Spawns Django `manage.py runserver 0.0.0.0:8000`
- Spawns a Command Window if you need to call `manage.py shell` or something

## Manual Overrides
- settings/local.py - MAILGUN_ACCESS_KEY
- settings/remote.py - everything worth looking at

## TODO:
- Use env keys
- Chance FileCache to Memcached new config
- I18N deprecation: `USE_I18N = True` and `django.core.context_processors.i18n`

