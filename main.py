from code_generater.pytorch import model_generator
import tools

if __name__ == '__main__':
    python_files = model_generator.run(directory='templates/pytorch/model/')
    for file_name in python_files:
        python_file, file_path = python_files[file_name]
        # tools.list_printer(python_file)
        tools.list_writer(file_path, python_file)

