pyinstaller main.py -F
if %errorlevel% neq 0 exit /b

del /F /Q /S build\main.spec
rmdir /S /Q build

xcopy /E /I binaries\ dist\binaries\
