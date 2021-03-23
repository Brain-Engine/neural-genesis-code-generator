import json


def save_as_json(data, path):
    json_data = json.dumps(data, indent=2)
    try:
        with open(path, 'w') as f:
            f.writelines(json_data)
    except:
        print("Fail to save json! Check your path {}.".format(path))

    return json_data
