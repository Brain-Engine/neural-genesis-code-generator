import os
import json


def read_json(json_dir, json_name):
    json_path = os.path.join(json_dir, json_name)
    with open(json_path, 'r') as json_file:
        config = json.load(json_file)
    return config
