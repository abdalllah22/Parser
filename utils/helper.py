import os
from glob import glob
import sys


def get_format_of_file(formats):
    try:
        file_format = formats
    except Exception as e:
        print(e)
    else:
        return file_format

def get_first_file_name(name):
    try:
        first_file = name
    except Exception as e:
        print(e)
    else:
        return first_file

def get_second_file_name(name):
    try:
        second_file = name
    except Exception as e:
        print(e)
    else:
        return second_file        

def select_all_files():
    os.chdir("input_data/xml")
    global files
    files = glob("*")
    return files