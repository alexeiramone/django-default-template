@echo OFF
start %CD%\..\mongoose-4.1.exe -document_root %CD%\_media
start %CD%\manage.py runserver 0.0.0.0:8000
start %windir%\system32\cmd.exe %CD%