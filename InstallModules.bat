REM This is setup script for install requed modules for HraZaHodnePenez.py
REM The modules which will be installed:
REM 					-PyGame
REM 					-Pygame GUI
REM 					-git
REM This script must be running with administrator privileges
REM Installer by James Construct

set ok=0
color c
@echo off
cls

echo Following modules will be installed on your computer: PyGame, Pygame GUI.
:Ask
echo Press Y to continue or N to abord action.
set INPUT=
set /P INPUT=Type input: %=%
If /I "%INPUT%"=="y" goto install
If /I "%INPUT%"=="n" exit
echo Incorrect input & goto Ask

:install
echo Installing requed modules (PyGame, Pygame GUI)
echo Installing PyGame (1/2)
pip install PyGame && (
   set pygame=OK
   set /a "ok=%ok%+1"
) || (
   set pygame=FAILED
)
echo DONE!

echo Installing Pygame GUI (2/2)
pip install PygameGUILib && (
   set gui=OK
   set /a "ok=%ok%+1"
) || (
   set gui=FAILED
)
echo DONE!


if "%ok%" EQU "2" (
	echo All packeges where installed successfully.
)
if not "%ok%" EQU "2" (
	echo Installation status:
	echo PyGame: %pygame%
	echo Pygame GUI: %gui%
)

pause
