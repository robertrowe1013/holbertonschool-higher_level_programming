#!/usr/bin/python3
"""load add save"""
import json
import sys
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file
try:
    arg_list = load("add_item.json")
except:
    arg_list = []
for i in range(1, len(sys.argv)):
    arg_list.append(sys.agrv[i])
save(arg_list, "add_item.json")
