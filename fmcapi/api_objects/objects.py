"""
This module contains the "object" class objects that represent the various objects in the FMC.
"""

from .api_template import *
from .helper_functions import *
from .api_template import *
from .devices import *
from .misc import *
from .objects import *
from .policy import *


class IPAddresses(APIClassTemplate):
    """
    The IPAddresses Object in the FMC.
    """

    URL_SUFFIX = '/object/networkaddresses'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPAddresses class.")
        self.parse_kwargs(**kwargs)

    def post(self):
        logging.info('POST method for API for IPAddresses not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for IPAddresses not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for IPAddresses not supported.')
        pass


class IPHost(APIClassTemplate):
    """
    The Host Object in the FMC.
    """

    URL_SUFFIX = '/object/hosts'
    REQUIRED_FOR_POST = ['name', 'value']
    REQUIRED_FOR_PUT = ['id', 'name', 'value']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPHost class.")
        self.parse_kwargs(**kwargs)
        if 'value' in kwargs:
            value_type = get_networkaddress_type(kwargs['value'])
            if value_type == 'range':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPHost function.".format(kwargs['value'], value_type))
            if value_type == 'network':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPHost function.".format(kwargs['value'], value_type))
            if validate_ip_bitmask_range(value=kwargs['value'], value_type=value_type):
                self.value = kwargs['value']
            else:
                logging.error("Provided value, {}, has an error with the IP address(es).".format(kwargs['value']))

    def format_data(self):
        logging.debug("In format_data() for IPHost class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'value' in self.__dict__:
            json_data['value'] = self.value
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IPHost class.")
        if 'value' in kwargs:
            self.value = kwargs['value']


class IPNetwork(APIClassTemplate):
    """
    The Network Object in the FMC.
    """

    URL_SUFFIX = '/object/networks'
    REQUIRED_FOR_POST = ['name', 'value']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPNetwork class.")
        self.parse_kwargs(**kwargs)
        if 'value' in kwargs:
            value_type = get_networkaddress_type(kwargs['value'])
            if value_type == 'range':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPNetwork function.".format(kwargs['value'], value_type))
            if value_type == 'host':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPNetwork function.".format(kwargs['value'], value_type))
            if validate_ip_bitmask_range(value=kwargs['value'], value_type=value_type):
                self.value = kwargs['value']
            else:
                logging.error("Provided value, {}, has an error with the IP address(es).".format(kwargs['value']))

    def format_data(self):
        logging.debug("In format_data() for IPNetwork class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'value' in self.__dict__:
            json_data['value'] = self.value
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IPNetwork class.")
        if 'value' in kwargs:
            self.value = kwargs['value']


class IPRange(APIClassTemplate):
    """
    The Range Object in the FMC.
    """

    URL_SUFFIX = '/object/ranges'
    REQUIRED_FOR_POST = ['name', 'value']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPRange class.")
        self.parse_kwargs(**kwargs)
        if 'value' in kwargs:
            value_type = get_networkaddress_type(kwargs['value'])
            if value_type == 'host':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPRange function.".format(kwargs['value'], value_type))
            if value_type == 'network':
                logging.warning("value, {}, is of type {}.  Limited functionality for this object due to it being "
                                "created via the IPRange function.".format(kwargs['value'], value_type))
            if validate_ip_bitmask_range(value=kwargs['value'], value_type=value_type):
                self.value = kwargs['value']
            else:
                logging.error("Provided value, {}, has an error with the IP address(es).".format(kwargs['value']))

    def format_data(self):
        logging.debug("In format_data() for IPRange class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'value' in self.__dict__:
            json_data['value'] = self.value
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IPRange class.")
        if 'value' in kwargs:
            self.value = kwargs['value']


class NetworkGroup(APIClassTemplate):
    """
    The NetworkGroup Object in the FMC.
    """

    URL_SUFFIX = '/object/networkgroups'

    # Technically you can have objects OR literals but I'm not set up for "OR" logic, yet.
    REQUIRED_FOR_POST = ['name', 'objects']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for NetworkGroup class.")
        self.parse_kwargs(**kwargs)
        self.type = 'NetworkGroup'

    def format_data(self):
        logging.debug("In format_data() for NetworkGroup class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'objects' in self.__dict__:
            json_data['objects'] = self.objects
        if 'literals' in self.__dict__:
            json_data['literals'] = self.literals
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for NetworkGroup class.")
        if 'objects' in kwargs:
            self.objects = kwargs['objects']
        if 'literals' in kwargs:
            self.literals = kwargs['literals']

    def named_networks(self, action, name=''):
        logging.debug("In named_networks() for NetworkGroup class.")
        if action == 'add':
            net1 = IPAddresses(fmc=self.fmc)
            response = net1.get()
            if 'items' in response:
                new_net = None
                for item in response['items']:
                    if item['name'] == name:
                        new_net = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                        break
                if new_net is None:
                    logging.warning('Network "{}" is not found in FMC.  Cannot add to NetworkGroup.'.format(name))
                else:
                    if 'objects' in self.__dict__:
                        duplicate = False
                        for obj in self.objects:
                            if obj['name'] == new_net['name']:
                                duplicate = True
                                break
                        if not duplicate:
                            self.objects.append(new_net)
                            logging.info('Adding "{}" to NetworkGroup.'.format(name))
                    else:
                        self.objects = [new_net]
                        logging.info('Adding "{}" to NetworkGroup.'.format(name))
        elif action == 'remove':
            if 'objects' in self.__dict__:
                objects_list = []
                for obj in self.objects:
                    if obj['name'] != name:
                        objects_list.append(obj)
                self.objects = objects_list
                logging.info('Removed "{}" from NetworkGroup.'.format(name))
            else:
                logging.info("This NetworkGroup has no named_networks.  Nothing to remove.")
        elif action == 'clear':
            if 'objects' in self.__dict__:
                del self.objects
                logging.info('All named_networks removed from this NetworkGroup.')

    def unnamed_networks(self, action, value=''):
        logging.debug("In unnamed_networks() for NetworkGroup class.")
        new_literal = []
        if action == 'add':
            if value == '':
                logging.error('Value assignment required to add unamed_network to NetworkGroup.')
                return
            literal_type = get_networkaddress_type(value=value)
            if literal_type == 'host' or literal_type == 'network':
                new_literal = {'value': value, 'type': literal_type}
            elif literal_type == 'range':
                logging.error('Ranges are not supported as unnamed_networks in a NetworkGroup.')
            else:
                logging.error('Value "{}" provided is not in a recognizable format.'.format(value))
                return
            if 'literals' in self.__dict__:
                duplicate = False
                for obj in self.literals:
                    if obj['value'] == new_literal['value']:
                        duplicate = True
                        break
                if not duplicate:
                    self.literals.append(new_literal)
                    logging.info('Adding "{}" to NetworkGroup.'.format(value))
            else:
                self.literals = [new_literal]
                logging.info('Adding "{}" to NetworkGroup.'.format(value))
        elif action == 'remove':
            if 'literals' in self.__dict__:
                literals_list = []
                for obj in self.literals:
                    if obj['value'] != value:
                        literals_list.append(obj)
                self.literals = literals_list
                logging.info('Removed "{}" from NetworkGroup.'.format(value))
            else:
                logging.info("This NetworkGroup has no unnamed_networks.  Nothing to remove.")
        elif action == 'clear':
            if 'literals' in self.__dict__:
                del self.literals
                logging.info('All unnamed_networks removed from this NetworkGroup.')


class AnyProtocolPortObjects(APIClassTemplate):
    """
    The AnyProtocolPortObjects Object in the FMC.
    """

    URL_SUFFIX = '/object/anyprotocolportobjects'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for AnyProtocolPortObjects class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for AnyProtocolPortObjects class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrideTargetId' in self.__dict__:
            json_data['overrideTargetId'] = self.overrideTargetId
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for AnyProtocolPortObjects class.")

    def post(self):
        logging.info('POST method for API for AnyProtocolPortObjects not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for AnyProtocolPortObjects not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for AnyProtocolPortObjects not supported.')
        pass


class ApplicationCategory(APIClassTemplate):
    """
    The ApplicationCategory Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationcategories'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationCategory class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationCategory class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationCategory class.")

    def post(self):
        logging.info('POST method for API for ApplicationCategory not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationCategory not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationCategory not supported.')
        pass


class ApplicationFilter(APIClassTemplate):
    """
    The ApplicationFilter Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationfilters'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationFilter class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationFilter class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'appConditions' in self.__dict__:
            json_data['appConditions'] = self.appConditions
        if 'applications' in self.__dict__:
            json_data['applications'] = self.applications
        if 'conditions' in self.__dict__:
            json_data['conditions'] = self.conditions
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationFilter class.")

    def post(self):
        logging.info('POST method for API for ApplicationFilter not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationFilter not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationFilter not supported.')
        pass


class ApplicationProductivity(APIClassTemplate):
    """
    The ApplicationProductivity Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationproductivities'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationProductivity class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationProductivity class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationProductivity class.")

    def post(self):
        logging.info('POST method for API for ApplicationProductivity not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationProductivity not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationProductivity not supported.')
        pass


class ApplicationRisk(APIClassTemplate):
    """
    The ApplicationRisk Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationrisks'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationRisk class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationRisk class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationRisk class.")

    def post(self):
        logging.info('POST method for API for ApplicationRisk not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationRisk not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationRisk not supported.')
        pass


class Application(APIClassTemplate):
    """
    The Application Object in the FMC.
    """

    URL_SUFFIX = '/object/applications'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Application class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for Application class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Application class.")
        if 'appProductivity' in kwargs:
            self.appProductivity = kwargs['appProductivity']
        if 'appCategories' in kwargs:
            self.appCategories = kwargs['appCategories']
        if 'appTags' in kwargs:
            self.appTags = kwargs['appTags']
        if 'appId' in kwargs:
            self.appId = kwargs['appId']
        if 'risk' in kwargs:
            self.risk = kwargs['risk']
        if 'applicationTypes' in kwargs:
            self.applicationTypes = kwargs['applicationTypes']

    def post(self):
        logging.info('POST method for API for Application not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Application not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Application not supported.')
        pass


class ApplicationTag(APIClassTemplate):
    """
    The ApplicationTag Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationtags'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationTag class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationTag class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationTag class.")

    def post(self):
        logging.info('POST method for API for ApplicationTag not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationTag not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationTag not supported.')
        pass


class ApplicationType(APIClassTemplate):
    """
    The ApplicationType Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationtypes'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationTag class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicationType class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationType class.")

    def post(self):
        logging.info('POST method for API for ApplicationType not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationType not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationType not supported.')
        pass


class CertEnrollment(APIClassTemplate):
    """
    The CertEnrollment Object in the FMC.
    """

    URL_SUFFIX = '/object/certenrollments'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for CertEnrollment class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for CertEnrollment class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for CertEnrollment class.")

    def post(self):
        logging.info('POST method for API for CertEnrollment not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for CertEnrollment not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for CertEnrollment not supported.')
        pass


class SLAMonitor(APIClassTemplate):
    """
    The SLAMonitor Object in the FMC.
    """
    URL_SUFFIX = '/object/slamonitors'
    REQUIRED_FOR_POST = ['name', 'slaId', 'monitorAddress', 'interfaceObjects', 'type']
    REQUIRED_FOR_PUT = ['id','type']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SLAMonitor class.")
        self.parse_kwargs(**kwargs)
        self.type = "SLAMonitor"

    def format_data(self):
        logging.debug("In format_data() for SLAMonitor class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'timeout' in self.__dict__:
            json_data['timeout'] = self.timeout
        if 'threshold' in self.__dict__:
            json_data['threshold'] = self.threshold
        if 'frequency' in self.__dict__:
            json_data['frequency'] = self.frequency
        if 'slaId' in self.__dict__:
            json_data['slaId'] = self.slaId
        if 'dataSize' in self.__dict__:
            json_data['dataSize'] = self.dataSize
        if 'tos' in self.__dict__:
            json_data['tos'] = self.tos
        if 'noOfPackets' in self.__dict__:
            json_data['noOfPackets'] = self.noOfPackets
        if 'monitorAddress' in self.__dict__:
            json_data['monitorAddress'] = self.monitorAddress
        if 'interfaceObjects' in self.__dict__:
            json_data['interfaceObjects'] = self.interfaceObjects
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SLAMonitor class.")
        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
        if 'threshold' in kwargs:
             self.securityZone = kwargs['threshold']
        if 'frequency' in kwargs:
            self.frequency = kwargs['frequency']
        if 'slaId' in kwargs:
            self.slaId = kwargs['slaId']
        if 'dataSize' in kwargs:
            self.dataSize = kwargs['dataSize']
        if 'tos' in kwargs:
            self.tos = kwargs['tos']
        if 'noOfPackets' in kwargs:
            self.noOfPackets = kwargs['noOfPackets']
        if 'monitorAddress' in kwargs:
            self.monitorAddress = kwargs['monitorAddress']
        if 'interfaceObjects' in kwargs:
            self.interfaceObjects = kwargs['interfaceObjects']
        if 'description' in kwargs:
            self.description = kwargs['description']

    def interfaces(self, names):
        logging.debug("In interfaces() for SLAMonitor class.")
        zones = []
        for name in names:
            #Supports passing list of str
            sz = SecurityZone(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                zones.append({'name': sz.name, 'id': sz.id, 'type': sz.type})
            else:
                logging.warning('Security Zone, "{}", not found.  Cannot add to SLAMonitor.'.format(name))
        if len(zones) != 0:
            #Make sure we found at least one zone
            self.interfaceObjects = zones
        else:
            logging.warning('No valid Security Zones found: "{}".  Cannot add to SLAMonitor.'.format(names))

class URL(APIClassTemplate):
    """
    The URL Object in the FMC.
    """

    URL_SUFFIX = '/object/urls'
    REQUIRED_FOR_POST = ['name', 'url']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for URL class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for URL class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'url' in self.__dict__:
            json_data['url'] = self.url
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for URL class.")
        if 'url' in kwargs:
            self.url = kwargs['url']


class URLGroup(APIClassTemplate):
    """
    The URLGroup Object in the FMC.
    """

    URL_SUFFIX = '/object/urlgroups'

    # Technically you can have objects OR literals but I'm not set up for "OR" logic, yet.
    REQUIRED_FOR_POST = ['name', 'objects']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for URLGroup class.")
        self.parse_kwargs(**kwargs)
        self.type = 'URLGroup'

    def format_data(self):
        logging.debug("In format_data() for URLGroup class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'objects' in self.__dict__:
            json_data['objects'] = self.objects
        if 'literals' in self.__dict__:
            json_data['literals'] = self.literals
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for URLGroup class.")
        if 'objects' in kwargs:
            self.objects = kwargs['objects']
        if 'literals' in kwargs:
            self.literals = kwargs['literals']

    def named_urls(self, action, name=''):
        logging.debug("In named_urls() for URLGroup class.")
        if action == 'add':
            url1 = URL(fmc=self.fmc)
            response = url1.get()
            if 'items' in response:
                new_url = None
                for item in response['items']:
                    if item['name'] == name:
                        new_url = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                        break
                if new_url is None:
                    logging.warning('URL "{}" is not found in FMC.  Cannot add to URLGroup.'.format(name))
                else:
                    if 'objects' in self.__dict__:
                        duplicate = False
                        for obj in self.objects:
                            if obj['name'] == new_url['name']:
                                duplicate = True
                                break
                        if not duplicate:
                            self.objects.append(new_url)
                            logging.info('Adding "{}" to URLGroup.'.format(name))
                    else:
                        self.objects = [new_url]
                        logging.info('Adding "{}" to URLGroup.'.format(name))
        elif action == 'remove':
            if 'objects' in self.__dict__:
                objects_list = []
                for obj in self.objects:
                    if obj['name'] != name:
                        objects_list.append(obj)
                self.objects = objects_list
                logging.info('Removed "{}" from URLGroup.'.format(name))
            else:
                logging.info("This URLGroup has no named_urls.  Nothing to remove.")
        elif action == 'clear':
            if 'objects' in self.__dict__:
                del self.objects
                logging.info('All named_urls removed from this URLGroup.')

    def unnamed_urls(self, action, value=''):
        logging.debug("In unnamed_urls() for URLGroup class.")
        if action == 'add':
            if value == '':
                logging.error('Value assignment required to add unamed_url to URLGroup.')
                return
            value_type = 'Url'
            new_literal = {'type': value_type, 'url': value}
            if 'literals' in self.__dict__:
                duplicate = False
                for obj in self.literals:
                    if obj['url'] == new_literal['url']:
                        duplicate = True
                        break
                if not duplicate:
                    self.literals.append(new_literal)
                    logging.info('Adding "{}" to URLGroup.'.format(value))
            else:
                self.literals = [new_literal]
                logging.info('Adding "{}" to URLGroup.'.format(value))
        elif action == 'remove':
            if 'literals' in self.__dict__:
                literals_list = []
                for obj in self.literals:
                    if obj['url'] != value:
                        literals_list.append(obj)
                self.literals = literals_list
                logging.info('Removed "{}" from URLGroup.'.format(value))
            else:
                logging.info("This URLGroup has no unnamed_urls.  Nothing to remove.")
        elif action == 'clear':
            if 'literals' in self.__dict__:
                del self.literals
                logging.info('All unnamed_urls removed from this URLGroup.')


class URLCategory(APIClassTemplate):
    """
    The URLCategory Object in the FMC.
    """

    URL_SUFFIX = '/object/urlcategories'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\.\(\) ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for URLCategory class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for URLCategory class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for URLCategory class.")

    def post(self):
        logging.info('POST method for API for URLCategory not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for URLCategory not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for URLCategory not supported.')
        pass


class VlanTag(APIClassTemplate):
    """
    The URL Object in the FMC.
    """

    URL_SUFFIX = '/object/vlantags'
    REQUIRED_FOR_POST = ['name', 'data']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for VlanTag class.")
        self.type = 'VlanTag'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for VlanTag class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'data' in self.__dict__:
            json_data['data'] = self.data
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for VlanTag class.")
        if 'data' in kwargs:
            self.data = kwargs['data']

    def vlans(self, start_vlan, end_vlan=''):
        logging.debug("In vlans() for VlanTag class.")
        start_vlan, end_vlan = validate_vlans(start_vlan=start_vlan, end_vlan=end_vlan)
        self.data = {'startTag': start_vlan, 'endTag': end_vlan}


class VlanGroupTag(APIClassTemplate):
    """
    The NetworkGroup Object in the FMC.
    """

    URL_SUFFIX = '/object/vlangrouptags'

    # Technically you can have objects OR literals but I'm not set up for "OR" logic, yet.
    REQUIRED_FOR_POST = ['name', 'objects']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for VlanGroupTag class.")
        self.parse_kwargs(**kwargs)
        self.type = 'VlanGroupTag'

    def format_data(self):
        logging.debug("In format_data() for VlanGroupTag class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'objects' in self.__dict__:
            json_data['objects'] = self.objects
        if 'literals' in self.__dict__:
            json_data['literals'] = self.literals
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for VlanGroupTag class.")
        if 'objects' in kwargs:
            self.objects = kwargs['objects']
        if 'literals' in kwargs:
            self.literals = kwargs['literals']

    def named_vlantags(self, action, name=''):
        logging.debug("In named_vlantags() for VlanGroupTag class.")
        if action == 'add':
            vlan1 = VlanTag(fmc=self.fmc)
            response = vlan1.get()
            if 'items' in response:
                new_vlan = None
                for item in response['items']:
                    if item['name'] == name:
                        new_vlan = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                        break
                if new_vlan is None:
                    logging.warning('VlanTag "{}" is not found in FMC.  Cannot add to VlanGroupTag.'.format(name))
                else:
                    if 'objects' in self.__dict__:
                        duplicate = False
                        for obj in self.objects:
                            if obj['name'] == new_vlan['name']:
                                duplicate = True
                                break
                        if not duplicate:
                            self.objects.append(new_vlan)
                            logging.info('Adding "{}" to VlanGroupTag.'.format(name))
                    else:
                        self.objects = [new_vlan]
                        logging.info('Adding "{}" to VlanGroupTag.'.format(name))
        elif action == 'remove':
            if 'objects' in self.__dict__:
                objects_list = []
                for obj in self.objects:
                    if obj['name'] != name:
                        objects_list.append(obj)
                self.objects = objects_list
                logging.info('Removed "{}" from VlanGroupTag.'.format(name))
            else:
                logging.info("This VlanGroupTag has no named_vlantags.  Nothing to remove.")
        elif action == 'clear':
            if 'objects' in self.__dict__:
                del self.objects
                logging.info('All named_vlantags removed from this VlanGroupTag.')

    def unnamed_vlantags(self, action, startvlan='', endvlan=''):
        logging.debug("In unnamed_vlantags() for VlanGroupTag class.")
        if action == 'add':
            startvlan, endvlan = validate_vlans(start_vlan=startvlan, end_vlan=endvlan)
            new_literal = {'startTag': startvlan, 'endTag': endvlan, 'type': ''}
            if 'literals' in self.__dict__:
                duplicate = False
                for obj in self.literals:
                    if obj['startTag'] == new_literal['startTag'] and obj['endTag'] == new_literal['endTag']:
                        duplicate = True
                        break
                if not duplicate:
                    self.literals.append(new_literal)
                    logging.info('Adding "{}/{}" to VlanGroupTag.'.format(startvlan, endvlan))
            else:
                self.literals = [new_literal]
                logging.info('Adding "{}/{}" to VlanGroupTag.'.format(startvlan, endvlan))
        elif action == 'remove':
            startvlan, endvlan = validate_vlans(start_vlan=startvlan, end_vlan=endvlan)
            if 'literals' in self.__dict__:
                literals_list = []
                for obj in self.literals:
                    if obj['startTag'] != startvlan and obj['endTag'] != endvlan:
                        literals_list.append(obj)
                self.literals = literals_list
                logging.info('Removed "{}/{}" from VlanGroupTag.'.format(startvlan, endvlan))
            else:
                logging.info("This VlanGroupTag has no unnamed_vlantags.  Nothing to remove.")
        elif action == 'clear':
            if 'literals' in self.__dict__:
                del self.literals
                logging.info('All unnamed_vlantags removed from this VlanGroupTag.')


class VariableSet(APIClassTemplate):
    """
    The VariableSet Object in the FMC.
    """

    URL_SUFFIX = '/object/variablesets'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for VariableSet class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for VariableSet class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for VariableSet class.")

    def post(self):
        logging.info('POST method for API for VariableSets not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for VariableSets not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for VariableSets not supported.')
        pass


class Ports(APIClassTemplate):
    """
    The Ports Object in the FMC.
    """

    URL_SUFFIX = '/object/ports'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Ports class.")
        self.parse_kwargs(**kwargs)

    def post(self):
        logging.info('POST method for API for Ports not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Ports not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Ports not supported.')
        pass


class ProtocolPort(APIClassTemplate):
    """
    The Port Object in the FMC.
    """

    URL_SUFFIX = '/object/protocolportobjects'
    REQUIRED_FOR_POST = ['name', 'port', 'protocol']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ProtocolPort class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ProtocolPort class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'port' in self.__dict__:
            json_data['port'] = self.port
        if 'protocol' in self.__dict__:
            json_data['protocol'] = self.protocol
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ProtocolPort class.")
        if 'port' in kwargs:
            self.port = kwargs['port']
        if 'protocol' in kwargs:
            self.protocol = kwargs['protocol']


class InterfaceGroup(APIClassTemplate):
    """
    The InterfaceGroup Object in the FMC.
    """

    URL_SUFFIX = '/object/interfacegroups'
    REQUIRED_FOR_POST = ['name', 'interfaceMode']
    REQUIRED_FOR_PUT = ['id']
    FILTER_BY_NAME = True

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for InterfaceGroup class.")
        self.parse_kwargs(**kwargs)
        self.type = 'InterfaceGroup'

    def format_data(self):
        logging.debug("In format_data() for InterfaceGroup class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'interfaceMode' in self.__dict__:
            json_data['interfaceMode'] = self.interfaceMode
        if 'interfaces' in self.__dict__:
            json_data['interfaces'] = self.interfaces
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for InterfaceGroup class.")
        if 'interfaceMode' in kwargs:
            self.interfaceMode = kwargs['interfaceMode']
        else:
            self.interfaceMode = 'ROUTED'
        if 'interfaces' in kwargs:
            self.interfaces = kwargs['interfaces']

    def p_interface(self, device_name="", action="add", names=[]):
        logging.debug("In interfaces() for InterfaceGroup class.")
        if action == 'add':
            intfs = []
            for name in names:
                intf = PhysicalInterface(fmc=self.fmc)
                intf.get(name=name,device_name=device_name)
                if 'id' in intf.__dict__ and 'ifname' in intf.__dict__:
                    intfs.append({'name': intf.name, 'id': intf.id, 'type': intf.type})
                elif 'id' in intf.__dict__:
                    logging.warning('PhysicalInterface, "{}", found without logical ifname.  Cannot add to InterfaceGroup.'.format(name))
                else:
                    logging.warning('PhysicalInterface, "{}", not found.  Cannot add to InterfaceGroup.'.format(name))
            if len(intfs) != 0:
                #Make sure we found at least one intf
                self.interfaces = intfs
            else:
                logging.warning('No valid PhysicalInterface found: "{}".  Cannot remove from InterfaceGroup.'.format(names))
        elif action == 'remove':
            if 'interfaces' in self.__dict__:
                intfs = []
                for interface in self.interfaces:
                    if interface["name"] not in names:
                        intfs.append(interface)
                    else:
                        logging.info('Removed "{}" from InterfaceGroup.'.format(interface["name"]))
                self.interfaces = intfs
            else:
                logging.warning("This InterfaceObject has no interfaces.  Nothing to remove.")
        elif action == 'clear-all':
            if 'interfaces' in self.__dict__:
                del self.interfaces
                logging.info('All PhysicalInterfaces removed from this InterfaceGroup.')


class InterfaceObject(APIClassTemplate):
    """
    The Interface Object Object in the FMC.
    """

    URL_SUFFIX = '/object/interfaceobjects'
    REQUIRED_FOR_POST = ['name', 'interfaceMode']
    FILTER_BY_NAME = True

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for InterfaceObject class.")
        self.parse_kwargs(**kwargs)

    def post(self):
        logging.info('POST method for API for InterfaceObject not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for InterfaceObject not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for InterfaceObject not supported.')
        pass


class ISESecurityGroupTags(APIClassTemplate):
    """
    The ISESecurityGroupTags Object in the FMC.
    """

    URL_SUFFIX = '/object/isesecuritygrouptags'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ISESecurityGroupTags class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ISESecurityGroupTags class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'tag' in self.__dict__:
            json_data['tag'] = self.tag
        if 'iseId' in self.__dict__:
            json_data['iseId'] = self.iseId
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ISESecurityGroupTags class.")

    def post(self):
        logging.info('POST method for API for ISESecurityGroupTags not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ISESecurityGroupTags not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ISESecurityGroupTags not supported.')
        pass


class Realms(APIClassTemplate):
    """
    The Realms Object in the FMC.
    """

    URL_SUFFIX = '/object/realms'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Realms class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for Realms class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Realms class.")

    def post(self):
        logging.info('POST method for API for Realms not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Realms not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Realms not supported.')
        pass


class RealmUserGroups(APIClassTemplate):
    """
    The RealmUserGroups Object in the FMC.
    """

    URL_SUFFIX = '/object/realmusergroups'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for RealmUserGroups class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for RealmUserGroups class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'realmUuid' in self.__dict__:
            json_data['realmUuid'] = self.realmUuid
        if 'realm' in self.__dict__:
            json_data['realm'] = self.realm
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for RealmUserGroups class.")

    def post(self):
        logging.info('POST method for API for RealmUserGroups not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for RealmUserGroups not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for RealmUserGroups not supported.')
        pass


class RealmUsers(APIClassTemplate):
    """
    The RealmUsers Object in the FMC.
    """

    URL_SUFFIX = '/object/realmusers'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for RealmUsers class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for RealmUsers class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'realmUuid' in self.__dict__:
            json_data['realmUuid'] = self.realmUuid
        if 'realm' in self.__dict__:
            json_data['realm'] = self.realm
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for RealmUsers class.")

    def post(self):
        logging.info('POST method for API for RealmUsers not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for RealmUsers not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for RealmUsers not supported.')
        pass


class SecurityGroupTags(APIClassTemplate):
    """
    The SecurityGroupTags Object in the FMC.
    """

    URL_SUFFIX = '/object/securitygrouptags'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SecurityGroupTags class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for SecurityGroupTags class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'tag' in self.__dict__:
            json_data['tag'] = self.tag
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SecurityGroupTags class.")

    def post(self):
        logging.info('POST method for API for SecurityGroupTags not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for SecurityGroupTags not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for SecurityGroupTags not supported.')
        pass


class SecurityZone(APIClassTemplate):
    """
    The Security Zone Object in the FMC.
    """

    URL_SUFFIX = '/object/securityzones'
    REQUIRED_FOR_POST = ['name', 'interfaceMode']
    FILTER_BY_NAME = True

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SecurityZone class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for SecurityZone class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'interfaceMode' in self.__dict__:
            json_data['interfaceMode'] = self.interfaceMode
        if 'interfaces' in self.__dict__:
            json_data['interfaces'] = self.interfaces
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SecurityZone class.")
        if 'interfaceMode' in kwargs:
            self.interfaceMode = kwargs['interfaceMode']
        else:
            self.interfaceMode = 'ROUTED'
        if 'interfaces' in kwargs:
            self.interfaces = kwargs['interfaces']


class SIUrlFeeds(APIClassTemplate):
    """
    The SIUrlFeeds Object in the FMC.
    """

    URL_SUFFIX = '/object/siurlfeeds'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SIUrlFeeds class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for SIUrlFeeds class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'checksumURL' in self.__dict__:
            json_data['checksumURL'] = self.checksumURL
        if 'feedURL' in self.__dict__:
            json_data['feedURL'] = self.feedURL
        if 'updateFrequency' in self.__dict__:
            json_data['updateFrequency'] = self.updateFrequency
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SIUrlFeeds class.")

    def post(self):
        logging.info('POST method for API for SIUrlFeeds not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for SIUrlFeeds not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for SIUrlFeeds not supported.')
        pass


class SIUrlLists(APIClassTemplate):
    """
    The SIUrlLists Object in the FMC.
    """

    URL_SUFFIX = '/object/siurllists'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SIUrlLists class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for SIUrlLists class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SIUrlLists class.")

    def post(self):
        logging.info('POST method for API for SIUrlLists not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for SIUrlLists not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for SIUrlLists not supported.')
        pass


class TunnelTags(APIClassTemplate):
    """
    The TunnelTags Object in the FMC.
    """

    URL_SUFFIX = '/object/tunneltags'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for TunnelTags class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for TunnelTags class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for TunnelTags class.")

    def post(self):
        logging.info('POST method for API for TunnelTags not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for TunnelTags not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for TunnelTags not supported.')
        pass


class Continent(APIClassTemplate):
    """
    The Continent Object in the FMC.
    """

    URL_SUFFIX = '/object/continents'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Continent class.")
        self.parse_kwargs(**kwargs)
        self.type = 'Continent'

    def format_data(self):
        logging.debug("In format_data() for Continent class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'countries' in self.__dict__:
            json_data['countries'] = self.countries
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Continent class.")
        if 'countries' in kwargs:
            self.countries = kwargs['countries']

    def post(self):
        logging.info('POST method for API for Continent not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Continent not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Continent not supported.')
        pass


class Country(APIClassTemplate):
    """
    The Country Object in the FMC.
    """

    URL_SUFFIX = '/object/countries'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Country class.")
        self.parse_kwargs(**kwargs)
        self.type = 'Country'

    def format_data(self):
        logging.debug("In format_data() for Country class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'iso2' in self.__dict__:
            json_data['iso2'] = self.iso2
        if 'iso3' in self.__dict__:
            json_data['iso3'] = self.iso3
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Country class.")
        if 'iso2' in kwargs:
            self.iso2 = kwargs['iso2']
        if 'iso3' in kwargs:
            self.iso3 = kwargs['iso3']

    def post(self):
        logging.info('POST method for API for Country not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Country not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Country not supported.')
        pass


class DNSServerGroups(APIClassTemplate):
    """
    The DNSServerGroups Object in the FMC.
    """

    URL_SUFFIX = '/object/dnsservergroups'
    REQUIRED_FOR_POST = ['name', 'timeout']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DNSServerGroups class.")
        self.parse_kwargs(**kwargs)
        self.type = 'DNSServerGroupObject'

    def format_data(self):
        logging.debug("In format_data() for DNSServerGroups class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'retries' in self.__dict__:
            json_data['retries'] = self.retries
        if 'timeout' in self.__dict__:
            json_data['timeout'] = self.timeout
        if 'dnsservers' in self.__dict__:
            json_data['dnsservers'] = self.dnsservers
        if 'defaultdomain' in self.__dict__:
            json_data['defaultdomain'] = self.defaultdomain
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DNSServerGroups class.")
        if 'retries' in kwargs:
            self.retries = kwargs['retries']
        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
        if 'dnsservers' in kwargs:
            self.dnsservers = kwargs['dnsservers']
        if 'defaultdomain' in kwargs:
            self.defaultdomain = kwargs['defaultdomain']

    def servers(self, action, name_servers):
        logging.debug("In servers() for DNSServerGroups class.")
        if action == 'add':
            for name_server in name_servers:
                if 'dnsservers' in self.__dict__:
                    self.dnsservers.append({"name-server":name_server})
                else:
                    self.dnsservers = [{"name-server":name_server}]
                logging.info('Name-server "{}" added to this DNSServerGroups object.'.format(name_server))
        elif action == 'remove':
            if 'dnsservers' in self.__dict__:
                for name_server in name_servers:
                    self.dnsservers = list(filter(lambda i: i['name-server'] != name_server, self.dnsservers))
            else:
                logging.warning('DNSServerGroups has no members.  Cannot remove name-server.')
        elif action == 'clear':
            if 'dnsservers' in self.__dict__:
                del self.dnsservers
                logging.info('All name-servers removed from this DNSServerGroups object.')


class EndPointDeviceTypes(APIClassTemplate):
    """
    The EndPointDeviceTypes Object in the FMC.
    """

    URL_SUFFIX = '/object/endpointdevicetypes'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for EndPointDeviceTypes class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for EndPointDeviceTypes class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'fqName' in self.__dict__:
            json_data['fqName'] = self.fqName
        if 'iseId' in self.__dict__:
            json_data['iseId'] = self.iseId
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for EndPointDeviceTypes class.")

    def post(self):
        logging.info('POST method for API for EndPointDeviceTypes not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for EndPointDeviceTypes not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for EndPointDeviceTypes not supported.')
        pass


class ExtendedAccessList(APIClassTemplate):
    """
    The ExtendedAccessList Object in the FMC.
    """

    URL_SUFFIX = '/object/extendedaccesslist'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ExtendedAccessList class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ExtendedAccessList class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ExtendedAccessList class.")

    def post(self):
        logging.info('POST method for API for ExtendedAccessList not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ExtendedAccessList not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ExtendedAccessList not supported.')
        pass


class FQDNS(APIClassTemplate):
    """
    The FQDNS Object in the FMC.
    """

    URL_SUFFIX = '/object/fqdns'
    VALID_FOR_DNS_RESOLUTION = ['IPV4_ONLY', 'IPV6_ONLY', 'IPV4_AND_IPV6']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for FQDNS class.")
        self.parse_kwargs(**kwargs)
        self.type = 'FQDN'

    def format_data(self):
        logging.debug("In format_data() for FQDNS class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrideTargetId' in self.__dict__:
            json_data['overrideTargetId'] = self.overrideTargetId
        if 'value' in self.__dict__:
            json_data['value'] = self.value
        if 'dnsResolution' in self.__dict__:
            if self.dnsResolution in self.VALID_FOR_DNS_RESOLUTION:
                json_data['dnsResolution'] = self.dnsResolution
            else:
                logging.warning('dnsResolution {} not a valid type".'.format(self.dnsResolution))
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for FQDNS class.")
        if 'overrideTargetId' in kwargs:
            self.overrideTargetId = kwargs['overrideTargetId']
        if 'value' in kwargs:
            self.value = kwargs['value']
        if 'dnsResolution' in kwargs:
            if kwargs['dnsResolution'] in self.VALID_FOR_DNS_RESOLUTION:
                self.dnsResolution = kwargs['dnsResolution']
            else:
                logging.warning('dnsResolution {} not a valid type".'.format(kwargs['dnsResolution']))
        if 'overrides' in kwargs:
            self.overrides = kwargs['overrides']
        if 'overridable' in kwargs:
            self.overridable = kwargs['overridable']


class Geolocation(APIClassTemplate):
    """
    The Geolocation Object in the FMC.
    """

    URL_SUFFIX = '/object/geolocations'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Geolocation class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for Geolocation class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'continentId' in self.__dict__:
            json_data['continentId'] = self.continentId
        if 'continents' in self.__dict__:
            json_data['continents'] = self.continents
        if 'countries' in self.__dict__:
            json_data['countries'] = self.countries
        if 'continentUUID' in self.__dict__:
            json_data['continentUUID'] = self.continentUUID
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Geolocation class.")

    def post(self):
        logging.info('POST method for API for Geolocation not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for Geolocation not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Geolocation not supported.')
        pass


class ICMPv4Object(APIClassTemplate):
    """
    The ICMPv4Object Object in the FMC.
    """

    URL_SUFFIX = '/object/icmpv4objects'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ICMPv4Object class.")
        self.parse_kwargs(**kwargs)
        self.type = 'ICMPV4Object'

    def format_data(self):
        logging.debug("In format_data() for ICMPv4Object class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrideTargetId' in self.__dict__:
            json_data['overrideTargetId'] = self.overrideTargetId
        if 'code' in self.__dict__:
            json_data['code'] = self.code
        if 'icmpType' in self.__dict__:
            json_data['icmpType'] = self.icmpType
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ICMPv4Object class.")
        if 'overrideTargetId' in kwargs:
            self.overrideTargetId = kwargs['overrideTargetId']
        if 'code' in kwargs:
            self.code = kwargs['code']
        if 'icmpType' in kwargs:
            self.icmpType = kwargs['icmpType']
        if 'overrides' in kwargs:
            self.overrides = kwargs['overrides']
        if 'overridable' in kwargs:
            self.overridable = kwargs['overridable']


class ICMPv6Object(APIClassTemplate):
    """
    The ICMPv6Object Object in the FMC.
    """

    URL_SUFFIX = '/object/icmpv6objects'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ICMPv6Object class.")
        self.parse_kwargs(**kwargs)
        self.type = 'ICMPV6Object'

    def format_data(self):
        logging.debug("In format_data() for ICMPv6Object class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'overrideTargetId' in self.__dict__:
            json_data['overrideTargetId'] = self.overrideTargetId
        if 'code' in self.__dict__:
            json_data['code'] = self.code
        if 'icmpType' in self.__dict__:
            json_data['icmpType'] = self.icmpType
        if 'overrides' in self.__dict__:
            json_data['overrides'] = self.overrides
        if 'overridable' in self.__dict__:
            json_data['overridable'] = self.overridable
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ICMPv6Object class.")
        if 'overrideTargetId' in kwargs:
            self.overrideTargetId = kwargs['overrideTargetId']
        if 'code' in kwargs:
            self.code = kwargs['code']
        if 'icmpType' in kwargs:
            self.icmpType = kwargs['icmpType']
        if 'overrides' in kwargs:
            self.overrides = kwargs['overrides']
        if 'overridable' in kwargs:
            self.overridable = kwargs['overridable']


class IKEv1IpsecProposals(APIClassTemplate):
    """
    The IKEv1IpsecProposals Object in the FMC.
    """

    URL_SUFFIX = '/object/ikev1ipsecproposals'
    REQUIRED_FOR_POST = ['name', 'espEncryption', 'espHash']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES-128', 'AES-192', 'AES-256', 'ESP-NULL']
    VALID_FOR_HASH = ['NONE', 'MD5', 'SHA']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv1IpsecProposals class.")
        self.parse_kwargs(**kwargs)
        self.type = 'IKEv1IPsecProposal'

    def format_data(self):
        logging.debug("In format_data() for IKEv1IpsecProposals class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'espEncryption' in self.__dict__:
            json_data['espEncryption'] = self.espEncryption
        if 'espHash' in self.__dict__:
            json_data['espHash'] = self.espHash
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv1IpsecProposals class.")
        if 'espEncryption' in kwargs:
            self.espEncryption = kwargs['espEncryption']
        if 'espHash' in kwargs:
            self.espHash = kwargs['espHash']


class IKEv1Policies(APIClassTemplate):
    """
    The IKEv1Policies Object in the FMC.
    """

    URL_SUFFIX = '/object/ikev1policies'
    REQUIRED_FOR_POST = ['name', 'encryption', 'hash', 'diffieHellmanGroup', 'lifetimeInSeconds', 'authenticationMethod']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES-128', 'AES-192', 'AES-256']
    VALID_FOR_HASH = ['MD5', 'SHA']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv1Policies class.")
        self.parse_kwargs(**kwargs)
        self.type = 'Ikev1PolicyObject'

    def format_data(self):
        logging.debug("In format_data() for IKEv1Policies class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'encryption' in self.__dict__:
            if self.encryption in self.VALID_FOR_ENCRYPTION:
                json_data['encryption'] = self.encryption
            else:
                logging.warning('encryption {} not a valid type".'.format(self.encryption))
        if 'hash' in self.__dict__:
            if self.hash in self.VALID_FOR_HASH:
                json_data['hash'] = self.hash
            else:
                logging.warning('hash {} not a valid type".'.format(self.hash))
        if 'priority' in self.__dict__:
            json_data['priority'] = self.priority
        if 'diffieHellmanGroup' in self.__dict__:
            json_data['diffieHellmanGroup'] = self.diffieHellmanGroup
        if 'authenticationMethod' in self.__dict__:
            json_data['authenticationMethod'] = self.authenticationMethod
        if 'lifetimeInSeconds' in self.__dict__:
            json_data['lifetimeInSeconds'] = self.lifetimeInSeconds
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv1Policies class.")
        if 'encryption' in kwargs:
            self.encryption = kwargs['encryption']
        if 'hash' in kwargs:
            self.hash = kwargs['hash']
        if 'priority' in kwargs:
            self.priority = kwargs['priority']
        if 'diffieHellmanGroup' in kwargs:
            self.diffieHellmanGroup = kwargs['diffieHellmanGroup']
        if 'authenticationMethod' in kwargs:
            self.authenticationMethod = kwargs['authenticationMethod']
        if 'lifetimeInSeconds' in kwargs:
            self.lifetimeInSeconds = kwargs['lifetimeInSeconds']


class IKEv2IpsecProposals(APIClassTemplate):
    """
    The IKEv2IpsecProposals Object in the FMC.
    """

    URL_SUFFIX = '/object/ikev2ipsecproposals'
    REQUIRED_FOR_POST = ['name', 'encryptionAlgorithms', 'integrityAlgorithms']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES', 'AES-192', 'AES-256', 'NULL', 'AES-GCM', 'AES-GCM-192', 'AES-GCM-256', 'AES-GMAC', 'AES-GMAC-192', 'AES-GMAC-256']
    VALID_FOR_HASH = ['NULL', 'MD5', 'SHA-1', 'SHA-256', 'SHA-384', 'SHA-512']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv2IpsecProposals class.")
        self.parse_kwargs(**kwargs)
        self.type = 'IKEv2IPsecProposal'

    def format_data(self):
        logging.debug("In format_data() for IKEv2IpsecProposals class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'encryptionAlgorithms' in self.__dict__:
            json_data['encryptionAlgorithms'] = self.encryptionAlgorithms
        if 'integrityAlgorithms' in self.__dict__:
            json_data['integrityAlgorithms'] = self.integrityAlgorithms
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv2IpsecProposals class.")
        if 'encryptionAlgorithms' in kwargs:
            self.encryptionAlgorithms = kwargs['encryptionAlgorithms']
        if 'integrityAlgorithms' in kwargs:
            self.integrityAlgorithms = kwargs['integrityAlgorithms']

    def encryption(self, action, algorithms=[]):
        logging.debug("In encryption() for IKEv2IpsecProposals class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'encryptionAlgorithms' in self.__dict__:
                        if algorithm in self.encryptionAlgorithms:
                            logging.warning('encryptionAlgorithms {} already exists".'.format(algorithm))
                        elif algorithm in self.VALID_FOR_ENCRYPTION:
                            self.encryptionAlgorithms.append(algorithm)
                        else:
                            logging.warning('encryptionAlgorithms {} not a valid type".'.format(algorithm))
                else:
                    self.encryptionAlgorithms = [algorithm]
        elif action == 'remove':
            if 'encryptionAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.encryptionAlgorithms = list(filter(lambda i: i != algorithm, self.encryptionAlgorithms))
            else:
                logging.warning('IKEv2IpsecProposals has no members.  Cannot remove encryptionAlgorithms.')
        elif action == 'clear':
            if 'encryptionAlgorithms' in self.__dict__:
                del self.encryptionAlgorithms
                logging.info('All encryptionAlgorithms removed from this IKEv2IpsecProposals object.')

    def hash(self, action, algorithms=[]):
        logging.debug("In hash() for IKEv2IpsecProposals class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'integrityAlgorithms' in self.__dict__:
                        if algorithm in self.integrityAlgorithms:
                            logging.warning('integrityAlgorithms {} already exists".'.format(algorithm))
                        elif algorithm in self.VALID_FOR_HASH:
                            self.integrityAlgorithms.append(algorithm)
                        else:
                            logging.warning('integrityAlgorithms {} not a valid type".'.format(algorithm))
                else:
                    self.integrityAlgorithms = [algorithm]
        elif action == 'remove':
            if 'integrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.integrityAlgorithms = list(filter(lambda i: i != algorithm, self.integrityAlgorithms))
            else:
                logging.warning('IKEv2IpsecProposals has no members.  Cannot remove integrityAlgorithms.')
        elif action == 'clear':
            if 'integrityAlgorithms' in self.__dict__:
                del self.integrityAlgorithms
                logging.info('All integrityAlgorithms removed from this IKEv2IpsecProposals object.')


class IKEv2Policies(APIClassTemplate):
    """
    The IKEv2Policies Object in the FMC.
    """

    URL_SUFFIX = '/object/ikev2policies'
    REQUIRED_FOR_POST = ['name', 'integrityAlgorithms', 'prfIntegrityAlgorithms', 'encryptionAlgorithms', 'diffieHellmanGroups']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES', 'AES-192', 'AES-256', 'NULL', 'AES-GCM', 'AES-GCM-192', 'AES-GCM-256']
    VALID_FOR_INTEGRITY = ['NULL', 'MD5', 'SHA', 'SHA-256', 'SHA-384', 'SHA-512']
    VALID_FOR_PRF_INTEGRITY = ['MD5', 'SHA', 'SHA-256', 'SHA-384', 'SHA-512']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv2Policies class.")
        self.parse_kwargs(**kwargs)
        self.type = 'Ikev2PolicyObject'

    def format_data(self):
        logging.debug("In format_data() for IKEv2Policies class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'priority' in self.__dict__:
            json_data['priority'] = self.priority
        if 'diffieHellmanGroups' in self.__dict__:
            json_data['diffieHellmanGroups'] = self.diffieHellmanGroups
        if 'integrityAlgorithms' in self.__dict__:
            json_data['integrityAlgorithms'] = self.integrityAlgorithms
        if 'prfIntegrityAlgorithms' in self.__dict__:
            json_data['prfIntegrityAlgorithms'] = self.prfIntegrityAlgorithms
        if 'encryptionAlgorithms' in self.__dict__:
            json_data['encryptionAlgorithms'] = self.encryptionAlgorithms
        if 'lifetimeInSeconds' in self.__dict__:
            json_data['lifetimeInSeconds'] = self.lifetimeInSeconds
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv2Policies class.")
        if 'priority' in kwargs:
            self.priority = kwargs['priority']
        if 'diffieHellmanGroups' in kwargs:
            self.diffieHellmanGroups = kwargs['diffieHellmanGroups']
        if 'integrityAlgorithms' in kwargs:
            self.integrityAlgorithms = kwargs['integrityAlgorithms']
        if 'prfIntegrityAlgorithms' in kwargs:
            self.prfIntegrityAlgorithms = kwargs['prfIntegrityAlgorithms']
        if 'encryptionAlgorithms' in kwargs:
            self.encryptionAlgorithms = kwargs['encryptionAlgorithms']
        if 'lifetimeInSeconds' in kwargs:
            self.lifetimeInSeconds = kwargs['lifetimeInSeconds']

    def encryption(self, action, algorithms=[]):
        logging.debug("In encryption() for IKEv2Policies class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'encryptionAlgorithms' in self.__dict__:
                        if algorithm in self.encryptionAlgorithms:
                            logging.warning('encryptionAlgorithms {} already exists".'.format(algorithm))
                        elif algorithm in self.VALID_FOR_ENCRYPTION:
                            self.encryptionAlgorithms.append(algorithm)
                        else:
                            logging.warning('encryptionAlgorithms {} not a valid type".'.format(algorithm))
                else:
                    self.encryptionAlgorithms = [algorithm]
        elif action == 'remove':
            if 'encryptionAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.encryptionAlgorithms = list(filter(lambda i: i != algorithm, self.encryptionAlgorithms))
            else:
                logging.warning('IKEv2Policies has no members.  Cannot remove encryptionAlgorithms.')
        elif action == 'clear':
            if 'encryptionAlgorithms' in self.__dict__:
                del self.encryptionAlgorithms
                logging.info('All encryptionAlgorithms removed from this IKEv2Policies object.')

    def hash(self, action, algorithms=[]):
        logging.debug("In hash() for IKEv2Policies class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'integrityAlgorithms' in self.__dict__:
                        if algorithm in self.integrityAlgorithms:
                            logging.warning('integrityAlgorithms {} already exists".'.format(algorithm))
                        elif algorithm in self.VALID_FOR_INTEGRITY:
                            self.integrityAlgorithms.append(algorithm)
                        else:
                            logging.warning('integrityAlgorithms {} not a valid type".'.format(algorithm))
                else:
                    if algorithm in self.VALID_FOR_INTEGRITY:
                        self.integrityAlgorithms = [algorithm]
                    else:
                        logging.warning('integrityAlgorithms {} not a valid type".'.format(algorithm))
        elif action == 'remove':
            if 'integrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.integrityAlgorithms = list(filter(lambda i: i != algorithm, self.integrityAlgorithms))
            else:
                logging.warning('IKEv2Policies has no members.  Cannot remove integrityAlgorithms.')
        elif action == 'clear':
            if 'integrityAlgorithms' in self.__dict__:
                del self.integrityAlgorithms
                logging.info('All integrityAlgorithms removed from this IKEv2Policies object.')

    def prf_hash(self, action, algorithms=[]):
        logging.debug("In prf_hash() for IKEv2Policies class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'prfIntegrityAlgorithms' in self.__dict__:
                        if algorithm in self.prfIntegrityAlgorithms:
                            logging.warning('prfIntegrityAlgorithms {} already exists".'.format(algorithm))
                        elif algorithm in self.VALID_FOR_PRF_INTEGRITY:
                            self.prfIntegrityAlgorithms.append(algorithm)
                        else:
                            logging.warning('prfIntegrityAlgorithms {} not a valid type".'.format(algorithm))
                else:
                    if algorithm in self.VALID_FOR_PRF_INTEGRITY:
                        self.prfIntegrityAlgorithms = [algorithm]
                    else:
                      logging.warning('prfIntegrityAlgorithms {} not a valid type".'.format(algorithm))
        elif action == 'remove':
            if 'prfIntegrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.prfIntegrityAlgorithms = list(filter(lambda i: i != algorithm, self.prfIntegrityAlgorithms))
            else:
                logging.warning('IKEv2Policies has no members.  Cannot remove prfIntegrityAlgorithms.')
        elif action == 'clear':
            if 'prfIntegrityAlgorithms' in self.__dict__:
                del self.prfIntegrityAlgorithms
                logging.info('All prfIntegrityAlgorithms removed from this IKEv2Policies object.')


class PortObjectGroup(APIClassTemplate):
    """
    The PortObjectGroup Object in the FMC.
    """

    URL_SUFFIX = '/object/portobjectgroups'

    # Technically you can have objects OR literals but I'm not set up for "OR" logic, yet.
    REQUIRED_FOR_POST = ['name', 'objects']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for PortObjectGroup class.")
        self.parse_kwargs(**kwargs)
        self.type = 'NetworkGroup'

    def format_data(self):
        logging.debug("In format_data() for PortObjectGroup class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'objects' in self.__dict__:
            json_data['objects'] = self.objects
        if 'literals' in self.__dict__:
            json_data['literals'] = self.literals
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for PortObjectGroup class.")
        if 'objects' in kwargs:
            self.objects = kwargs['objects']
        if 'literals' in kwargs:
            self.literals = kwargs['literals']

    def named_ports(self, action, name=''):
        logging.debug("In named_ports() for PortObjectGroup class.")
        if action == 'add':
            port1 = Ports(fmc=self.fmc)
            response = port1.get()
            if 'items' in response:
                new_port = None
                for item in response['items']:
                    if item['name'] == name:
                        new_port = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                        break
                if new_port is None:
                    logging.warning('Port "{}" is not found in FMC.  Cannot add to PortObjectGroup.'.format(name))
                else:
                    if 'objects' in self.__dict__:
                        duplicate = False
                        for obj in self.objects:
                            if obj['name'] == new_port['name']:
                                duplicate = True
                                break
                        if not duplicate:
                            self.objects.append(new_port)
                            logging.info('Adding "{}" to PortObjectGroup.'.format(name))
                    else:
                        self.objects = [new_port]
                        logging.info('Adding "{}" to PortObjectGroup.'.format(name))
        elif action == 'remove':
            if 'objects' in self.__dict__:
                objects_list = []
                for obj in self.objects:
                    if obj['name'] != name:
                        objects_list.append(obj)
                self.objects = objects_list
                logging.info('Removed "{}" from PortObjectGroup.'.format(name))
            else:
                logging.info("This PortObjectGroup has no named_ports.  Nothing to remove.")
        elif action == 'clear':
            if 'objects' in self.__dict__:
                del self.objects
                logging.info('All named_ports removed from this PortObjectGroup.')
