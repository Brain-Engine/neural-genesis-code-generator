import json
import os
# debug
import tools


def read_json(json_dir, json_name):
    json_path = os.path.join(json_dir, json_name)
    with open(json_path, 'r') as json_file:
        config = json.load(json_file)
    return config


def read_templates(template_dir, template_name='model.template'):
    template_path = os.path.join(template_dir, template_name)
    with open(template_path, mode='r') as template_file:
        template = template_file.readlines()
    return template


def generator(indexs: dict, template: list, config: dict):
    """

    :param indexs: line-index in template when run str insert.
    :param template: file template (example: "xxx/xxx/model/model.template")
    :param config: items will be insert into template
    :return: template
    >>># Model Name
    >>>template[indexs['Name']] = template[indexs['Name']].format("ModelName")
    >>># Parent Model Init
    >>>template[indexs['Super']] = template[indexs['Super']].format("ModelName")
    >>># Model Attribute
    >>>template[indexs['Attribute']] = template[indexs['Attribute']].format("self.conv = nn.Conv2d(MyParameters)")
    >>># Forward Input
    >>>template[indexs['Input']] = template[indexs['Input']].format("x")
    >>># Forward Body
    >>>template[indexs['Forward']] = template[indexs['Forward']].format("x = x")
    >>># Forward Output
    >>>template[indexs['Output']] = template[indexs['Output']].format("x")
    >>>tools.list_printer(template)
    """
    for name in indexs:
        template[indexs[name]] = template[indexs[name]].format(*config[name])

    return template


def run(directory, template_name='model.template', config_name='config.json', index_name='index.json'):
    indexs = read_json(directory, index_name)['model.template']
    template = read_templates(directory, template_name)
    config = read_json(directory, config_name)
    # generate python files
    python_files = {}
    for model_name in config:
        python_files[model_name] = generator(indexs, template, config[model_name]), config[model_name]['Path']

    return python_files
