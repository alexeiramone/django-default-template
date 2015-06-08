# Django Default Template
Default template for my personal/profissional Django projects
Useful if you develop in Windows and deploy in Linux

> **IMPORTANT** This project is public but many of the features it uses are loaded from private repositories so this won't work out-of-the-box.

## Usage:

    django-admin.py startproject --extension=py,json --template=https://github.com/alexeiramone/django-default-template/archive/master.zip whatever
    pip install -U -r requirements/local.txt
    manage.py migrate
    manage.py createsuperuser
    manage.py loaddata fixtures.json
    manage.py collectstatic --noinput

Where `whatever` is the projectname.

This will create (where you ran `django-admin.py`):

    \whatever
    \whatever\.gitignore
    \whatever\LICENSE
    \whatever\manage.py
    \whatever\project_static
    \whatever\README.md
    \whatever\run.bat
    \whatever\settings
    \whatever\templates
    \whatever\whatever
    \whatever\_cache
    \whatever\_log
    \whatever\_media
    \whatever\fixtures.json
    \whatever\project_static\alexei.css
    \whatever\project_static\alexei.min.css
    \whatever\project_static\favicon
    \whatever\project_static\img
    \whatever\project_static\favicon\original.png
    \whatever\project_static\img\void.txt
    \whatever\settings\base.py
    \whatever\settings\local.py
    \whatever\settings\remote.py
    \whatever\settings\__init__.py
    \whatever\templates\base.html
    \whatever\templates\email_template.html
    \whatever\templates\index.html
    \whatever\whatever\context_processors.py
    \whatever\whatever\urls.py
    \whatever\whatever\views.py
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
- project_static folder, will be collected. We use it for site-specific assets like logo and CSS overrides (in alexei.css)
- media/favicon - We use [Realfavicongenerator.net](http://realfavicongenerator.net/) and drop all stuff there. Original.png as used as folder placeholder but we always upload the logo original file there.
- /templates/base.html - Extends from core.html (In AMDB's private repo)
- /templates/index.html - Homepage
- /templates/email_template.html - Simple sanitized email template, inherits from private repo too.
- Sites framework: settings.local uses SITE_ID=2 and settings.remote uses SITE_ID=1

## Run.bat
- Spawns Mongoose preconfigured to this project's default media path
- Spawns Django `manage.py runserver 0.0.0.0:8000`
- Spawns a Command Window if you need to call `manage.py shell` or something

## Manual Overrides
- settings/local.py - MAILGUN_ACCESS_KEY
- settings/remote.py - everything worth looking at
- Delete all void.txt files


## TODO:
- Use env keys
- Chance FileCache to Memcached new config
- I18N deprecation: `USE_I18N = True` and `django.core.context_processors.i18n`
- Fixtures: test
- Requirements (update all txts)
- Requirements testing

