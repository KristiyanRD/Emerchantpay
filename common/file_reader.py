import json
import os
import yaml


class FileReader:

    @staticmethod
    def yaml_reader(relative_path=''):
        with open(os.path.realpath(relative_path), "r") as cfg:
            try:
                data = yaml.safe_load(cfg)
                return data
            except yaml.YAMLError as exc:
                return print(exc)

    @staticmethod
    def json_reader(relative_path=''):
        with open(os.path.realpath(relative_path), "r") as cfg:
            try:
                data = json.loads(cfg.read())
                return data
            except json.JSONDecodeError as exc:
                return print(exc)
