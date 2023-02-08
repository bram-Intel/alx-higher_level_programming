#!/usr/bin/python3
"""defining load_from_json_file function"""


import json

def save_to_json_file(my_obj, filename):
    """writes an object to text file"""
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)


