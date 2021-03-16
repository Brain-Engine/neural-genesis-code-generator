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


def get_force_args_and_defaults(func_info, remove_param_self_in_init_func=True):
    # args
    try:
        args = func_info.args
        args = list(args)
    except:
        args = [None]

    # defaults
    try:
        defaults = func_info.defaults
        defaults = list(defaults)
    except:
        defaults = [None]

    args.reverse()
    defaults.reverse()
    force_requrie = [None] * len(args)
    params_default = [None] * len(args)

    for index in range(len(args)):
        params_default[index] = defaults[index] if index < len(defaults) else None
        force_requrie[index] = False if index < len(defaults) else True

    force_requrie.reverse()
    params_default.reverse()
    if remove_param_self_in_init_func:
        force_requrie = force_requrie[1:]
        params_default = params_default[1:]
        args.reverse()
        args = args[1:]

    return args, params_default, force_requrie


def get_varargs_varkw_exists(func_info):
    # varargs
    try:
        varargs = True if func_info.varargs else False
    except:
        print("[ERROR] while get arrt 'func_info.varargs!'")
        raise AttributeError

    # varkw
    try:
        varkw = True if func_info.varkw else False
    except:
        print("[ERROR] while get arrt 'func_info.varkw!'")
        raise AttributeError
    return varargs, varkw


def get_force_kwonlyargs_and_kwonlydefaults(func_info):
    # kwonlyargs
    try:
        kwonlyargs = func_info.kwonlyargs
        # kwonlyargs = list(kwonlyargs)
    except:
        kwonlyargs = {}

    # kwonlydefaults
    try:
        kwonlydefaults = func_info.kwonlydefaults
        # kwonlydefaults = list(kwonlydefaults)
    except:
        kwonlydefaults = {}

    force_requrie = [None] * len(kwonlyargs)
    kwonlyargs_default = [None] * len(kwonlyargs)
    for index, key in enumerate(kwonlyargs):
        if key in kwonlydefaults:
            kwonlyargs_default[index] = kwonlydefaults[key]
            force_requrie[index] = False
        else:
            kwonlyargs_default[index] = None
            force_requrie[index] = True

    return list(kwonlyargs), kwonlyargs_default, force_requrie


def get_annotations(func_info, delete_return=True):
    # annotations
    try:
        params_type = func_info.annotations
        params_type = {key: str(params_type[key]) for key in params_type}
        if 'return' in params_type and delete_return:
            del params_type['return']
    except:
        print("[ERROR] while get attr 'func_info.annotations!'")
        raise AttributeError
    return params_type


def resolve_info(force_args_and_defaults,
                 force_kwonlyargs_and_kwonlydefaults,
                 varargs_varkw_exists,
                 params_type,
                 to_dict=True):
    varargs, varkw = varargs_varkw_exists
    force_args_and_defaults = zip(*force_args_and_defaults)
    info = []
    for i in force_args_and_defaults:
        info.append(list(i))

    if varargs:
        info.append(['args', None, False])

    force_kwonlyargs_and_kwonlydefaults = zip(*force_kwonlyargs_and_kwonlydefaults)
    for i in force_kwonlyargs_and_kwonlydefaults:
        info.append(list(i))

    if varkw:
        info.append(['**kwargs', None, False])

    for params in info:
        if params[0] in params_type:
            param_type = params_type[params[0]]
            params.append(param_type)
        else:
            params.append("Any")

    if to_dict:
        for index, param in enumerate(info):
            info[index] = {"name": param[0], "default_value": param[1], "required": param[2], "type": param[3]}
            dict(info[index])

    # print(info)
    return info


def get_function_info(func_info: inspect.FullArgSpec):
    # Analyse args and defaults.
    force_args_and_defaults = get_force_args_and_defaults(func_info)
    # args, params_default, force_requrie = force_args_and_defaults
    # print(len(force_requrie[1:]))
    # print(len(params_default[1:]))
    # print(len(args[1:]))

    # Set flags for if varargs or varkw exists.
    varargs_varkw_exists = get_varargs_varkw_exists(func_info)
    # varargs, varkw = varargs_varkw_exists
    # print(varargs)
    # print(varkw)

    # Analyse kwonlyargs and kwonlydefaults.
    force_kwonlyargs_and_kwonlydefaults = get_force_kwonlyargs_and_kwonlydefaults(func_info)
    # kwonlyargs, kwonlyargs_default, force_requrie = force_kwonlyargs_and_kwonlydefaults
    # print(force_requrie)
    # print(kwonlyargs_default)
    # print(kwonlyargs)

    # Analyse annotations.
    params_type = get_annotations(func_info)
    # print(len(params_type))
    # print(params_type)

    info = resolve_info(force_args_and_defaults, force_kwonlyargs_and_kwonlydefaults, varargs_varkw_exists, params_type)

    return info


def get_attr_init_dict(attr):
    attr_info_dict = {}
    for name in attr.__dict__:
        if not str(name).islower():
            attr_info = {}
            sub_attr = attr.__dict__[name]

            try:
                init_func = sub_attr.__init__
            except:
                continue
                pass

            print(name)
            info = inspect.getfullargspec(init_func)
            info = get_function_info(info)
            attr_info_dict[name] = info
            # print(info)

    return attr_info_dict
