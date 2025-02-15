import json


class Data:
    def save(self, data, file_path, indent_num=2):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=indent_num)

    def load(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
