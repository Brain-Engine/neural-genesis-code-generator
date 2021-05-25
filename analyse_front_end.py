import time
from framework_analyse.frontend_json_analyse import analyse, attribute, forward_analyse
from tools import save_as_json


start = time.time()
# node_list, edge_dict = analyse("zdemo/20210319112759.json")
node_list, edge_dict = analyse("zdemo/20210525151754.json")

# print(edge_dict)
attr_dict, attr_list = attribute(node_list)

forward_list, output_id = forward_analyse(attr_dict, edge_dict)


template = {
    "MyModel": {
        "Path": "./demo/model.py",
        "Name": ["Model"],
        "Init": [" "],
        "Super": ["Model"],
        "Attribute": attr_list,
        "Input": ["x"],
        "Forward": forward_list,
        "Output": [output_id],
        "Function": ["Model"]
    }
}

end = time.time()

json_data = save_as_json(template, "./templates/pytorch/demo/config.json")
# print(json_data)
print(end-start)

