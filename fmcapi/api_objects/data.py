from unittest import mock
from abc import ABCMeta, abstractmethod
from fmcapi.api_objects.helper_functions import get_networkaddress_type

#
# This base class would be used to manage all the keys and their respective values
# If anything "special" is required for a specific key, then the format_data or parse_kwargs can be overridden in the
# child class
#


class BaseData(object):

    @property
    def key(self):
        return self.__class__.__name__.lower()

    def __init__(self, **kwargs):
        print(f'Init for {self.key}')
        self.value = None
        self.parse_kwargs(**kwargs)

    def format_data(self):
        print(f'Formatting data for {self.key}')
        if self.value:
            return {self.key: self.value}
        return {}

    def parse_kwargs(self, **kwargs):
        print(f'Parsing kwargs for {self.key}')
        if self.key in kwargs:
            self.value = kwargs[self.key]


#
# The data classes only need to define what is different, which in most cases is nothing! But if you
# need to do some special processing in any method you can override here
#


class Id(BaseData):
    ...


class Name(BaseData):
    ...


class Type(BaseData):
    ...


class Objects(BaseData):
    ...


class Literals(BaseData):

    # For example, lets override the key name when the json is built
    def format_data(self):
        print(f'Formatting data for {self.key}')
        if self.value:
            return {"changed_key_name": self.value}
        return {}


class Value(BaseData):
    ...


class Description(BaseData):
    ...


#
# This base class would be used to manage all the API operations (which is your APIClassTemplate now)
# If anything "special" is required for a specific operation, then it can be overridden in the child class
#  The abstract method enforce that the methods must be overridden in the child class
#

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
        # This loads all the data classes as defined in the keys
        self._data = {data().key: data() for data in self.keys}
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        for data in self._data.values():
            data.parse_kwargs(**kwargs)

    def format_data(self):
        json_data = {}
        for data in self._data.values():
            json_data.update(data.format_data())
        return json_data


#
# Again the child classes only need to define what is different, which in most cases will be just the absract methods
#


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
