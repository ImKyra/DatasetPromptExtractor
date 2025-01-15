@echo off
REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH. Please install Python and try again.
    pause
    exit /b
)

REM Step 1: Set up virtual environment
echo Creating virtual environment...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo Failed to create virtual environment. Please check your Python installation.
    pause
    exit /b
)

REM Step 2: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b
)

REM Step 3: Check for pip (Python package manager) inside venv
echo Checking for pip...
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --default-pip
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to install pip. Please check your Python installation.
        pause
        exit /b
    )
)

REM Step 4: Install required dependencies from requirements.txt inside venv
echo Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies. Please check your requirements.txt file.
    pause
    exit /b
)

REM Step 5: Run the GUI application
echo Running the GUI application...
python run.py
if %ERRORLEVEL% NEQ 0 (
    echo Failed to launch the application. Please check your code for errors.
    pause
    exit /b
)

REM Step 6: Deactivate virtual environment after the application closes
echo Deactivating virtual environment...
deactivate

pause