import inspect


def get_attr_name(attr):
    attr_list = []
    for name in attr.__dict__:
        if not str(name).islower():
            # print(name)
            attr_list.append(name)

    return attr_list


def get_attr_by_name(attr_dict, sub_attr_name):
    return attr_dict.__dict__[sub_attr_name]


def get_attr_info_list(attr):
    attr_info_list = []
    for name in attr.__dict__:
        if not str(name).islower():
            try:
                attr_info = {}
                sub_attr = attr.__dict__[name]
                init_func = sub_attr.__init__
                inspect.signature(init_func)
                # print(init_func)
                params = init_func.__code__.co_varnames
                # print(params)
                # print(param)
                attr_info["name"] = name
                attr_info["params"] = params

                attr_info_list.append(attr_info)
            except:
                pass
    return attr_info_list


def get_attr_info_dict(attr, replace_param_self=False):
    attr_info_dict = {}
    for name in attr.__dict__:
        if not str(name).islower():
            try:
                attr_info = {}
                sub_attr = attr.__dict__[name]
                init_func = sub_attr.__init__
                info = inspect.getfullargspec(init_func)

                params = info.args
                params_default_value = info.defaults

                params = list(params)
                params_default_value = list(params_default_value)

                if replace_param_self:
                    params[0] = name
                attr_info["params"] = params
                attr_info["params_default_value"] = params_default_value

                attr_info_dict[name]=attr_info
            except:
                pass
    return attr_info_dict
