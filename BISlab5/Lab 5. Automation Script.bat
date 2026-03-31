@echo off
REM Path to Google Chrome
set chromePath="C:\Program Files\Google\Chrome\Application\chrome.exe"

REM Path to SQL Server 2022 Configuration Manager
set sqlConfigPath="%ProgramData%\Microsoft\Windows\Start Menu\Programs\Microsoft SQL Server 2022\Configuration Tools\SQL Server 2022 Configuration Manager.lnk"

REM Path to SQL Server Management Studio 19
set ssmsPath="C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE\Ssms.exe"

REM Path to Services Manager
set servicesPath="%windir%\system32\services.msc"

REM Path to Python executable
set pythonPath="C:\Users\Rabin Ghimire\AppData\Local\Programs\Python\Python37-32\python.exe"

REM Paths to Python files
set lab2Path="E:\Desktop\St Xaviers College\BIM VI Sem BIS\Lab 2 Python File Linear Regression.py"
set lab3Path="E:\Desktop\St Xaviers College\BIM VI Sem BIS\Lab 3 Python File K Means Clustering.py"

REM Open each URL in Google Chrome
start "" %chromePath% "https://drive.google.com/drive/home"
start "" %chromePath% "https://mail.google.com/mail/u/0/#inbox"

REM Open SQL Server 2022 Configuration Manager
start "" %sqlConfigPath%

REM Open SQL Server Management Studio 19
start "" %ssmsPath%

REM Check MSSQL$SQLEXPRESS service status
echo Checking MSSQL$SQLEXPRESS service status...
sc query "MSSQL$SQLEXPRESS" | findstr /i "RUNNING"
if %errorlevel%==0 (
    echo MSSQL$SQLEXPRESS service is already running.
) else (
    echo MSSQL$SQLEXPRESS service is not running. Attempting to start...
    net start "MSSQL$SQLEXPRESS"
    if %errorlevel%==0 (
        echo MSSQL$SQLEXPRESS service started successfully.
    ) else (
        echo Failed to start MSSQL$SQLEXPRESS service. Please check manually.
    )
)

REM Execute Lab 2 Python script
echo Executing Lab 2: Linear Regression...
%pythonPath% %lab2Path%
if %errorlevel%==0 (
    echo Lab 2: Linear Regression executed successfully.
) else (
    echo Failed to execute Lab 2: Linear Regression. Please check the file or Python installation.
)

REM Execute Lab 3 Python script
echo Executing Lab 3: K-Means Clustering...
%pythonPath% %lab3Path%
if %errorlevel%==0 (
    echo Lab 3: K-Means Clustering executed successfully.
) else (
    echo Failed to execute Lab 3: K-Means Clustering. Please check the file or Python installation.
)

REM Open Services Manager
start "" %servicesPath%

REM Display completion message
echo All websites, applications, services, and Python scripts have been processed successfully.
pause
