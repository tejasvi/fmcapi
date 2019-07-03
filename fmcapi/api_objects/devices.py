"""
This module contains the "device" class objects that represent the various objects in the FMC.
"""

from .api_template import *
from .helper_functions import *
from .api_template import *
from .devices import *
from .misc import *
from .objects import *
from .policy import *

class Device(APIClassTemplate):
    """
    The Device Object in the FMC.
    """

    URL_SUFFIX = '/devices/devicerecords'
    REQUIRED_FOR_POST = ['accessPolicy', 'hostName', 'regKey']
    REQUIRED_FOR_PUT = ['id']
    LICENSES = ['BASE', 'MALWARE', 'URLFilter', 'THREAT', 'VPN']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Device class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for Device class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'hostName' in self.__dict__:
            json_data['hostName'] = self.hostName
        if 'natID' in self.__dict__:
            json_data['natID'] = self.natID
        if 'regKey' in self.__dict__:
            json_data['regKey'] = self.regKey
        if 'license_caps' in self.__dict__:
            json_data['license_caps'] = self.license_caps
        if 'accessPolicy' in self.__dict__:
            json_data['accessPolicy'] = self.accessPolicy
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Device class.")
        if 'hostName' in kwargs:
            self.hostName = kwargs['hostName']
        if 'natID' in kwargs:
            self.natID = kwargs['natID']
        if 'regKey' in kwargs:
            self.regKey = kwargs['regKey']
        if 'license_caps' in kwargs:
            self.license_caps = kwargs['license_caps']
        if 'accessPolicy' in kwargs:
            self.accessPolicy = kwargs['accessPolicy']
        if 'acp_name' in kwargs:
            self.acp(name=kwargs['acp_name'])
        if 'model' in kwargs:
            self.model = kwargs['model']
        if 'modelId' in kwargs:
            self.modelId = kwargs['modelId']
        if 'modelNumber' in kwargs:
            self.modelNumber = kwargs['modelNumber']
        if 'modelType' in kwargs:
            self.modelType = kwargs['modelType']
        if 'healthStatus' in kwargs:
            self.healthStatus = kwargs['healthStatus']
        if 'healthPolicy' in kwargs:
            self.healthPolicy = kwargs['healthPolicy']
        if 'keepLocalEvents' in kwargs:
            self.keepLocalEvents = kwargs['keepLocalEvents']
        if 'prohibitPacketTransfer' in kwargs:
            self.prohibitPacketTransfer = kwargs['prohibitPacketTransfer']

    def licensing(self, action, name='BASE'):
        logging.debug("In licensing() for Device class.")
        if action == 'add':
            if name in self.LICENSES:
                if 'license_caps' in self.__dict__:
                    self.license_caps.append(name)
                    self.license_caps = list(set(self.license_caps))
                else:
                    self.license_caps = [name]
                logging.info('License "{}" added to this Device object.'.format(name))

            else:
                logging.warning('{} not found in {}.  Cannot add license to Device.'.format(name, self.LICENSES))
        elif action == 'remove':
            if name in self.LICENSES:
                if 'license_caps' in self.__dict__:
                    try:
                        self.license_caps.remove(name)
                    except ValueError:
                        logging.warning('{} is not assigned to this device thus cannot be removed.'.format(name))
                    logging.info('License "{}" removed from this Device object.'.format(name))
                else:
                    logging.warning('{} is not assigned to this device thus cannot be removed.'.format(name))

            else:
                logging.warning('{} not found in {}.  Cannot remove license from '
                                'Device.'.format(name, self.LICENSES))
        elif action == 'clear':
            if 'license_caps' in self.__dict__:
                del self.license_caps
                logging.info('All licensing removed from this Device object.')

    def acp(self, name=''):
        logging.debug("In acp() for Device class.")
        acp = AccessControlPolicy(fmc=self.fmc)
        acp.get(name=name)
        if 'id' in acp.__dict__:
            self.accessPolicy = {'id': acp.id, 'type': acp.type}
        else:
            logging.warning('Access Control Policy {} not found.  Cannot set up accessPolicy for '
                            'Device.'.format(name))

    def post(self, **kwargs):
        logging.debug("In post() for Device class.")
        # Attempting to "Deploy" during Device registration causes issues.
        self.fmc.autodeploy = False
        return super().post(**kwargs)


