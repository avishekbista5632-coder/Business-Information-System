@echo off
echo ==========================================
echo     Machine Learning Lab Automation
echo ==========================================

:: 1. Launch essential applications
echo Launching Google Chrome...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"

echo Launching Visual Studio Code...
start "" "C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"

echo Launching SQL Server Management Studio...
start "" "C:\Program Files (x86)\Microsoft SQL Server Management Studio 18\Common7\IDE\Ssms.exe"

:: 2. Check MSSQL service
echo Checking MSSQL$SQLEXPRESS status...
sc query MSSQL$SQLEXPRESS | find "RUNNING"
IF %ERRORLEVEL% EQU 0 (
    echo MSSQL$SQLEXPRESS is already running.
) ELSE (
    echo Starting MSSQL$SQLEXPRESS service...
    net start MSSQL$SQLEXPRESS
    IF %ERRORLEVEL% EQU 0 (
        echo MSSQL service started successfully.
    ) ELSE (
        echo Failed to start MSSQL service. Please check manually.
    )
)

:: 3. Open Python lab files
echo Opening Python lab files...
set PY_PATH=C:\Users\%USERNAME%\Documents\ML_Labs
if exist "%PY_PATH%\Lab_2.py" (
    start "" "%PY_PATH%\Lab2_LinearRegression.py"
) else (
    echo Lab 2 file not found: %PY_PATH%\Lab2_LinearRegression.py
)

if exist "%PY_PATH%\Lab3_KMeansClustering.py" (
    start "" "%PY_PATH%\Lab3_KMeansClustering.py"
) else (
    echo Lab 3 file not found: %PY_PATH%\Lab3_KMeansClustering.py
)

echo Automation complete.
pause
