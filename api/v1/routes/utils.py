# utils.py

import os
import logging
import subprocess

def get_current_dir():
    """Returns the absolute path of the current working directory"""
    return os.path.abspath(os.getcwd())

def get_script_dir():
    """Returns the absolute path of the script's directory"""
    return os.path.dirname(os.path.abspath(__file__))

def run_command(cmd):
    """Runs a shell command and returns its output"""
    try:
        output = subprocess.check_output(cmd, shell=True)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
        return None

def create_dir(path):
    """Creates a directory if it does not exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def is_file_empty(filename):
    """Checks if a file is empty"""
    return os.path.getsize(filename) == 0