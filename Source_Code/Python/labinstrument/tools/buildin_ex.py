#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
import copy


class MultiDict(dict):
    '''
    This class's intend is to avoid the key used before defined error
    '''

    def __missing__(self, key):
        self[key] = MultiDict()
        return self[key]

    def convert2dict(self):
        return eval(str(self))


if __name__ == '__main__':
    print('MultiDict demo')
    a = MultiDict()
    a[1][2][3] = 5
    print(a)
    # convert2dict demo
    a = a.convert2dict()
    print(type(a[1]))


def dict_walk(param: dict, parent=''):
    # this function is used as the os.walk but format with dict, which dict as folder, and which value(not dict) as file
    # parent,key_dicts,key_values
    if not parent:
        parent = []
    dicts = []
    values = []
    for key, value in param.items():
        if type(value) is dict:
            dicts.append(key)
        else:
            values.append(key)
    yield tuple(parent), dicts, values
    for key in dicts:
        cp=parent+[key,]
        for x in dict_walk(param[key], parent=cp):
            yield x

def dict_delta(dict1,dict2):
    '''remain things in dict1 not in dict2'''
    dict3=copy.deepcopy(dict1)
    for x in list(dict_walk(dict1))[::-1]:
        for y in x[1]:
            if get_dict_with_key_list(dict1, x[0] + (y,))==get_dict_with_key_list(dict2, x[0] + (y,)):
                get_dict_with_key_list(dict3,x[0]).pop(y)
        for y in x[2]:
            if get_dict_with_key_list(dict1,x[0]+ (y,))==get_dict_with_key_list(dict2,x[0]+ (y,)):
                get_dict_with_key_list(dict3, x[0]).pop(y)

    return dict_remove_empty(dict3)



def get_dict_with_key_list(param: dict, key):
    '''
    :param param:dict 
    :param key: list / str sep with ','
    :return: value 
    '''
    tmp = param
    # print('tmp,key=',tmp,key)
    for x in key:
        tmp = tmp.get(x)
    return tmp


def dict_find_key(param: dict, key):
    '''
    Use dict walk function to get the key in dict.
    :param param: dict to be scan
    :param key: key to be find
    :return: list format as  [(parent,keys2dict,keys2value)]
    '''
    return [x for x in dict_walk(param) if key in x[1] + x[2]]


def dict_find_value(param: dict, value):
    '''
    Use dict walk function to get the value in dict.
    :param param: dict to be scan
    :param value: value to be find
    :return: list format as [(parent,keys2dict,keys2value)]
    '''
    return [x for x in dict_walk(param) for y in x[1] + x[2] if get_dict_with_key_list(param, x[0] + (y,)) == value]


def dict_remove_pair(param: dict, param_key=None, param_value=None):
    ret_val=copy.deepcopy(param)
    for key, value in list(ret_val.items()):
        if (key == param_key or param_key == None) and (value == param_value or param_value == None):
            ret_val.pop(key)
        elif type(value) is dict:
            ret_val[key]=dict_remove_pair(ret_val[key],param_key,param_value)
    return ret_val


def dict_remove_empty(param: dict):
    ret_val = copy.deepcopy(param)
    for x in list(dict_walk(ret_val))[::-1]:
        for y in x[1]:
            if get_dict_with_key_list(ret_val, x[0] + (y,)) in [{}, dict()]:
                get_dict_with_key_list(ret_val, x[0]).pop(y)
    return ret_val


if __name__ == '__main__':
    print('Walk dict demo')
    a = {'1': 2, '2': {3: {4: {}}}}
    print(a)
    for x in dict_walk(a):
        print(x)
    print('get_dict_with_key_list demo:')
    print(get_dict_with_key_list(a, ['2', 3]))
    print('dict_find_key demo:')
    print(dict_find_key(a, 3))
    print('dict_find_value demo:')
    print(dict_find_value(a, 5))
    print('dict_remove_empty:')
    print(dict_remove_empty({'1': 2, '2': {3: {4: {}}}}))
    print(dict_remove_pair({'1': 2, '2': {3: {4: {}}},3:2},param_key=3))
