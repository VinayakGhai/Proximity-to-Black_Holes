@echo off
REM Auto Push for GitHub + OSF
REM Save this as auto_push.bat in C:\Users\Vinayak\Documents\OTPOCMRRTBHL

cd /d "%~dp0"

REM 1. Stage all changes
git add .

REM 2. Commit with timestamp
for /f "tokens=1-6 delims=/: " %%a in ("%date% %time%") do (
    set timestamp=%%c-%%b-%%a_%%d-%%e-%%f
)
git commit -m "Auto commit: %timestamp%"

REM 3. Push to GitHub
git push origin main

REM 4. Push to OSF
git push osf main

echo Changes pushed to GitHub and OSF at %timestamp%
