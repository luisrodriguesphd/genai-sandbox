#!/bin/bash

REPO_NAME="single_vs_multi_agent"
echo "Start setting up the $REPO_NAME repository"

echo "****************************************"
echo "Install pip using ensurepip and upgrade"
echo "****************************************"
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# Check if pip installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to ensure the installation of pip for Python"
    exit 1
fi

echo "****************************************"
echo "Create and Activate Virtual Environment"
echo "****************************************"
python3 -m venv venv

# Check if virtual environment creation was successful
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment"
    exit 1
fi

# Activate the virtual environment
source ./venv/bin/activate

echo "****************************************"
echo "Install Requirements"
echo "****************************************"
python3 -m pip install --upgrade pip
pip install --upgrade setuptools
pip cache purge
pip install -r requirements.txt

# Check if requirements installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install requirements for development"
    exit 1
