batch
@echo off
echo Deleting temporary files...

:: Delete files in C:\Windows\Temp
del /q /f C:\Windows\Temp\*

:: Delete files in C:\Users\vedan\AppData\Local\Temp
del /q /f C:\Users\vedan\AppData\Local\Temp\*

echo Temporary files deleted.
pause
