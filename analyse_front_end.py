from framework_analyse.frontend_json_analyse import analyse, attribute, forward_analyse
from tools import save_as_json

node_list, edge_dict = analyse("zdemo/20210319112759.json")

attr_dict, attr_list = attribute(node_list)

forward_list, output_id = forward_analyse(attr_dict, edge_dict)

print(forward_list)
print(output_id)

template = {
    "MyModel": {
        "Path": "./demo/model.py",
        "Name": ["MyModel"],
        "Init": [" "],
        "Super": ["MyModel"],
        "Attribute": attr_list,
        "Input": ["x"],
        "Forward": forward_list,
        "Output": [output_id],
    }
}


json_data = save_as_json(template, "./templates/pytorch/demo/config.json")
print(json_data)
