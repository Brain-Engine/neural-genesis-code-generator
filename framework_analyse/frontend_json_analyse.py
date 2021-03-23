import json


def analyse(file_path: str):
    try:
        with open(file_path, 'r') as f:
            json_dict = json.load(f)
    except:
        print("[ERROR]Load json file {} failed.".format(file_path))

    nodes = json_dict["nodes"]
    node_list = []
    for node in nodes:
        node_dict = {}
        param_dict = {}
        neural_network_data = node["neuralNetworkData"]
        for param in neural_network_data:
            if param["value"] == param['default_value'] and not param['required']:
                pass
            else:
                param_dict[param["name"]] = param["value"]

        node_dict["id"] = node["id"]
        node_dict["name"] = node["label"]
        node_dict["params"] = param_dict
        node_list.append(node_dict)

    edge_dict = {}
    edges = json_dict["edges"]
    for edge in edges:
        edge_dict[edge["source"]] = edge["target"]

    return node_list, edge_dict


def attribute(node_list: list):
    attr_dict = {}
    attr_list = []
    for node in node_list:

        params = node['params']
        param_string = ""
        for param in params:
            # print(param, params[param])
            param_string += f"{param}={params[param]}, "

        attr_string = f"self.{node['name']}_{node['id']} = nn.{node['name']}({param_string[:-2]})"
        attr_dict[node['id']]={"name": f"self.{node['name']}_{node['id']}",
                          "attribute": attr_string}
        attr_list.append(attr_string)

    return attr_dict, attr_list


def forward_analyse(attr_dict: dict, edge_dict: dict):
    input_id = 'x'
    output_id = 'x'
    forward_list=[]
    for source in edge_dict:
        output_id = source
        forward_list.append(f"{output_id} = {attr_dict[output_id]['name']}({input_id})")
        input_id = output_id

    return forward_list, output_id


'''
x
a b
b c
c d

'''