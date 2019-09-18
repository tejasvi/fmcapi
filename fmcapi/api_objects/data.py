from unittest import mock

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate


class BaseData(object):

    ATTRIBUTE = 'OVERRIDE_ME'

    def __init__(self, **kwargs):
        print(f'Init for {self.ATTRIBUTE}')
        self.value = None
        self.parse_kwargs(**kwargs)

    def format_data(self):
        print(f'Formatting data for {self.ATTRIBUTE}')
        if self.value:
            return {self.ATTRIBUTE: self.value}
        return None

    def parse_kwargs(self, **kwargs):
        print(f'Parsing kwargs for {self.ATTRIBUTE}')
        if self.ATTRIBUTE in kwargs:
            self.value = kwargs[self.ATTRIBUTE]


class Id(BaseData):
    ATTRIBUTE = 'id'


class Name(BaseData):
    ATTRIBUTE = 'name'


class Type(BaseData):
    ATTRIBUTE = 'type'


class Objects(BaseData):
    ATTRIBUTE = 'objects'


class Literals(BaseData):
    ATTRIBUTE = 'literals'


class NetworkGroups(APIClassTemplate):
    """
    The NetworkGroups Object in the FMC.
    """

    URL_SUFFIX = '/object/networkgroups'

    REQUIRED_FOR_POST = ['name']

    ATTRIBUTES = [Id, Name, Type, Objects, Literals]

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc)
        self.type = 'NetworkGroup'
        self._data = {data.ATTRIBUTE: data() for data in self.ATTRIBUTES}
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        for data in self._data.values():
            data.parse_kwargs(**kwargs)

    def format_data(self):
        json_data = {}
        for data in self._data.values():
            value = data.format_data()
            if value:
                json_data.update(value)
        return json_data

if __name__ == "__main__":
    d = {'id'      : 'my_id',
         'name'    : 'my_name',
         'type'    : 'my_type',
         'objects' : 'my_objects',
         'literals': 'my_literals'}

    x = NetworkGroups(fmc=mock.Mock(), **d)
    print(x.format_data())
