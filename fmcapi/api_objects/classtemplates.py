"""Super class that is inherited by all API objects."""
from fmcapi.api_objects.helper_functions import syntax_correcter
from abc import ABCMeta, abstractmethod, ABC
import json
import logging

logging.debug(f"In the {__name__} module.")


class BaseData(object):
    """
    The BaseData base class is used to manage all the keys and their respective values.  If anything "special" is
    required for a specific key, then the format_data or parse_kwargs can be overridden in the child class.
    """

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


class Id(BaseData, ABC):
    ...


class Name(BaseData, ABC):
    ...


class Type(BaseData, ABC):
    ...


class Objects(BaseData, ABC):
    ...


class Literals(BaseData, ABC):
    ...


class Value(BaseData, ABC):
    ...


class Description(BaseData, ABC):
    ...


class Limit(BaseData, ABC):
    ...


class APIClassTemplate(metaclass=ABCMeta):
    """
    This class is the base framework for most of the objects in the FMC.
    """

    FILTER_BY_NAME = False
    URL = ''

    @property
    @abstractmethod
    def first_supported_fmc_version(self):
        return '6.1'

    @property
    @abstractmethod
    def url_suffix(self):
        return ''

    @property
    @abstractmethod
    def required_for_post(self):
        return ['name']

    @property
    @abstractmethod
    def required_for_put(self):
        return ['id']

    @property
    @abstractmethod
    def required_for_delete(self):
        return ['id']

    @property
    @abstractmethod
    def required_for_get(self):
        return []

    @property
    @abstractmethod
    def valid_characters_for_name(self):
        return """"[.\w\d_\-]"""

    @property
    @abstractmethod
    def keys(self):
        return []

    @property
    @abstractmethod
    def type(self):
        return ''

    @property
    @abstractmethod
    def limit(self):
        if not self.key:
            self.limit = kwargs['limit']
        else:
            self.limit = self.fmc.limit

    @property
    @abstractmethod
    def name(self):
        orginal_name = self.value
        self.value = syntax_correcter(orginal_name, permitted_syntax=self.valid_characters_for_name)
        if self.value != orginal_name:
            logging.info(f"Adjusting provided name to '{self.value}' due to invalid characters.")


    @property
    def show_json(self):
        return self.format_data()

    def __init__(self, fmc, **kwargs):
        # This loads all the data classes as defined in the keys
        logging.debug("In __init__() for APIClassTemplate class.")
        self.fmc = fmc
        self._data = {data().key: data() for data in self.keys}
        self.parse_kwargs(**kwargs)
        self.URL = f'{self.fmc.configuration_url}{self.url_suffix}'

    def parse_kwargs(self, **kwargs):
        logging.debug("In parse_kwargs() for APIClassTemplate class.")
        for data in self._data.values():
            data.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for APIClassTemplate class.")
        json_data = {}
        for data in self._data.values():
            json_data.update(data.format_data())
        return json_data

    def parse_kwargs_old(self, **kwargs):
        if 'offset' in kwargs:
            self.offset = kwargs['offset']
        if 'name' in kwargs:
            self.name = syntax_correcter(kwargs['name'], permitted_syntax=self.valid_characters_for_name)
            if self.name != kwargs['name']:
                logging.info(f"Adjusting name '{kwargs['name']}' to '{self.name}' due to invalid characters.")
        if 'description' in kwargs:
            self.description = kwargs['description']
        else:
            self.description = 'Created by fmcapi.'
        if 'metadata' in kwargs:
            self.metadata = kwargs['metadata']
        if 'overridable' in kwargs:
            self.overridable = kwargs['overridable']
        else:
            self.overridable = False
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'links' in kwargs:
            self.links = kwargs['links']
        if 'paging' in kwargs:
            self.paging = kwargs['paging']
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'items' in kwargs:
            self.items = kwargs['items']
        if 'dry_run' in kwargs:
            self.dry_run = kwargs['dry_run']
        else:
            self.dry_run = False

    def valid_for_get(self):
        logging.debug("In valid_for_get() for APIClassTemplate class.")
        if self.required_for_get == ['']:
            return True
        for item in self.required_for_get:
            if item not in self.__dict__:
                return False
        return True

    def get(self, **kwargs):
        """
        If no self.name or self.id exists then return a full listing of all objects of this type.
        Otherwise set "expanded=true" results for this specific object.
        :return:
        """
        logging.debug("In get() for APIClassTemplate class.")
        self.parse_kwargs(**kwargs)
        if self.fmc.serverVersion < self.first_supported_fmc_version:
            logging.error(f'Your FMC version, {self.fmc.serverVersion} does not support GET of this feature.')
            return {'items': []}
        if self.valid_for_get():
            if 'id' in self.__dict__:
                url = f'{self.URL}/{self.id}'
                if self.dry_run:
                    logging.info('Dry Run enabled.  Not actually sending to FMC.  Here is what would have been sent:')
                    logging.info('\tMethod = GET')
                    logging.info(f'\tURL = {self.URL}')
                    return False
                response = self.fmc.send_to_api(method='get', url=url)
                self.parse_kwargs(**response)
                if 'name' in self.__dict__:
                    logging.info(f'GET success. Object with name: "{self.name}" and id: "{self.id}" fetched from FMC.')
                else:
                    logging.info(f'GET success. Object with id: "{self.id}" fetched from FMC.')
            elif 'name' in self.__dict__:
                if self.FILTER_BY_NAME:
                    url = f'{self.URL}?name={self.name}&expanded=true'
                else:
                    url = f'{self.URL}?expanded=true'
                    if 'limit' in self.__dict__:
                        url = f'{url}&limit={self.limit}'
                    if 'offset' in self.__dict__:
                        url = f'{url}&offset={self.offset}'
                response = self.fmc.send_to_api(method='get', url=url)
                if 'items' not in response:
                    response['items'] = []
                for item in response['items']:
                    if 'name' in item:
                        if item['name'] == self.name:
                            self.id = item['id']
                            self.parse_kwargs(**item)
                            logging.info(f'GET success. Object with name: "{self.name}" and id: "{self.id}" '
                                         f'fetched from FMC.')
                            return item
                    else:
                        logging.warning(f'No "name" attribute associated with this item to check against {self.name}.')
                if 'id' not in self.__dict__:
                    logging.warning(f"\tGET query for {self.name} is not found.\n\t\tResponse: {json.dumps(response)}")
            else:
                logging.info("GET query for object with no name or id set.  "
                             "Returning full list of these object types instead.")
                url = f'{self.URL}?expanded=true&limit={self.limit}'
                if self.dry_run:
                    logging.info('Dry Run enabled.  Not actually sending to FMC.  Here is what would have been sent:')
                    logging.info('\tMethod = GET')
                    logging.info(f'\tURL = {self.URL}')
                    return False
                response = self.fmc.send_to_api(method='get', url=url)
            if 'items' not in response:
                response['items'] = []
            return response
        else:
            logging.warning("get() method failed due to failure to pass valid_for_get() test.")
            return False

    def valid_for_post(self):
        logging.debug("In valid_for_post() for APIClassTemplate class.")
        for item in self.required_for_post:
            if item not in self.__dict__:
                return False
        return True

    def post(self, **kwargs):
        logging.debug("In post() for APIClassTemplate class.")
        if self.fmc.serverVersion < self.first_supported_fmc_version:
            logging.error(f'Your FMC version, {self.fmc.serverVersion} does not support POST of this feature.')
            return False
        if 'id' in self.__dict__:
            logging.info("ID value exists for this object.  Redirecting to put() method.")
            self.put()
        else:
            if self.valid_for_post():
                if self.dry_run:
                    logging.info('Dry Run enabled.  Not actually sending to FMC.  Here is what would have been sent:')
                    logging.info('\tMethod = POST')
                    logging.info(f'\tURL = {self.URL}')
                    logging.info(f'\tJSON = {self.format_data()}')
                    return False
                response = self.fmc.send_to_api(method='post', url=self.URL, json_data=self.format_data())
                if response:
                    self.parse_kwargs(**response)
                    if 'name' in self.__dict__ and 'id' in self.__dict__:
                        logging.info(f'POST success. Object with name: "{self.name}" and id: "{id}" created in FMC.')
                    else:
                        logging.info('POST success but no "id" or "name" values in API response.')
                else:
                    logging.warning('POST failure.  No data in API response.')
                return response
            else:
                logging.warning("post() method failed due to failure to pass valid_for_post() test.")
                return False

    def valid_for_put(self):
        logging.debug("In valid_for_put() for APIClassTemplate class.")
        for item in self.required_for_put:
            if item not in self.__dict__:
                return False
        return True

    def put(self, **kwargs):
        logging.debug("In put() for APIClassTemplate class.")
        self.parse_kwargs(**kwargs)
        if self.fmc.serverVersion < self.first_supported_fmc_version:
            logging.error(f'Your FMC version, {self.fmc.serverVersion} does not support PUT of this feature.')
            return False
        if self.valid_for_put():
            url = f'{self.URL}/{self.id}'
            if self.dry_run:
                logging.info('Dry Run enabled.  Not actually sending to FMC.  Here is what would have been sent:')
                logging.info('\tMethod = PUT')
                logging.info(f'\tURL = {self.URL}')
                logging.info(f'\tJSON = {self.format_data()}')
                return False
            response = self.fmc.send_to_api(method='put', url=url, json_data=self.format_data())
            self.parse_kwargs(**response)
            if 'name' in self.__dict__:
                logging.info(f'PUT success. Object with name: "{self.name}" and id: "{self.id}" updated in FMC.')
            else:
                logging.info(f'PUT success. Object with id: "{self.id}" updated in FMC.')
            return response
        else:
            logging.warning("put() method failed due to failure to pass valid_for_put() test.")
            return False

    def valid_for_delete(self):
        logging.debug("In valid_for_delete() for APIClassTemplate class.")
        for item in self.required_for_delete:
            if item not in self.__dict__:
                return False
        return True

    def delete(self, **kwargs):
        logging.debug("In delete() for APIClassTemplate class.")
        self.parse_kwargs(**kwargs)
        if self.fmc.serverVersion < self.first_supported_fmc_version:
            logging.error(f'Your FMC version, {self.fmc.serverVersion} does not support DELETE of this feature.')
            return False
        if self.valid_for_delete():
            url = f'{self.URL}/{self.id}'
            if self.dry_run:
                logging.info('Dry Run enabled.  Not actually sending to FMC.  Here is what would have been sent:')
                logging.info('\tMethod = DELETE')
                logging.info(f'\tURL = {self.URL}')
                logging.info(f'\tJSON = {self.format_data()}')
                return False
            response = self.fmc.send_to_api(method='delete', url=url, json_data=self.format_data())
            if not response:
                return None
            self.parse_kwargs(**response)
            if 'name' in self.name:
                logging.info(f'DELETE success. Object with name: "{self.name}" and id: "{self.id}" deleted in FMC.')
            else:
                logging.info(f'DELETE success. Object id: "{self.id}" deleted in FMC.')
            return response
        else:
            logging.warning("delete() method failed due to failure to pass valid_for_delete() test.")
            return False
