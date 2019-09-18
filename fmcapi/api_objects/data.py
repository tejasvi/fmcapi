from unittest import mock
from abc import ABCMeta, abstractmethod
from fmcapi.api_objects.helper_functions import get_networkaddress_type


class BaseData(metaclass=ABCMeta):

    @property
    @abstractmethod
    def key(self):
        return ''

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
    def key(self):
        return 'id'


class Name(BaseData):
    @property
    def key(self):
        return 'name'


class Type(BaseData):
    @property
    def key(self):
        return 'type'


class Objects(BaseData):
    @property
    def key(self):
        return 'objects'


class Literals(BaseData):
    @property
    def key(self):
        return 'literals'


class Value(BaseData):
    @property
    def key(self):
        return 'value'


class Description(BaseData):
    @property
    def key(self):
        return 'description'


class BaseAPI(metaclass=ABCMeta):

    @property
    @abstractmethod
    def url_suffix(self):
        return ''

    @property
    @abstractmethod
    def required_for_post(self):
        return []

    @property
    @abstractmethod
    def keys(self):
        return []

    @property
    @abstractmethod
    def type(self):
        return ''

    def __init__(self, fmc, **kwargs):
        self._data = {data().key: data() for data in self.keys}
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


class NetworkGroups(BaseAPI):
    """
    The NetworkGroups Object in the FMC.
    """

    @property
    def url_suffix(self):
        return '/object/networkgroups'

    @property
    def required_for_post(self):
        return ['name']

    @property
    def keys(self):
        return [Id, Name, Type, Objects, Literals]

    @property
    def type(self):
        return 'NetworkGroup'


class Hosts(BaseAPI):
    """
    The Hosts Object in the FMC.
    """

    @property
    def url_suffix(self):
        return '/object/hosts'

    @property
    def required_for_post(self):
        return ['id', 'name', 'value']

    @property
    def keys(self):
        return [Id, Name, Value, Description]

    @property
    def type(self):
        return get_networkaddress_type(self._data['value'].value)


if __name__ == "__main__":

    d = {'id': 'my_id',
         'name': 'my_name',
         'type': 'my_type',
         'objects': 'my_objects',
         'literals': 'my_literals'}

    x = NetworkGroups(fmc=mock.Mock(), **d)
    print(x.format_data())

    d = {'id': 'my_id',
         'name': 'my_name',
         'value': '10.0.0.1',
         'description': 'my_description'}

    x = Hosts(fmc=mock.Mock(), **d)
    print(x.format_data())
    print(x.type)
