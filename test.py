# import re
# from framework_analyse.class_info_analyse import process_param_type
# tem_str = "typing.Union[torch.Size, typing.List[int], typing.Tuple[int, ...], typing.Tuple[typing.Tuple[str, int]]]"
# process_param_type(tem_str)


from framework_analyse.frontend_json_analyse import analyse

node_list, edge_list = analyse("zdemo/20210319112759.json")

print(node_list)
print(edge_list)
