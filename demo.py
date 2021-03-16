from code_generater.pytorch import model_generator
import json
import torch
from framework_analyse.class_info_analyse import get_attr_init_dict


def save_as_json(data, path):
    json_data = json.dumps(data, separators=(',', ':'))
    try:
        with open(path, 'w') as f:
            f.writelines(json_data)
    except:
        print("Fail to save json! Check your path {}.".format(path))

    return json_data


if __name__ == '__main__':

    info_dict = get_attr_init_dict(torch.nn)

    save_as_json(info_dict, './demo.json')
