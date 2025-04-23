@echo off
cd /d "%~dp0" 
call ..\.env\Scripts\activate         
call python manage.py runserver
pause                               
