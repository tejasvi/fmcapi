from unittest import mock
from abc import ABCMeta, abstractmethod

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate


class BaseData(object):

    @property
    @abstractmethod
    def key(self):
        pass

    def __init__(self, **kwargs):
        print(f'Init for {self.key}')
        self.value = None
        self.parse_kwargs(**kwargs)

    def format_data(self):
        print(f'Formatting data for {self.key}')
        if self.value:
            return {self.key: self.value}
        return None

    def parse_kwargs(self, **kwargs):
        print(f'Parsing kwargs for {self.key}')
        if self.key in kwargs:
            self.value = kwargs[self.key]


class Id(BaseData):
    @property
    @abstractmethod
    def key(self):
        return 'id'


class Name(BaseData):
    @property
    @abstractmethod
    def key(self):
        return 'name'


class Type(BaseData):
    @property
    @abstractmethod
    def key(self):
        return 'type'


class Objects(BaseData):
    @property
    @abstractmethod
    def key(self):
        return 'objects'


class Literals(BaseData):
    @property
    @abstractmethod
    def key(self):
        return 'literals'


class BaseAPI(object):
    pass


class NetworkGroups(APIClassTemplate):
    """
    The NetworkGroups Object in the FMC.
    """

    URL_SUFFIX = '/object/networkgroups'

    REQUIRED_FOR_POST = ['name']

    KEYS = [Id, Name, Type, Objects, Literals]

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc)
        self.type = 'NetworkGroup'
        self._data = {data.key: data() for data in self.KEYS}
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
