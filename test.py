# import re
# from framework_analyse.class_info_analyse import process_param_type
# tem_str = "typing.Union[torch.Size, typing.List[int], typing.Tuple[int, ...], typing.Tuple[typing.Tuple[str, int]]]"
# process_param_type(tem_str)

from framework_analyse.frontend_json_analyse import analyse, attribute, forward_analyse

node_list, edge_dict = analyse("zdemo/20210319112759.json")

# print(node_list)
# print(edge_dict)

attr_dict, attr_list = attribute(node_list)

# for attr in attr_dict:
#     print(attr_dict[attr])

forward_list, output_id = forward_analyse(attr_dict, edge_dict)

print(forward_list)
print(output_id)

template = {
    "Path": "./demo/model.py",
    "Name": ["MyModel"],
    "Init": [],
    "Super": ["MyModel"],
    "Attribute": attr_list,
    "Input": ["x"],
    "Forward": forward_list,
    "Output": [output_id],
}
