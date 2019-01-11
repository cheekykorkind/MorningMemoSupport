@ECHO off
REM make samba folder
SET sharedFolder=C:\Users\IEUser\Desktop\work
if not exist "%sharedFolder%" mkdir %sharedFolder%
net share Works=%sharedFolder% /grant:everyone,FULL /users:10

REM samba setting part
REM Turn on network discovery
netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes
REM Turn on file and printer sharing
netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes

REM choco install
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
choco upgrade chocolatey

REM python3.5.1 install part
choco install python --version 3.5.1 -y

python -m pip install --upgrade pip
python -m pip install pyqt5
python -m pip install pyqt5-tools
python -m pip install pyinstaller
python -m pip install selenium
python -m pip install clipboard

setx Path "C:\ProgramData\chocolatey\lib\python3\tools\Scripts;%Path%" -m

REM git bash install part
choco install git.install -y

REM git bash command set up part
Call %~dp0\personalGitSetUp.bat

REM notepad++ install part
choco install notepadplusplus.install -y

REM googlechrome install
choco install googlechrome -y

REM Chrome Driver install
choco install selenium-chrome-driver -y
copy C:\tools\selenium\chromedriver.exe %sharedFolder%\src\chromedriver.exe

pause
REM REM python3.5.1 install part
REM bitsadmin.exe /transfer "python3.5.1 down" https://www.python.org/ftp/python/3.5.1/python-3.5.1-amd64.exe %sharedFolder%\python-3.5.1-amd64.exe
REM %sharedFolder%\python-3.5.1-amd64.exe /S

REM REM python3.5.1 user environment variables set up part
REM SET pythonEnv1=%LOCALAPPDATA%\Programs\Python\Python35\Scripts\
REM SET pythonEnv2=%LOCALAPPDATA%\Programs\Python\Python35\
REM setx PATH "%pythonEnv1%;%pythonEnv2%;%PATH%"

