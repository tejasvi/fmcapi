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


class accessPolicy(BaseData, ABC):
    ...


class action(BaseData, ABC):
    ...


class activeMACAddress(BaseData, ABC):
    ...


class appConditions(BaseData, ABC):
    ...


class applications(BaseData, ABC):
    ...


class arpConfig(BaseData, ABC):
    ...


class authenticationMethod(BaseData, ABC):
    ...


class bridgeGroupId(BaseData, ABC):
    ...


class checksumURL(BaseData, ABC):
    ...


class code(BaseData, ABC):
    ...


class conditions(BaseData, ABC):
    ...


class containerType(BaseData, ABC):
    ...


class continentId(BaseData, ABC):
    ...


class continents(BaseData, ABC):
    ...


class continentUUID(BaseData, ABC):
    ...


class countries(BaseData, ABC):
    ...


class dataSize(BaseData, ABC):
    ...


class defaultAction(BaseData, ABC):
    ...


class defaultdomain(BaseData, ABC):
    ...


class description(BaseData, ABC):
    ...


class destinationInterface(BaseData, ABC):
    ...


class destinationNetworks(BaseData, ABC):
    ...


class destinationPorts(BaseData, ABC):
    ...


class destinationZones(BaseData, ABC):
    ...


class diffieHellmanGroup(BaseData, ABC):
    ...


class dns(BaseData, ABC):
    ...


class dnsResolution(BaseData, ABC):
    ...


class dnsservers(BaseData, ABC):
    ...


class enableAntiSpoofing(BaseData, ABC):
    ...


class enabled(BaseData, ABC):
    ...


class enableDNSLookup(BaseData, ABC):
    ...


class encryption(BaseData, ABC):
    ...


class encryptionAlgorithms(BaseData, ABC):
    ...


class erspanFlowId(BaseData, ABC):
    ...


class erspanSourceIP(BaseData, ABC):
    ...


class espEncryption(BaseData, ABC):
    ...


class espHash(BaseData, ABC):
    ...


class etherChannelId(BaseData, ABC):
    ...


class failoverActiveMac(BaseData, ABC):
    ...


class failoverStandyMac(BaseData, ABC):
    ...


class fallThrough(BaseData, ABC):
    ...


class feedURL(BaseData, ABC):
    ...


class filePolicy(BaseData, ABC):
    ...


class forceBreak(BaseData, ABC):
    ...


class fqName(BaseData, ABC):
    ...


class fragmentReassembly(BaseData, ABC):
    ...


class frequency(BaseData, ABC):
    ...


class ftdHABoostrap(BaseData, ABC):
    ...


class gateway(BaseData, ABC):
    ...


class hardware(BaseData, ABC):
    ...


class hash(BaseData, ABC):
    ...


class healthPolicy(BaseData, ABC):
    ...


class healthStatus(BaseData, ABC):
    ...


class hostName(BaseData, ABC):
    ...


class icmpType(BaseData, ABC):
    ...


class id(BaseData, ABC):
    ...


class ifname(BaseData, ABC):
    ...


class integrityAlgorithms(BaseData, ABC):
    ...


class interfaceInOriginalDestination(BaseData, ABC):
    ...


class interfaceInTranslatedNetwork(BaseData, ABC):
    ...


class interfaceInTranslatedSource(BaseData, ABC):
    ...


class interfaceIpv6(BaseData, ABC):
    ...


class interfaceMode(BaseData, ABC):
    ...


class interfaceName(BaseData, ABC):
    ...


class interfaceObjects(BaseData, ABC):
    ...


class interfaces(BaseData, ABC):
    ...


class ipAddress(BaseData, ABC):
    ...


class ipsPolicy(BaseData, ABC):
    ...


class ipv4(BaseData, ABC):
    ...


class ipv4Configuration(BaseData, ABC):
    ...


class ipv6(BaseData, ABC):
    ...


class ipv6Configuration(BaseData, ABC):
    ...


class iseId(BaseData, ABC):
    ...


class iso2(BaseData, ABC):
    ...


class iso3(BaseData, ABC):
    ...


class isPartofContainer(BaseData, ABC):
    ...


class isTunneled(BaseData, ABC):
    ...


class lacpMode(BaseData, ABC):
    ...


class license_caps(BaseData, ABC):
    ...


class lifetimeInSeconds(BaseData, ABC):
    ...


class literals(BaseData, ABC):
    ...


class loadBalancing(BaseData, ABC):
    ...


class logBegin(BaseData, ABC):
    ...


