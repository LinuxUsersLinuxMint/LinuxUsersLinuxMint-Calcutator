@echo off
@title=Python-Calcutator Uninstall
:m
cls
echo Python-Calcutator Uninstall
echo Which Version Do You Want To Uninstall?
echo 1.Python-Calcutator-TR
echo 2.Python-Calcutator-EN
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==1 goto one
if %input%==2 goto two
goto m
:one
echo Python-Calcutator-TR Uninstall.
pause
del C:\Users\%users%\calc
pause
exit
goto m
:two
echo Python-Calcutator-EN Uninstall.
pause
del C:\Users\%users%\calc
pause
exit