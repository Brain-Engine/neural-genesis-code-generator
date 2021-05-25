import torch
import time
import neural_genesis
from framework_analyse.class_info_analyse import get_attr_init_dict
from tools import save_as_json


if __name__ == '__main__':
    # start = time.time_ns()
    start = time.time()
    info_dict = get_attr_init_dict(neural_genesis.nn)
    # end = time.time_ns()
    end = time.time()
    save_as_json(info_dict, './function_attr.json')
    print(end-start)
