import os


def read_templates(template_dir, template_name='model.template'):
    template_path = os.path.join(template_dir, template_name)
    with open(template_path, mode='r') as template_file:
        template = template_file.readlines()
    return template
