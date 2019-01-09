@ECHO off
SET sharedFolder=C:\Users\IEUser\Desktop\work
SET MainFileName=Main

REM Use --onefile option after convert ui to py. 
pyuic5 "View/Ui_MainWindow.ui" -o "View/Ui_MainWindow.py"

pyinstaller --onefile --distpath "./Product" %MainFileName%.py
copy %sharedFolder%\src\chromedriver.exe %sharedFolder%\src\Product\chromedriver.exe

REM clean up
rmdir /s /q %sharedFolder%\src\__pycache__
rmdir /s /q %sharedFolder%\src\build
del /q %sharedFolder%\src\%MainFileName%.spec


pause

REM python -m PyInstaller.__main__ --clean -F seleniumTest.py -p "C:\ProgramData\chocolatey\lib\python3\tools\Lib\site-packages\PyQt5\Qt\bin"
REM python -m PyInstaller.__main__ --clean -F Main.py -p "C:\ProgramData\chocolatey\lib\python3\tools\Lib\site-packages\PyQt5\Qt\bin"

REM python -m PyInstaller.__main__ Main.spec -p "C:\ProgramData\chocolatey\lib\python3\tools\Lib\site-packages\PyQt5\Qt\bin"
REM C:\ProgramData\chocolatey\lib\python3\tools\Scripts

REM pyinstaller Main.py
REM pyi-makespec --onefile Main.py
REM pyinstaller --onefile --add-data "View/Main.ui;." Main.py -p "C:\ProgramData\chocolatey\lib\python3\tools\Lib\site-packages\PyQt5\Qt\bin"
REM pyinstaller --onefile --add-data "View/Main.ui;View" Main.py -p "C:\ProgramData\chocolatey\lib\python3\tools\Lib\site-packages\PyQt5\Qt\bin"

REM Use --onefile option after convert ui to py. 
REM pyuic5 "View/Ui_MainWindow.ui" -o "View/Ui_MainWindow.py"
REM pyinstaller --onefile Main.py

REM pyinstaller --clean -F Main.spec Main.py