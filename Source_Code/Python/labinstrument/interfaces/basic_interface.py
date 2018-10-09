import abc
import copy
import json
import os
from ..tools.builtin_ex import *

class IConfigurable:
    @abc.abstractmethod
    def set_parameters(self, parameter):
        pass

    @abc.abstractmethod
    def get_parameters(self):
        pass

    def verify_config(self,parameter):
        if self.dump_config(parameter)==parameter:
            return 1
        else:
            return 0

    def load_config(self, cfg):
        """
        This method is to convert serialized setting -> instrument
        :param cfg: dict
        :return: json
        """
        # as we may have a problem of where we should delete the values of unused
        # 1. we delete in every package(set_parameters), there should be a little complex in writing the module.
        # 2. we delete in load_config(this function), will cuz a little complex in writing module, too.
        #    and may also cuz some risk in writing module:
        #    (if the module want a key, but the key is removed, this will cuz key error Exception)
        # Analyse: way 1 bring a rule into coding, and makes coding module a little complicated
        #          way 2 bring a rule into coding, and bring a little cost in running script,
        #
        #
        # Finally: I choose the Second way. To Send Useful Message Into Module And Determine Whither It Is Useful Here
        parameter = json.loads(cfg)
        return self.set_parameters(parameter)

    def dump_config(self, cfg: dict = None):
        """
        This method is get instrument settings-> serialized setting 
        :param cfg: dict   this parameter is a predefined config, 
                           any config not shown in this config will save as 'unused_cfg' instead of its real value 
        :return: Boolean
        """
        # if have a pre-config config, then we need to take unused into consideration
        # else we should get all settings from instrument
        # !!! I should keep this config without empty dict inside
        if cfg:
            ret_val = copy.deepcopy(cfg)
            instrument_cfg = self.get_parameters()
            for key_map, keys_dict, keys_value in dict_walk(ret_val):
                for key in keys_value:
                    if get_dict_with_key_list(ret_val, key_map)[key] != 'unused':
                        get_dict_with_key_list(ret_val, key_map)[key] = get_dict_with_key_list(instrument_cfg, key_map)[
                            key]
            return json.dumps(ret_val)
        else:
            return json.dumps(self.get_parameters())

    def save_snapshot(self, param):
        """
        This method is to save instrument's setting -> quick save
        :param param: name of sav file, should be anything any type you want
        :return: None 
        """
        file_path = os.path.join(__file__, 'snapshot', str(param) + '.sav')
        if not os.path.exists(os.path.join(__file__, 'snapshot')):
            os.makedirs(os.path.join(__file__, 'snapshot'))
        with open(file_path, 'w') as f:
            f.write(self.dump_config())

    def load_snapshot(self, param):
        """
        This method is to set quick save -> instrument's setting
        :param param: name of sav file, should be anything any type you want
        :return: None
        """
        file_path = os.path.join(__file__, 'snapshot', str(param) + '.sav')
        if not os.path.exists(os.path.join(__file__, 'snapshot')):
            os.makedirs(os.path.join(__file__, 'snapshot'))
        with open(file_path, 'r') as f:
            self.load_config(f.read())