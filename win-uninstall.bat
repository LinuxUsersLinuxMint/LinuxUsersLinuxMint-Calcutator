@echo off
@title=Python-Calcutator Uninstall
:m
cls
echo Python-Calcutator Uninstall
echo Are you sure you want to uninstall Python-Calcutator?
echo Yes (1)
echo No (2)
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==1 goto one
if %input%==2 goto two
goto m
:one
echo Python-Calcutator Uninstall.
pause
del C:\Users\%users%\calc
pause
exit
goto m
:two
echo Python-Calcutator removal has been cancelled.
pause
exit