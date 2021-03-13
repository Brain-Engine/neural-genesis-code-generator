import os
# import shutil


def list_writer(file_path, data_list, use_abs_path=True):
    if use_abs_path:
        file_path = os.path.abspath(file_path)

    file_dir = os.path.dirname(file_path)
    os.makedirs(file_dir, exist_ok=True)
    print(file_dir)
    with open(file_path, 'w+') as f:
        f.writelines(data_list)
