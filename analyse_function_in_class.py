import torch
from framework_analyse.class_info_analyse import get_attr_init_dict
from tools import save_as_json


if __name__ == '__main__':

    info_dict = get_attr_init_dict(torch.nn)

    save_as_json(info_dict, './function_attr.json')
