#!/bin/bash

# Step 0: Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python is not installed or not added to PATH. Please install Python and try again."
    exit 1
fi

# Step 1: Set up virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment. Please check your Python installation."
    exit 1
fi

# Step 2: Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

# Step 3: Check for pip (Python package manager) inside venv
echo "Checking for pip..."
pip --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "pip is not installed. Installing pip..."
    python3 -m ensurepip --default-pip
    if [ $? -ne 0 ]; then
        echo "Failed to install pip. Please check your Python installation."
        exit 1
    fi
fi

# Step 4: Install required dependencies from requirements.txt inside venv
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies. Please check your requirements.txt file."
    exit 1
fi

# Step 5: Run the GUI application
echo "Running the GUI application..."
python3 run.py
if [ $? -ne 0 ]; then
    echo "Failed to launch the application. Please check your code for errors."
    deactivate
    exit 1
fi

# Step 6: Deactivate virtual environment after the application closes
echo "Deactivating virtual environment..."
deactivate

echo "Done!"