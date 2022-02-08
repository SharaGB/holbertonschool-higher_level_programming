#!/usr/bin/python3
"""
This is the ``base`` module.
"""
import json
import csv


class Base:
    """ Write the first class Base:
    - private class attribute __nb_objects = 0 """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation. """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation. """
        if list_objs is None:
            emp_list = []
        else:
            emp_list = [cls.to_dictionary(idx) for idx in list_objs]

        filename = cls.__name__ + '.json'
        with open(filename, mode='w') as a_file:
            a_file.write(cls.to_json_string(emp_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation. """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if cls.__name__ == "Rectangle":
            dummy = cls(6, 6)
        else:
            dummy = cls(6)
        # Actualiza el diccionario con los elementos de otro objeto diccionario
        # o de un iterable de pares clave/valor (generalmente tuplas)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r') as a_file:
                dict = cls.from_json_string(a_file.read())
                return list(cls.create(**list_) for list_ in dict)
        except:
            return list()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and deserializes in CSV. """
        filename = cls.__name__ + '.csv'
        name = cls.__name__

        if list_objs is None:
            emp_list = []
        else:
            emp_list = [cls.to_dictionary(idx) for idx in list_objs]

        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file)

            if name == 'Rectangle':
                for key in list_objs:
                    csv_writer.writerow(['id', 'width', 'height', 'x', 'y'])
            elif name == 'Square':
                for key in list_objs:
                    csv_writer.writerow(['id', 'size', 'x', 'y'])
            return key

    @classmethod
    def load_from_file_csv(cls):
        """ Serializes and deserializes in CSV. """
        filename = cls.__name__ + '.csv'
        line = 0
        dict = []
        try:
            with open(filename, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if line == 0:
                        line += 1
                    else:
                        dict_ = {'id': int(row[0]), 'size': int(row[1]),
                                 'x': int(row[2]), 'y': int(row[3])}
                        line += 1
                obj = cls.create(**dict_)
                dict.append(obj)

        except:
            return dict