class PhysicalInterface(APIClassTemplate):
    """
    The Physical Interface Object in the FMC.
    """
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""
    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_PUT = ['id', 'device_id']
    VALID_FOR_IPV4 = ['static', 'dhcp', 'pppoe']
    VALID_FOR_MODE = ['INLINE', 'PASSIVE', 'TAP', 'ERSPAN', 'NONE']
    VALID_FOR_MTU = range(64, 9000)
    VALID_FOR_HARDWARE_SPEED = ['AUTO', 'TEN', 'HUNDRED', 'THOUSAND', 'TEN_THOUSAND', 'FORTY_THOUSAND', 'LAKH']
    VALID_FOR_HARDWARE_DUPLEX = ['AUTO', 'FULL', 'HALF']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for PhysicalInterface class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for PhysicalInterface class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'mode' in self.__dict__:
            json_data['mode'] = self.mode
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'hardware' in self.__dict__:
            json_data['hardware'] = self.hardware
        if 'MTU' in self.__dict__:
            json_data['MTU'] = self.MTU
        if 'managementOnly' in self.__dict__:
            json_data['managementOnly'] = self.managementOnly
        if 'ifname' in self.__dict__:
            json_data['ifname'] = self.ifname
        if 'securityZone' in self.__dict__:
            json_data['securityZone'] = self.securityZone
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'ipv4' in self.__dict__:
            json_data['ipv4'] = self.ipv4
        if 'ipv6' in self.__dict__:
            json_data['ipv6'] = self.ipv6
        if 'activeMACAddress' in self.__dict__:
            json_data['activeMACAddress'] = self.activeMACAddress
        if 'standbyMACAddress' in self.__dict__:
            json_data['standbyMACAddress'] = self.standbyMACAddress
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for PhysicalInterface class.")
        if 'ipv4' in kwargs:
            if list(kwargs['ipv4'].keys())[0] in self.VALID_FOR_IPV4:
                self.ipv4 = kwargs['ipv4']
            else:
                logging.warning('Method {} is not a valid ipv4 type.'.format(kwargs['ipv4']))
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'mode' in kwargs:
            if kwargs['mode'] in self.VALID_FOR_MODE:
                self.mode = kwargs['mode']
            else:
                logging.warning('Mode {} is not a valid mode.'.format(kwargs['mode']))
        if 'hardware' in kwargs:
            self.hardware = kwargs['hardware']
        if 'securityZone' in kwargs:
            self.securityZone = kwargs['securityZone']
        if 'enabled' in kwargs:
            # This doesn't seem to be working
            self.enabled = kwargs['enabled']
        else:
            self.enabled = False
        if 'MTU' in kwargs:
            if kwargs['MTU'] in self.VALID_FOR_MTU:
                self.MTU = kwargs['MTU']
            else:
                logging.warning('MTU {} should be in the range 64-9000".'.format(kwargs['MTU']))
                self.MTU = 1500
        if 'managementOnly' in kwargs:
            self.managementOnly = kwargs['managementOnly']
        if 'ifname' in kwargs:
            self.ifname = kwargs['ifname']
        if 'ipv6' in kwargs:
            self.ipv6 = kwargs['ipv6']
        if 'activeMACAddress' in kwargs:
            self.activeMACAddress = kwargs['activeMACAddress']
        if 'standbyMACAddress' in kwargs:
            self.standbyMACAddress = kwargs['standbyMACAddress']

    def device(self, device_name):
        logging.debug("In device() for PhysicalInterface class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/physicalinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL, self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'physicalInterface.'.format(device_name))

    def sz(self, name):
        logging.debug("In sz() for PhysicalInterface class.")
        sz = SecurityZone(fmc=self.fmc)
        sz.get(name=name)
        if 'id' in sz.__dict__:
            new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
            self.securityZone = new_zone
        else:
            logging.warning('Security Zone, "{}", not found.  Cannot add to PhysicalInterface.'.format(name))

    def static(self, ipv4addr, ipv4mask):
        logging.debug("In static() for PhysicalInterface class.")
        self.ipv4 = {"static": {"address": ipv4addr, "netmask": ipv4mask}}

    def dhcp(self, enableDefault=True, routeMetric=1):
        logging.debug("In dhcp() for PhysicalInterface class.")
        self.ipv4 = {"dhcp": {"enableDefaultRouteDHCP": enableDefault, "dhcpRouteMetric": routeMetric}}

    def hwmode(self, mode):
        logging.debug("In hwmode() for PhysicalInterface class.")
        if mode in self.VALID_FOR_MODE:
            self.mode = mode
        else:
            logging.warning('Mode {} is not a valid mode.'.format(mode))

    def hardware(self, speed, duplex="FULL"):
        # There are probably some incompatibilities that need to be accounted for
        logging.debug("In hardware() for PhysicalInterface class.")
        if speed in self.VALID_FOR_HARDWARE_SPEED and duplex in self.VALID_FOR_HARDWARE_DUPLEX:
            self.hardware = {"duplex": duplex, "speed": speed}
        else:
            logging.warning('Speed {} or Duplex {} is not a valid mode.'.format(speed, duplex))


class BridgeGroupInterfaces(APIClassTemplate):
    """
    The Bridge Group Interface Object in the FMC.
    """
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""
    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['bridgeGroupId']
    REQUIRED_FOR_PUT = ['id', 'device_id']
    VALID_FOR_IPV4 = ['static', 'dhcp', 'pppoe']
    VALID_FOR_MODE = ['INLINE', 'PASSIVE', 'TAP', 'ERSPAN', 'NONE']
    VALID_FOR_MTU = range(64, 9000)

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for BridgeGroupInterfaces class.")
        self.parse_kwargs(**kwargs)
        self.type = "BridgeGroupInterface"

    def format_data(self):
        logging.debug("In format_data() for BridgeGroupInterfaces class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'mode' in self.__dict__:
            json_data['mode'] = self.mode
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'MTU' in self.__dict__:
            json_data['MTU'] = self.MTU
        if 'managementOnly' in self.__dict__:
            json_data['managementOnly'] = self.managementOnly
        if 'ipAddress' in self.__dict__:
            json_data['ipAddress'] = self.ipAddress
        if 'selectedInterfaces' in self.__dict__:
            json_data['selectedInterfaces'] = self.selectedInterfaces
        if 'bridgeGroupId' in self.__dict__:
            json_data['bridgeGroupId'] = self.bridgeGroupId
        if 'macLearn' in self.__dict__:
            json_data['macLearn'] = self.macLearn
        if 'ifname' in self.__dict__:
            json_data['ifname'] = self.ifname
        if 'securityZone' in self.__dict__:
            json_data['securityZone'] = self.securityZone
        if 'arpConfig' in self.__dict__:
            json_data['arpConfig'] = self.arpConfig
        if 'ipv4' in self.__dict__:
            json_data['ipv4'] = self.ipv4
        if 'ipv6' in self.__dict__:
            json_data['ipv6'] = self.ipv6
        if 'macTable' in self.__dict__:
            json_data['macTable'] = self.macTable
        if 'enableAntiSpoofing' in self.__dict__:
            json_data['enableAntiSpoofing'] = self.enableAntiSpoofing
        if 'fragmentReassembly' in self.__dict__:
            json_data['fragmentReassembly'] = self.fragmentReassembly
        if 'enableDNSLookup' in self.__dict__:
            json_data['enableDNSLookup'] = self.enableDNSLookup
        if 'activeMACAddress' in self.__dict__:
            json_data['activeMACAddress'] = self.activeMACAddress
        if 'standbyMACAddress' in self.__dict__:
            json_data['standbyMACAddress'] = self.standbyMACAddress
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for BridgeGroupInterfaces class.")
        if 'ipv4' in kwargs:
            if list(kwargs['ipv4'].keys())[0] in self.VALID_FOR_IPV4:
                self.ipv4 = kwargs['ipv4']
            else:
                logging.warning('Method {} is not a valid ipv4 type.'.format(kwargs['ipv4']))
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'mode' in kwargs:
            if kwargs['mode'] in self.VALID_FOR_MODE:
                self.mode = kwargs['mode']
            else:
                logging.warning('Mode {} is not a valid mode.'.format(kwargs['mode']))
        if 'securityZone' in kwargs:
            self.securityZone = kwargs['securityZone']
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']
        else:
            self.enabled = False
        if 'MTU' in kwargs:
            if kwargs['MTU'] in self.VALID_FOR_MTU:
                self.MTU = kwargs['MTU']
            else:
                logging.warning('MTU {} should be in the range 64-9000".'.format(kwargs['MTU']))
                self.MTU = 1500
        if 'managementOnly' in kwargs:
            self.managementOnly = kwargs['managementOnly']
        if 'ipAddress' in kwargs:
            self.ipAddress = kwargs['ipAddress']
        if 'selectedInterfaces' in kwargs:
            self.selectedInterfaces = kwargs['selectedInterfaces']
        if 'bridgeGroupId' in kwargs:
            self.bridgeGroupId = kwargs['bridgeGroupId']
        if 'macLearn' in kwargs:
            self.macLearn = kwargs['macLearn']
        if 'ifname' in kwargs:
            self.ifname = kwargs['ifname']
        if 'arpConfig' in kwargs:
            self.arpConfig = kwargs['arpConfig']
        if 'ipv6' in kwargs:
            self.ipv6 = kwargs['ipv6']
        if 'macTable' in kwargs:
            self.macTable = kwargs['macTable']
        if 'enableAntiSpoofing' in kwargs:
            self.enableAntiSpoofing = kwargs['enableAntiSpoofing']
        if 'fragmentReassembly' in kwargs:
            self.fragmentReassembly = kwargs['fragmentReassembly']
        if 'enableDNSLookup' in kwargs:
            self.enableDNSLookup = kwargs['enableDNSLookup']
        if 'activeMACAddress' in kwargs:
            self.activeMACAddress = kwargs['activeMACAddress']
        if 'standbyMACAddress' in kwargs:
            self.standbyMACAddress = kwargs['standbyMACAddress']

    def device(self, device_name):
        logging.debug("In device() for BridgeGroupInterfaces class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/bridgegroupinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL,
                                                              self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'BridgeGroupInterfaces.'.format(device_name))

    def sz(self, name):
        logging.debug("In sz() for BridgeGroupInterfaces class.")
        sz = SecurityZone(fmc=self.fmc)
        sz.get(name=name)
        if 'id' in sz.__dict__:
            new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
            self.securityZone = new_zone
        else:
            logging.warning('Security Zone, "{}", not found.  Cannot add to BridgeGroupInterfaces.'.format(name))

    def static(self, ipv4addr, ipv4mask):
        logging.debug("In static() for BridgeGroupInterfaces class.")
        self.ipv4 = {"static": {"address": ipv4addr, "netmask": ipv4mask}}

    def dhcp(self, enableDefault=True, routeMetric=1):
        logging.debug("In dhcp() for BridgeGroupInterfaces class.")
        self.ipv4 = {"dhcp": {"enableDefaultRouteDHCP": enableDefault, "dhcpRouteMetric": routeMetric}}

    def p_interfaces(self, p_interfaces, device_name):
        logging.debug("In p_interface() for BridgeGroupInterfaces class.")
        list = []
        for p_intf in p_interfaces:
            intf1 = PhysicalInterface(fmc=self.fmc)
            intf1.get(name=p_intf, device_name=device_name)
            if 'id' in intf1.__dict__:
                list.append({'name': intf1.name, 'id': intf1.id, 'type': intf1.type})
            else:
                logging.warning(
                    'PhysicalInterface, "{}", not found.  Cannot add to BridgeGroupInterfaces.'.format(name))
        self.selectedInterfaces = list


class RedundantInterfaces(APIClassTemplate):
    """
    The Bridge Group Interface Object in the FMC.
    """
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""
    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['redundantId']
    REQUIRED_FOR_PUT = ['id', 'device_id']
    VALID_FOR_IPV4 = ['static', 'dhcp', 'pppoe']
    VALID_FOR_MODE = ['INLINE', 'PASSIVE', 'TAP', 'ERSPAN', 'NONE']
    VALID_FOR_MTU = range(64, 9000)

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for RedundantInterfaces class.")
        self.parse_kwargs(**kwargs)
        self.type = "RedundantInterface"

    def format_data(self):
        logging.debug("In format_data() for RedundantInterfaces class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'mode' in self.__dict__:
            json_data['mode'] = self.mode
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'MTU' in self.__dict__:
            json_data['MTU'] = self.MTU
        if 'managementOnly' in self.__dict__:
            json_data['managementOnly'] = self.managementOnly
        if 'ipAddress' in self.__dict__:
            json_data['ipAddress'] = self.ipAddress
        if 'primaryInterface' in self.__dict__:
            json_data['primaryInterface'] = self.primaryInterface
        if 'secondaryInterface' in self.__dict__:
            json_data['secondaryInterface'] = self.secondaryInterface
        if 'redundantId' in self.__dict__:
            json_data['redundantId'] = self.redundantId
        if 'macLearn' in self.__dict__:
            json_data['macLearn'] = self.macLearn
        if 'ifname' in self.__dict__:
            json_data['ifname'] = self.ifname
        if 'securityZone' in self.__dict__:
            json_data['securityZone'] = self.securityZone
        if 'arpConfig' in self.__dict__:
            json_data['arpConfig'] = self.arpConfig
        if 'ipv4' in self.__dict__:
            json_data['ipv4'] = self.ipv4
        if 'ipv6' in self.__dict__:
            json_data['ipv6'] = self.ipv6
        if 'macTable' in self.__dict__:
            json_data['macTable'] = self.macTable
        if 'enableAntiSpoofing' in self.__dict__:
            json_data['enableAntiSpoofing'] = self.enableAntiSpoofing
        if 'fragmentReassembly' in self.__dict__:
            json_data['fragmentReassembly'] = self.fragmentReassembly
        if 'enableDNSLookup' in self.__dict__:
            json_data['enableDNSLookup'] = self.enableDNSLookup
        if 'activeMACAddress' in self.__dict__:
            json_data['activeMACAddress'] = self.activeMACAddress
        if 'standbyMACAddress' in self.__dict__:
            json_data['standbyMACAddress'] = self.standbyMACAddress
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for RedundantInterfaces class.")
        if 'ipv4' in kwargs:
            if list(kwargs['ipv4'].keys())[0] in self.VALID_FOR_IPV4:
                self.ipv4 = kwargs['ipv4']
            else:
                logging.warning('Method {} is not a valid ipv4 type.'.format(kwargs['ipv4']))
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'mode' in kwargs:
            if kwargs['mode'] in self.VALID_FOR_MODE:
                self.mode = kwargs['mode']
            else:
                logging.warning('Mode {} is not a valid mode.'.format(kwargs['mode']))
        if 'securityZone' in kwargs:
            self.securityZone = kwargs['securityZone']
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']
        if 'MTU' in kwargs:
            if kwargs['MTU'] in self.VALID_FOR_MTU:
                self.MTU = kwargs['MTU']
            else:
                logging.warning('MTU {} should be in the range 64-9000".'.format(kwargs['MTU']))
                self.MTU = 1500
        if 'managementOnly' in kwargs:
            self.managementOnly = kwargs['managementOnly']
        if 'ipAddress' in kwargs:
            self.ipAddress = kwargs['ipAddress']
        if 'primaryInterface' in kwargs:
            self.primaryInterface = kwargs['primaryInterface']
        if 'secondaryInterface' in kwargs:
            self.secondaryInterface = kwargs['secondaryInterface']
        if 'redundantId' in kwargs:
            self.redundantId = kwargs['redundantId']
        if 'macLearn' in kwargs:
            self.macLearn = kwargs['macLearn']
        if 'ifname' in kwargs:
            self.ifname = kwargs['ifname']
        if 'arpConfig' in kwargs:
            self.arpConfig = kwargs['arpConfig']
        if 'ipv6' in kwargs:
            self.ipv6 = kwargs['ipv6']
        if 'macTable' in kwargs:
            self.macTable = kwargs['macTable']
        if 'enableAntiSpoofing' in kwargs:
            self.enableAntiSpoofing = kwargs['enableAntiSpoofing']
        if 'fragmentReassembly' in kwargs:
            self.fragmentReassembly = kwargs['fragmentReassembly']
        if 'enableDNSLookup' in kwargs:
            self.enableDNSLookup = kwargs['enableDNSLookup']
        if 'activeMACAddress' in kwargs:
            self.activeMACAddress = kwargs['activeMACAddress']
        if 'standbyMACAddress' in kwargs:
            self.standbyMACAddress = kwargs['standbyMACAddress']

    def device(self, device_name):
        logging.debug("In device() for RedundantInterfaces class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/redundantinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL, self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'RedundantInterfaces.'.format(device_name))

    def sz(self, name):
        logging.debug("In sz() for RedundantInterfaces class.")
        sz = SecurityZone(fmc=self.fmc)
        sz.get(name=name)
        if 'id' in sz.__dict__:
            new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
            self.securityZone = new_zone
        else:
            logging.warning('Security Zone, "{}", not found.  Cannot add to RedundantInterfaces.'.format(name))

    def static(self, ipv4addr, ipv4mask):
        logging.debug("In static() for RedundantInterfaces class.")
        self.ipv4 = {"static": {"address": ipv4addr, "netmask": ipv4mask}}

    def dhcp(self, enableDefault=True, routeMetric=1):
        logging.debug("In dhcp() for RedundantInterfaces class.")
        self.ipv4 = {"dhcp": {"enableDefaultRouteDHCP": enableDefault, "dhcpRouteMetric": routeMetric}}

    def primary(self, p_interface, device_name):
        logging.debug("In primary() for RedundantInterfaces class.")
        intf1 = PhysicalInterface(fmc=self.fmc)
        intf1.get(name=p_interface, device_name=device_name)
        if 'id' in intf1.__dict__:
            self.primaryInterface = {'name': intf1.name, 'id': intf1.id, 'type': intf1.type}
            if 'MTU' not in self.__dict__:
                self.MTU = intf1.MTU
        else:
            logging.warning('PhysicalInterface, "{}", not found.  Cannot add to RedundantInterfaces.'.format(name))

    def secondary(self, p_interface, device_name):
        logging.debug("In primary() for RedundantInterfaces class.")
        intf1 = PhysicalInterface(fmc=self.fmc)
        intf1.get(name=p_interface, device_name=device_name)
        if 'id' in intf1.__dict__:
            self.secondaryInterface = {'name': intf1.name, 'id': intf1.id, 'type': intf1.type}
        else:
            logging.warning('PhysicalInterface, "{}", not found.  Cannot add to RedundantInterfaces.'.format(name))


class EtherchannelInterfaces(APIClassTemplate):
    """
    The Etherchanel Interface Object in the FMC.
    """
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""
    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['etherChannelId', 'mode', 'MTU']
    REQUIRED_FOR_PUT = ['id', 'device_id']
    VALID_FOR_IPV4 = ['static', 'dhcp', 'pppoe']
    VALID_FOR_MODE = ['INLINE', 'PASSIVE', 'TAP', 'ERSPAN', 'NONE']
    VALID_FOR_LACP_MODE = ['ACTIVE', 'PASSIVE', 'ON']
    VALID_FOR_MTU = range(64, 9000)

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for RedundantInterfaces class.")
        self.parse_kwargs(**kwargs)
        self.type = "RedundantInterface"

    def format_data(self):
        logging.debug("In format_data() for EtherchannelInterfaces class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'mode' in self.__dict__:
            json_data['mode'] = self.mode
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'MTU' in self.__dict__:
            json_data['MTU'] = self.MTU
        if 'managementOnly' in self.__dict__:
            json_data['managementOnly'] = self.managementOnly
        if 'ipAddress' in self.__dict__:
            json_data['ipAddress'] = self.ipAddress
        if 'selectedInterfaces' in self.__dict__:
            json_data['selectedInterfaces'] = self.selectedInterfaces
        if 'etherChannelId' in self.__dict__:
            json_data['etherChannelId'] = self.etherChannelId
        if 'lacpMode' in self.__dict__:
            json_data['lacpMode'] = self.lacpMode
        if 'maxActivePhysicalInterface' in self.__dict__:
            json_data['maxActivePhysicalInterface'] = self.maxActivePhysicalInterface
        if 'minActivePhysicalInterface' in self.__dict__:
            json_data['minActivePhysicalInterface'] = self.minActivePhysicalInterface
        if 'hardware' in self.__dict__:
            json_data['hardware'] = self.hardware
        if 'erspanFlowId' in self.__dict__:
            json_data['erspanFlowId'] = self.erspanFlowId
        if 'erspanSourceIP' in self.__dict__:
            json_data['erspanSourceIP'] = self.erspanSourceIP
        if 'loadBalancing' in self.__dict__:
            json_data['loadBalancing'] = self.loadBalancing
        if 'macLearn' in self.__dict__:
            json_data['macLearn'] = self.macLearn
        if 'ifname' in self.__dict__:
            json_data['ifname'] = self.ifname
        if 'securityZone' in self.__dict__:
            json_data['securityZone'] = self.securityZone
        if 'arpConfig' in self.__dict__:
            json_data['arpConfig'] = self.arpConfig
        if 'ipv4' in self.__dict__:
            json_data['ipv4'] = self.ipv4
        if 'ipv6' in self.__dict__:
            json_data['ipv6'] = self.ipv6
        if 'macTable' in self.__dict__:
            json_data['macTable'] = self.macTable
        if 'enableAntiSpoofing' in self.__dict__:
            json_data['enableAntiSpoofing'] = self.enableAntiSpoofing
        if 'fragmentReassembly' in self.__dict__:
            json_data['fragmentReassembly'] = self.fragmentReassembly
        if 'enableDNSLookup' in self.__dict__:
            json_data['enableDNSLookup'] = self.enableDNSLookup
        if 'activeMACAddress' in self.__dict__:
            json_data['activeMACAddress'] = self.activeMACAddress
        if 'standbyMACAddress' in self.__dict__:
            json_data['standbyMACAddress'] = self.standbyMACAddress
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for EtherchannelInterfaces class.")
        if 'ipv4' in kwargs:
            if list(kwargs['ipv4'].keys())[0] in self.VALID_FOR_IPV4:
                self.ipv4 = kwargs['ipv4']
            else:
                logging.warning('Method {} is not a valid ipv4 type.'.format(kwargs['ipv4']))
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'mode' in kwargs:
            if kwargs['mode'] in self.VALID_FOR_MODE:
                self.mode = kwargs['mode']
            else:
                logging.warning('Mode {} is not a valid mode.'.format(kwargs['mode']))
        if 'securityZone' in kwargs:
            self.securityZone = kwargs['securityZone']
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']
        if 'MTU' in kwargs:
            if kwargs['MTU'] in self.VALID_FOR_MTU:
                self.MTU = kwargs['MTU']
            else:
                logging.warning('MTU {} should be in the range 64-9000".'.format(kwargs['MTU']))
                self.MTU = 1500
        if 'managementOnly' in kwargs:
            self.managementOnly = kwargs['managementOnly']
        if 'ipAddress' in kwargs:
            self.ipAddress = kwargs['ipAddress']
        if 'selectedInterfaces' in kwargs:
            self.selectedInterfaces = kwargs['selectedInterfaces']
        if 'etherChannelId' in kwargs:
            self.etherChannelId = kwargs['etherChannelId']
        if 'lacpMode' in kwargs:
            if kwargs['lacpMode'] in self.VALID_FOR_LACP_MODE:
                self.lacpMode = kwargs['lacpMode']
            else:
                logging.warning('LACP Mode {} is not a valid mode".'.format(kwargs['lacpMode']))
        if 'maxActivePhysicalInterface' in kwargs:
            self.maxActivePhysicalInterface = kwargs['maxActivePhysicalInterface']
        if 'minActivePhysicalInterface' in kwargs:
            self.minActivePhysicalInterface = kwargs['minActivePhysicalInterface']
        if 'hardware' in kwargs:
            self.hardware = kwargs['hardware']
        if 'erspanFlowId' in kwargs:
            self.erspanFlowId = kwargs['erspanFlowId']
        if 'erspanSourceIP' in kwargs:
            self.erspanSourceIP = kwargs['erspanSourceIP']
        if 'loadBalancing' in kwargs:
            if kwargs['loadBalancing'] in self.VALID_FOR_LOAD_BALANCING:
                self.loadBalancing = kwargs['loadBalancing']
            else:
                logging.warning('Load balancing method {} is not a valid method".'.format(kwargs['loadBalancing']))
        if 'macLearn' in kwargs:
            self.macLearn = kwargs['macLearn']
        if 'ifname' in kwargs:
            self.ifname = kwargs['ifname']
        if 'arpConfig' in kwargs:
            self.arpConfig = kwargs['arpConfig']
        if 'ipv6' in kwargs:
            self.ipv6 = kwargs['ipv6']
        if 'macTable' in kwargs:
            self.macTable = kwargs['macTable']
        if 'enableAntiSpoofing' in kwargs:
            self.enableAntiSpoofing = kwargs['enableAntiSpoofing']
        if 'fragmentReassembly' in kwargs:
            self.fragmentReassembly = kwargs['fragmentReassembly']
        if 'enableDNSLookup' in kwargs:
            self.enableDNSLookup = kwargs['enableDNSLookup']
        if 'activeMACAddress' in kwargs:
            self.activeMACAddress = kwargs['activeMACAddress']
        if 'standbyMACAddress' in kwargs:
            self.standbyMACAddress = kwargs['standbyMACAddress']

    def device(self, device_name):
        logging.debug("In device() for EtherchannelInterfaces class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/etherchannelinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL,
                                                               self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'EtherchannelInterfaces.'.format(device_name))

    def sz(self, name):
        logging.debug("In sz() for EtherchannelInterfaces class.")
        sz = SecurityZone(fmc=self.fmc)
        sz.get(name=name)
        if 'id' in sz.__dict__:
            new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
            self.securityZone = new_zone
        else:
            logging.warning('Security Zone, "{}", not found.  Cannot add to RedundantInterfaces.'.format(name))

    def static(self, ipv4addr, ipv4mask):
        logging.debug("In static() for EtherchannelInterfaces class.")
        self.ipv4 = {"static": {"address": ipv4addr, "netmask": ipv4mask}}

    def dhcp(self, enableDefault=True, routeMetric=1):
        logging.debug("In dhcp() for EtherchannelInterfaces class.")
        self.ipv4 = {"dhcp": {"enableDefaultRouteDHCP": enableDefault, "dhcpRouteMetric": routeMetric}}

    def p_interfaces(self, p_interfaces, device_name):
        logging.debug("In p_interfaces() for EtherchannelInterfaces class.")
        list = []
        for p_intf in p_interfaces:
            intf1 = PhysicalInterface(fmc=self.fmc)
            intf1.get(name=p_intf, device_name=device_name)
            if 'id' in intf1.__dict__:
                list.append({'name': intf1.name, 'id': intf1.id, 'type': intf1.type})
            else:
                logging.warning(
                    'PhysicalInterface, "{}", not found.  Cannot add to EtherchannelInterfaces.'.format(name))
        self.selectedInterfaces = list


class SubInterfaces(APIClassTemplate):
    """
    The Subinterface Object in the FMC.
    """
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\-\/\. ]"""
    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['name', 'subIntfId', 'MTU']
    REQUIRED_FOR_PUT = ['id', 'device_id']
    VALID_FOR_IPV4 = ['static', 'dhcp', 'pppoe']
    VALID_FOR_MODE = ['INLINE', 'PASSIVE', 'TAP', 'ERSPAN', 'NONE']
    VALID_FOR_MTU = range(64, 9000)

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SubInterfaces class.")
        self.parse_kwargs(**kwargs)
        self.type = "SubInterface"

    def format_data(self):
        logging.debug("In format_data() for SubInterfaces class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'mode' in self.__dict__:
            json_data['mode'] = self.mode
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'MTU' in self.__dict__:
            json_data['MTU'] = self.MTU
        if 'managementOnly' in self.__dict__:
            json_data['managementOnly'] = self.managementOnly
        if 'ipAddress' in self.__dict__:
            json_data['ipAddress'] = self.ipAddress
        if 'subIntfId' in self.__dict__:
            json_data['subIntfId'] = self.subIntfId
        if 'vlanId' in self.__dict__:
            json_data['vlanId'] = self.vlanId
        if 'macLearn' in self.__dict__:
            json_data['macLearn'] = self.macLearn
        if 'ifname' in self.__dict__:
            json_data['ifname'] = self.ifname
        if 'securityZone' in self.__dict__:
            json_data['securityZone'] = self.securityZone
        if 'arpConfig' in self.__dict__:
            json_data['arpConfig'] = self.arpConfig
        if 'ipv4' in self.__dict__:
            json_data['ipv4'] = self.ipv4
        if 'ipv6' in self.__dict__:
            json_data['ipv6'] = self.ipv6
        if 'macTable' in self.__dict__:
            json_data['macTable'] = self.macTable
        if 'enableAntiSpoofing' in self.__dict__:
            json_data['enableAntiSpoofing'] = self.enableAntiSpoofing
        if 'fragmentReassembly' in self.__dict__:
            json_data['fragmentReassembly'] = self.fragmentReassembly
        if 'enableDNSLookup' in self.__dict__:
            json_data['enableDNSLookup'] = self.enableDNSLookup
        if 'activeMACAddress' in self.__dict__:
            json_data['activeMACAddress'] = self.activeMACAddress
        if 'standbyMACAddress' in self.__dict__:
            json_data['standbyMACAddress'] = self.standbyMACAddress
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SubInterfaces class.")
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'ipv4' in kwargs:
            if list(kwargs['ipv4'].keys())[0] in self.VALID_FOR_IPV4:
                self.ipv4 = kwargs['ipv4']
            else:
                logging.warning('Method {} is not a valid ipv4 type.'.format(kwargs['ipv4']))
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'mode' in kwargs:
            if kwargs['mode'] in self.VALID_FOR_MODE:
                self.mode = kwargs['mode']
            else:
                logging.warning('Mode {} is not a valid mode.'.format(kwargs['mode']))
        if 'securityZone' in kwargs:
            self.securityZone = kwargs['securityZone']
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']
        if 'MTU' in kwargs:
            if kwargs['MTU'] in self.VALID_FOR_MTU:
                self.MTU = kwargs['MTU']
            else:
                logging.warning('MTU {} should be in the range 64-9000".'.format(kwargs['MTU']))
                self.MTU = 1500
        if 'managementOnly' in kwargs:
            self.managementOnly = kwargs['managementOnly']
        if 'ipAddress' in kwargs:
            self.ipAddress = kwargs['ipAddress']
        if 'subIntfId' in kwargs:
            self.subIntfId = kwargs['subIntfId']
        if 'vlanId' in kwargs:
            self.vlanId = kwargs['vlanId']
        if 'macLearn' in kwargs:
            self.macLearn = kwargs['macLearn']
        if 'ifname' in kwargs:
            self.ifname = kwargs['ifname']
        if 'arpConfig' in kwargs:
            self.arpConfig = kwargs['arpConfig']
        if 'ipv6' in kwargs:
            self.ipv6 = kwargs['ipv6']
        if 'macTable' in kwargs:
            self.macTable = kwargs['macTable']
        if 'enableAntiSpoofing' in kwargs:
            self.enableAntiSpoofing = kwargs['enableAntiSpoofing']
        if 'fragmentReassembly' in kwargs:
            self.fragmentReassembly = kwargs['fragmentReassembly']
        if 'enableDNSLookup' in kwargs:
            self.enableDNSLookup = kwargs['enableDNSLookup']
        if 'activeMACAddress' in kwargs:
            self.activeMACAddress = kwargs['activeMACAddress']
        if 'standbyMACAddress' in kwargs:
            self.standbyMACAddress = kwargs['standbyMACAddress']

    def device(self, device_name):
        logging.debug("In device() for SubInterfaces class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/subinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL, self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'SubInterfaces.'.format(device_name))

    def sz(self, name):
        logging.debug("In sz() for SubInterfaces class.")
        sz = SecurityZone(fmc=self.fmc)
        sz.get(name=name)
        if 'id' in sz.__dict__:
            new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
            self.securityZone = new_zone
        else:
            logging.warning('Security Zone, "{}", not found.  Cannot add to SubInterfaces.'.format(name))

    def static(self, ipv4addr, ipv4mask):
        logging.debug("In static() for SubInterfaces class.")
        self.ipv4 = {"static": {"address": ipv4addr, "netmask": ipv4mask}}

    def dhcp(self, enableDefault=True, routeMetric=1):
        logging.debug("In dhcp() for SubInterfaces class.")
        self.ipv4 = {"dhcp": {"enableDefaultRouteDHCP": enableDefault, "dhcpRouteMetric": routeMetric}}

    def p_interface(self, p_interface, device_name):
        logging.debug("In p_interface() for SubInterfaces class.")
        intf1 = PhysicalInterface(fmc=self.fmc)
        intf1.get(name=p_interface, device_name=device_name)
        if 'id' in intf1.__dict__:
            self.name = intf1.name
            if 'MTU' not in self.__dict__:
                self.MTU = intf1.MTU
        else:
            logging.warning('PhysicalInterface, "{}", not found.  Cannot add to SubInterfaces.'.format(name))


class StaticRoutes(APIClassTemplate):
    """
    The StaticRoutes Object in the FMC.
    """

    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for StaticRoutes class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for StaticRoutes class.")
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
        logging.debug("In parse_kwargs() for StaticRoutes class.")

    def device(self, device_name):
        logging.debug("In device() for StaticRoutes class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/routing/staticroutes'.format(self.fmc.configuration_url, self.PREFIX_URL,
                                                             self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'physicalInterface.'.format(device_name))

    def post(self):
        logging.info('POST method for API for StaticRoutes not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for StaticRoutes not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for StaticRoutes not supported.')
        pass


class IPv4StaticRoute(APIClassTemplate):
    """
    The IPv4StaticRoute Object in the FMC.
    """

    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['interfaceName', 'selectedNetworks', 'gateway']
    REQUIRED_FOR_PUT = ['id', 'device_id']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPv4StaticRoute class.")
        self.type = 'IPv4StaticRoute'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for IPv4StaticRoute class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'interfaceName' in self.__dict__:
            json_data['interfaceName'] = self.interfaceName
        if 'selectedNetworks' in self.__dict__:
            json_data['selectedNetworks'] = self.selectedNetworks
        if 'gateway' in self.__dict__:
            json_data['gateway'] = self.gateway
        if 'routeTracking' in self.__dict__:
            json_data['routeTracking'] = self.routeTracking
        if 'metricValue' in self.__dict__:
            json_data['metricValue'] = self.metricValue
        if 'isTunneled' in self.__dict__:
            json_data['isTunneled'] = self.isTunneled
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IPv4StaticRoute class.")
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'interfaceName' in kwargs:
            self.interfaceName = kwargs['interfaceName']
        if 'selectedNetworks' in kwargs:
            self.selectedNetworks = kwargs['selectedNetworks']
        if 'gateway' in kwargs:
            self.gateway = kwargs['gateway']
        if 'routeTracking' in kwargs:
            self.routeTracking = kwargs['routeTracking']
        if 'metricValue' in kwargs:
            self.metricValue = kwargs['metricValue']
        if 'isTunneled' in kwargs:
            self.isTunneled = kwargs['isTunneled']

    def device(self, device_name):
        logging.debug("In device() for IPv4StaticRoute class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/routing/ipv4staticroutes'.format(self.fmc.configuration_url, self.PREFIX_URL,
                                                                 self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'IPv4StaticRoute.'.format(device_name))

    def networks(self, action, networks):
        logging.info("In networks() for IPv4StaticRoute class.")
        if action == 'add':
            # Valid objects are IPHost, IPNetwork and NetworkGroup.  Create a dictionary to contain all three object type.
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
            for network in networks:
                # Find the matching object name in the dictionary if it exists
                net1 = list(filter(lambda i: i['name'] == network, items))
                if len(net1) > 0:
                    if 'selectedNetworks' in self.__dict__:
                        # Check to see if network already exists
                        exists = list(filter(lambda i: i['id'] == net1[0]['id'], self.selectedNetworks))
                        if 'id' in exists:
                            logging.warning('Network {} already exists in selectedNetworks.'.format(network))
                        else:
                            self.selectedNetworks.append(
                                {"type": net1[0]['type'], "id": net1[0]['id'], "name": net1[0]['name']})
                    else:
                        self.selectedNetworks = [
                            {"type": net1[0]['type'], "id": net1[0]['id'], "name": net1[0]['name']}]
                else:
                    logging.warning('Network {} not found.  Cannot set up device for '
                                    'IPv4StaticRoute.'.format(network))
        elif action == 'remove':
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
            for network in networks:
                net1 = list(filter(lambda i: i['name'] == network, items))
                if len(net1) > 0:
                    if 'selectedNetworks' in self.__dict__:
                        new_net1 = list(filter(lambda i: i['id'] != net1[0]['id'], self.selectedNetworks))
                    else:
                        logging.warning('No selectedNetworks found for this Device '
                                        'IPv4StaticRoute.'.format(network))
                else:
                    logging.warning('Network {} not found.  Cannot set up device for '
                                    'IPv4StaticRoute.'.format(network))
        elif action == 'clear':
            if 'selectedNetworks' in self.__dict__:
                del self.selectedNetworks
                logging.info('All selectedNetworks removed from this IPv4StaticRoute object.')

    def gw(self, name):
        logging.info("In gw() for IPv4StaticRoute class.")
        gw1 = IPHost(fmc=self.fmc)
        gw1.get(name=name)
        if 'id' in gw1.__dict__:
            self.gateway = {
                "object": {
                    "type": gw1.type,
                    "id": gw1.id,
                    "name": gw1.name}}
        else:
            logging.warning('Network {} not found.  Cannot set up device for '
                            'IPv4StaticRoute.'.format(name))

    def ipsla(self, name):
        logging.info("In ipsla() for IPv4StaticRoute class.")
        ipsla1 = SLAMonitor(fmc=self.fmc)
        ipsla1.get(name=name)
        if 'id' in ipsla1.__dict__:
            self.routeTracking = {
                "type": ipsla1.type,
                "id": ipsla1.id,
                "name": ipsla1.name}
        else:
            logging.warning('Object {} not found.  Cannot set up device for '
                            'IPv4StaticRoute.'.format(name))


class IPv6StaticRoute(APIClassTemplate):
    """
    The IPv6StaticRoute Object in the FMC.
    """

    PREFIX_URL = '/devices/devicerecords'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['interfaceName', 'selectedNetworks', 'gateway']
    REQUIRED_FOR_PUT = ['id', 'device_id']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IPv6StaticRoute class.")
        self.type = 'IPv6StaticRoute'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for IPv6StaticRoute class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'interfaceName' in self.__dict__:
            json_data['interfaceName'] = self.interfaceName
        if 'selectedNetworks' in self.__dict__:
            json_data['selectedNetworks'] = self.selectedNetworks
        if 'gateway' in self.__dict__:
            json_data['gateway'] = self.gateway
        if 'metricValue' in self.__dict__:
            json_data['metricValue'] = self.metricValue
        if 'isTunneled' in self.__dict__:
            json_data['isTunneled'] = self.isTunneled
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IPv6StaticRoute class.")
        if 'device_name' in kwargs:
            self.device(device_name=kwargs['device_name'])
        if 'interfaceName' in kwargs:
            self.interfaceName = kwargs['interfaceName']
        if 'selectedNetworks' in kwargs:
            self.selectedNetworks = kwargs['selectedNetworks']
        if 'gateway' in kwargs:
            self.gateway = kwargs['gateway']
        if 'metricValue' in kwargs:
            self.metricValue = kwargs['metricValue']
        if 'isTunneled' in kwargs:
            self.isTunneled = kwargs['isTunneled']

    def device(self, device_name):
        logging.debug("In device() for IPv6StaticRoute class.")
        device1 = Device(fmc=self.fmc)
        device1.get(name=device_name)
        if 'id' in device1.__dict__:
            self.device_id = device1.id
            self.URL = '{}{}/{}/routing/ipv6staticroutes'.format(self.fmc.configuration_url, self.PREFIX_URL,
                                                                 self.device_id)
            self.device_added_to_url = True
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'IPv6StaticRoute.'.format(device_name))

    def networks(self, action, networks):
        logging.info("In networks() for IPv6StaticRoute class.")
        if action == 'add':
            # Valid objects are IPHost, IPNetwork and NetworkGroup.  Create a dictionary to contain all three object type.
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
            for network in networks:
                # Find the matching object name in the dictionary if it exists
                net1 = list(filter(lambda i: i['name'] == network, items))
                if len(net1) > 0:
                    if 'selectedNetworks' in self.__dict__:
                        # Check to see if network already exists
                        exists = list(filter(lambda i: i['id'] == net1[0]['id'], self.selectedNetworks))
                        if 'id' in exists:
                            logging.warning('Network {} already exists in selectedNetworks.'.format(network))
                        else:
                            self.selectedNetworks.append(
                                {"type": net1[0]['type'], "id": net1[0]['id'], "name": net1[0]['name']})
                    else:
                        self.selectedNetworks = [
                            {"type": net1[0]['type'], "id": net1[0]['id'], "name": net1[0]['name']}]
                else:
                    logging.warning('Network {} not found.  Cannot set up device for '
                                    'IPv6StaticRoute.'.format(network))
        elif action == 'remove':
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
            for network in networks:
                net1 = list(filter(lambda i: i['name'] == network, items))
                if len(net1) > 0:
                    if 'selectedNetworks' in self.__dict__:
                        new_net1 = list(filter(lambda i: i['id'] != net1[0]['id'], self.selectedNetworks))
                    else:
                        logging.warning('No selectedNetworks found for this Device '
                                        'IPv6StaticRoute.'.format(network))
                else:
                    logging.warning('Network {} not found.  Cannot set up device for '
                                    'IPv6StaticRoute.'.format(network))
        elif action == 'clear':
            if 'selectedNetworks' in self.__dict__:
                del self.selectedNetworks
                logging.info('All selectedNetworks removed from this IPv6StaticRoute object.')

    def gw(self, name):
        logging.info("In gw() for IPv6StaticRoute class.")
        gw1 = IPHost(fmc=self.fmc)
        gw1.get(name=name)
        if 'id' in gw1.__dict__:
            self.gateway = {
                "object": {
                    "type": gw1.type,
                    "id": gw1.id,
                    "name": gw1.name}}
        else:
            logging.warning('Network {} not found.  Cannot set up device for '
                            'IPv6StaticRoute.'.format(name))


class DeviceGroups(APIClassTemplate):
    """
    The DeviceGroups Object in the FMC.
    """

    URL_SUFFIX = '/devicegroups/devicegrouprecords'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DeviceGroups class.")
        self.type = 'DeviceGroup'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for DeviceGroups class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'members' in self.__dict__:
            json_data['members'] = self.members
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DeviceGroups class.")
        if 'members' in kwargs:
            self.members = kwargs['members']

    def devices(self, action, members=[]):
        logging.debug("In devices() for DeviceGroups class.")
        if action == 'add':
            for member in members:
                if member["type"] == 'device':
                    dev1 = Device(fmc=self.fmc)
                    dev1.get(name=member["name"])
                elif member["type"] == 'deviceHAPair':
                    dev1 = DeviceHAPairs(fmc=self.fmc)
                    dev1.get(name=member["name"])
                if 'id' in dev1.__dict__:
                    if 'members' in self.__dict__:
                        self.members.append({"id":dev1.id, "type":dev1.type, "name":dev1.name})
                    else:
                        self.members = [{"id":dev1.id, "type":dev1.type, "name":dev1.name}]
                    logging.info('Device "{}" added to this DeviceGroup object.'.format(dev1.name))
                else:
                    logging.warning('{} not found.  Cannot add Device to DeviceGroup.'.format(member))
        elif action == 'remove':
            if 'members' in self.__dict__:
                for member in members:
                    if member["type"] == 'device':
                        dev1 = Device(fmc=self.fmc)
                        dev1.get(name=member["name"])
                    elif member["type"] == 'deviceHAPair':
                        dev1 = DeviceHAPairs(fmc=self.fmc)
                        dev1.get(name=member["name"])
                    if 'id' in dev1.__dict__:
                        if member["type"] == 'device':
                            self.members = list(filter(lambda i: i['id'] != dev1.id, self.members))
                        elif member["type"] == 'deviceHAPair':
                            devHA1 = DeviceHAPairs(fmc=self.fmc)
                            devHA1.get(name=member["name"])
                            self.members = list(filter(lambda i: i['id'] != devHA1.primary["id"], self.members))
                            self.members = list(filter(lambda i: i['id'] != devHA1.secondary["id"], self.members))
                    else:
                        logging.warning('Device {} not registered.  Cannot remove Device from DeviceGroup.'.format(member))
            else:
                logging.warning('DeviceGroup has no members.  Cannot remove Device.')
        elif action == 'clear':
            if 'members' in self.__dict__:
                del self.members
                logging.info('All devices removed from this DeviceGroup object.')


class DeviceHAPairs(APIClassTemplate):
    """
    The DeviceHAPairs Object in the FMC.
    """

    URL_SUFFIX = '/devicehapairs/ftddevicehapairs'
    REQUIRED_FOR_POST = ['primary', 'secondary', 'ftdHABootstrap']
    REQUIRED_FOR_PUT = ['id']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DeviceHAPairs class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for DeviceHAPairs class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'primary' in self.__dict__:
            json_data['primary'] = self.primary
        if 'secondary' in self.__dict__:
            json_data['secondary'] = self.secondary
        if 'ftdHABootstrap' in self.__dict__:
            json_data['ftdHABootstrap'] = self.ftdHABootstrap
        if 'action' in self.__dict__:
            json_data['action'] = self.action
        if 'forceBreak' in self.__dict__:
            json_data['forceBreak'] = self.forceBreak
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DeviceHAPairs class.")
        if 'primary' in kwargs:
            self.primary = kwargs['primary']
        if 'secondary' in kwargs:
            self.secondary = kwargs['secondary']
        if 'ftdHABootstrap' in kwargs:
            self.ftdHABootstrap = kwargs['ftdHABootstrap']
        if 'action' in kwargs:
            self.action = kwargs['action']
        if 'forceBreak' in kwargs:
            self.forceBreak = kwargs['forceBreak']

    def device(self, primary_name="", secondary_name=""):
        logging.debug("In device() for DeviceHAPairs class.")
        primary = Device(fmc=self.fmc)
        primary.get(name=primary_name)
        secondary = Device(fmc=self.fmc)
        secondary.get(name=secondary_name)
        if 'id' in primary.__dict__:
            self.primary_id = primary.id
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'DeviceHAPairs.'.format(primary_name))
        if 'id' in secondary.__dict__:
            self.secondary_id = secondary.id
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'DeviceHAPairs.'.format(secondary_name))

    def primary(self, name):
        logging.debug("In primary() for DeviceHAPairs class.")
        primary = Device(fmc=self.fmc)
        primary.get(name=name)
        if 'id' in primary.__dict__:
            self.primary = {"id": primary.id}
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'DeviceHAPairs.'.format(primary_name))

    def secondary(self, name):
        logging.debug("In secondary() for DeviceHAPairs class.")
        secondary = Device(fmc=self.fmc)
        secondary.get(name=name)
        if 'id' in secondary.__dict__:
            self.secondary = {"id": secondary.id}
        else:
            logging.warning('Device {} not found.  Cannot set up device for '
                            'DeviceHAPairs.'.format(primary_name))

    def switch_ha(self):
        logging.debug("In switch_ha() for DeviceHAPairs class.")
        ha1 = DeviceHAPairs(fmc=self.fmc)
        ha1.get(name=self.name)
        if 'id' in ha1.__dict__:
            self.id = ha1.id
            self.action = "SWITCH"
        else:
            logging.warning('DeviceHAPair {} not found.  Cannot set up HA for SWITCH.'.format(self.name))

    def break_ha(self):
        logging.debug("In break_ha() for DeviceHAPairs class.")
        ha1 = DeviceHAPairs(fmc=self.fmc)
        ha1.get(name=self.name)
        if 'id' in ha1.__dict__:
            self.id = ha1.id
            self.action = "HABREAK"
            self.forceBreak = True
        else:
            logging.warning('DeviceHAPair {} not found.  Cannot set up HA for BREAK.'.format(self.name))

    def post(self, **kwargs):
        logging.debug("In post() for DeviceHAPairs class.")
        # Attempting to "Deploy" during Device registration causes issues.
        self.fmc.autodeploy = False
        return super().post(**kwargs)

    def put(self, **kwargs):
        logging.debug("In put() for DeviceHAPairs class.")
        # Attempting to "Deploy" during Device registration causes issues.
        self.fmc.autodeploy = False
        return super().put(**kwargs)

class DeviceHAMonitoredInterfaces(APIClassTemplate):
    """
    The DeviceHAMonitoredInterfaces Object in the FMC.
    """

    PREFIX_URL = '/devicehapairs/ftddevicehapairs'
    REQUIRED_FOR_PUT = ['id']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DeviceHAMonitoredInterfaces class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for DeviceHAMonitoredInterfaces class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'ipv4Configuration' in self.__dict__:
            json_data['ipv4Configuration'] = self.ipv4Configuration
        if 'ipv6Configuration' in self.__dict__:
            json_data['ipv6Configuration'] = self.ipv6Configuration
        if 'monitorForFailures' in self.__dict__:
            json_data['monitorForFailures'] = self.monitorForFailures
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DeviceHAMonitoredInterfaces class.")
        if 'ha_name' in kwargs:
            self.device_ha(ha_name=kwargs['ha_name'])
        if 'ipv4Configuration' in kwargs:
            self.ipv4Configuration = kwargs['ipv4Configuration']
        if 'ipv6Configuration' in kwargs:
            self.ipv6Configuration = kwargs['ipv6Configuration']
        if 'monitorForFailures' in kwargs:
            self.monitorForFailures = kwargs['monitorForFailures']

    def device_ha(self, ha_name):
        logging.debug("In device_ha() for DeviceHAMonitoredInterfaces class.")
        deviceha1 = DeviceHAPairs(fmc=self.fmc, name=ha_name)
        deviceha1.get()
        if 'id' in deviceha1.__dict__:
            self.deviceha_id = deviceha1.id
            self.URL = '{}{}/{}/monitoredinterfaces'.format(self.fmc.configuration_url, self.PREFIX_URL, self.deviceha_id)
            self.deviceha_added_to_url = True
        else:
            logging.warning('Device HA {} not found.  Cannot set up device for '
                            'DeviceHAMonitoredInterfaces.'.format(ha_name))

    def ipv4(self, ipv4addr, ipv4mask, ipv4standbyaddr):
        logging.debug("In ipv4() for DeviceHAMonitoredInterfaces class.")
        self.ipv4Configuration = {
            "activeIPv4Address": ipv4addr,
            "activeIPv4Mask": ipv4mask,
            "standbyIPv4Address": ipv4standbyaddr}

    def post(self):
        logging.info('POST method for API for DeviceHAMonitoredInterfaces not supported.')
        pass

class DeviceHAFailoverMAC(APIClassTemplate):
    """
    The DeviceHAFailoverMAC Object in the FMC.
    """

    PREFIX_URL = '/devicehapairs/ftddevicehapairs'
    REQUIRED_FOR_POST = ['physicalInterface', 'failoverActiveMac', 'failoverStandbyMac']
    REQUIRED_FOR_PUT = ['id']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DeviceHAFailoverMAC class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for DeviceHAFailoverMAC class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'physicalInterface' in self.__dict__:
            json_data['physicalInterface'] = self.physicalInterface
        if 'failoverActiveMac' in self.__dict__:
            json_data['failoverActiveMac'] = self.failoverActiveMac
        if 'failoverStandbyMac' in self.__dict__:
            json_data['failoverStandbyMac'] = self.failoverStandbyMac
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DeviceHAFailoverMAC class.")
        if 'ha_name' in kwargs:
            self.device_ha(ha_name=kwargs['ha_name'])
        if 'physicalInterface' in kwargs:
            self.physicalInterface = kwargs['physicalInterface']
        if 'failoverActiveMac' in kwargs:
            self.failoverActiveMac = kwargs['failoverActiveMac']
        if 'failoverStandbyMac' in kwargs:
            self.failoverStandbyMac = kwargs['failoverStandbyMac']

    def device_ha(self, ha_name):
        logging.debug("In device_ha() for DeviceHAFailoverMAC class.")
        deviceha1 = DeviceHAPairs(fmc=self.fmc, name=ha_name)
        deviceha1.get()
        if 'id' in deviceha1.__dict__:
            self.deviceha_id = deviceha1.id
            self.URL = '{}{}/{}/failoverinterfacemacaddressconfigs'.format(self.fmc.configuration_url, self.PREFIX_URL, self.deviceha_id)
            self.deviceha_added_to_url = True
        else:
            logging.warning('Device HA {} not found.  Cannot set up device for '
                            'DeviceHAFailoverMAC.'.format(ha_name))

    def p_interface(self, name, device_name):
        logging.debug("In p_interface() for DeviceHAFailoverMAC class.")
        intf1 = PhysicalInterface(fmc=self.fmc)
        intf1.get(name=name,device_name=device_name)
        if 'id' in intf1.__dict__:
            self.physicalInterface = {'name': intf1.name, 'id': intf1.id, 'type': intf1.type}
        else:
            logging.warning('PhysicalInterface, "{}", not found.  Cannot add to DeviceHAFailoverMAC.'.format(name))

    def edit(self, name, ha_name):
        logging.debug("In edit() for DeviceHAFailoverMAC class.")
        deviceha1 = DeviceHAPairs(fmc=self.fmc, name=ha_name)
        deviceha1.get()
        obj1 = DeviceHAFailoverMAC(fmc=self.fmc)
        obj1.device_ha(ha_name=ha_name)
        failovermac_json = obj1.get()
        items = failovermac_json.get('items', [])
        found = False
        for item in items:
            if item['physicalInterface']['name'] == name:
                found = True
                self.id = item['id']
                self.name = item['physicalInterface']['name']
                self.failoverActiveMac = item['failoverActiveMac']
                self.failoverStandbyMac = item['failoverStandbyMac']
                self.deviceha_id = deviceha1.id
                self.URL = '{}{}/{}/failoverinterfacemacaddressconfigs'.format(self.fmc.configuration_url, self.PREFIX_URL, self.deviceha_id)
                break
        if found is False:
            logging.warning('PhysicalInterface, "{}", not found.  Cannot add to DeviceHAFailoverMAC.'.format(name))
