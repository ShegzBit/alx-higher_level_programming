#!/usr/bin/python3
"""
A sript that taskes arguments to it and parse them into
a json file
"""
from sys import argv
from io import StringIO
from json import dump, dumps, load, loads
from os.path import exists


_save = __import__("5-save_to_json_file").save_to_json_file
_load = __import__("6-load_from_json_file").load_from_json_file
data = argv[1:]

prev_data = []

if exists("add_item.json"):
    prev_data = _load("add_item.json")

main_data = prev_data + data
_save(main_data, "add_item.json")