class logEnd(BaseData, ABC):
    ...


class logFiles(BaseData, ABC):
    ...


class maclLearn(BaseData, ABC):
    ...


class macTable(BaseData, ABC):
    ...


class managementOnly(BaseData, ABC):
    ...


class maxActivePhysicalInterface(BaseData, ABC):
    ...


class members(BaseData, ABC):
    ...


class metricValue(BaseData, ABC):
    ...


class minActivePhysicalInterface(BaseData, ABC):
    ...


class mode(BaseData, ABC):
    ...


class model(BaseData, ABC):
    ...


class modelId(BaseData, ABC):
    ...


class modelNumber(BaseData, ABC):
    ...


class modelType(BaseData, ABC):
    ...


class monitorAddress(BaseData, ABC):
    ...


class monitorForFailures(BaseData, ABC):
    ...


class MTU(BaseData, ABC):
    ...


class name(BaseData, ABC):
    ...


class natID(BaseData, ABC):
    ...


class natType(BaseData, ABC):
    ...


class netToNet(BaseData, ABC):
    ...


class noOfPackets(BaseData, ABC):
    ...


class noProxyArp(BaseData, ABC):
    ...


class objects(BaseData, ABC):
    ...


class originalDestination(BaseData, ABC):
    ...


class originalDestinationPort(BaseData, ABC):
    ...


class originalNetwork(BaseData, ABC):
    ...


class originalPort(BaseData, ABC):
    ...


class originalSource(BaseData, ABC):
    ...


class originalSourceNetworks(BaseData, ABC):
    ...


class originalSourcePort(BaseData, ABC):
    ...


class overridable(BaseData, ABC):
    ...


class overrides(BaseData, ABC):
    ...


class overrideTargetId(BaseData, ABC):
    ...


class patOptions(BaseData, ABC):
    ...


class physicalInterface(BaseData, ABC):
    ...


class policy(BaseData, ABC):
    ...


class port(BaseData, ABC):
    ...


class prfIntegrityAlgorithms(BaseData, ABC):
    ...


class primary(BaseData, ABC):
    ...


class primaryInterface(BaseData, ABC):
    ...


class priority(BaseData, ABC):
    ...


class protocol(BaseData, ABC):
    ...


class pushUpgradeFileOnly(BaseData, ABC):
    ...


class realm(BaseData, ABC):
    ...


class realmUuid(BaseData, ABC):
    ...


class redundantId(BaseData, ABC):
    ...


class regKey(BaseData, ABC):
    ...


class retries(BaseData, ABC):
    ...


class routeLookup(BaseData, ABC):
    ...


class routeTracking(BaseData, ABC):
    ...


class secondary(BaseData, ABC):
    ...


class secondaryInterface(BaseData, ABC):
    ...


class securityZone(BaseData, ABC):
    ...


class selectedInterfaces(BaseData, ABC):
    ...


class selectedNetworks(BaseData, ABC):
    ...


class sendEventsToFMC(BaseData, ABC):
    ...


class serviceProtocol(BaseData, ABC):
    ...


class slaId(BaseData, ABC):
    ...


class sourceInterface(BaseData, ABC):
    ...


class sourceNetworks(BaseData, ABC):
    ...


class sourcePorts(BaseData, ABC):
    ...


class sourceZones(BaseData, ABC):
    ...


class standyMACAddress(BaseData, ABC):
    ...


class subIntfId(BaseData, ABC):
    ...


class sw_version(BaseData, ABC):
    ...


class tag(BaseData, ABC):
    ...


class targets(BaseData, ABC):
    ...


class threshold(BaseData, ABC):
    ...


class timeout(BaseData, ABC):
    ...


class tos(BaseData, ABC):
    ...


class translatedDestination(BaseData, ABC):
    ...


class translatedDestinationPort(BaseData, ABC):
    ...


class translatedNetwork(BaseData, ABC):
    ...


class translatedPort(BaseData, ABC):
    ...


class translatedSource(BaseData, ABC):
    ...


class translatedSourcePort(BaseData, ABC):
    ...


class type(BaseData, ABC):
    ...


class unidirectional(BaseData, ABC):
    ...


class updateFrequency(BaseData, ABC):
    ...


class upgadePackage(BaseData, ABC):
    ...


class url(BaseData, ABC):
    ...


class urls(BaseData, ABC):
    ...


class value(BaseData, ABC):
    ...


class variableSet(BaseData, ABC):
    ...


class vlanId(BaseData, ABC):
    ...


class vlanTags(BaseData, ABC):
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
