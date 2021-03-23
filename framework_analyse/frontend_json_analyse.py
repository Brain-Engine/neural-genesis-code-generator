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

    edge_list = []
    edges = json_dict["edges"]
    for edge in edges:
        edge_link = {edge["source"]: edge["target"]}
        edge_list.append(edge_link)

    return node_list, edge_list
