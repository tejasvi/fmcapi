"""
This module contains the "policy" class objects that represent the various objects in the FMC.
"""

from .api_template import *
from .helper_functions import *
from .api_template import *
from .devices import *
from .misc import *
from .objects import *
from .policy import *


class IntrusionPolicy(APIClassTemplate):
    """
    The Intrusion Policy Object in the FMC.
    """

    URL_SUFFIX = '/policy/intrusionpolicies'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IntrusionPolicy class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for IntrusionPolicy class.")
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
        logging.debug("In parse_kwargs() for IntrusionPolicy class.")

    def post(self):
        logging.info('POST method for API for IntrusionPolicy not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for IntrusionPolicy not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for IntrusionPolicy not supported.')
        pass


class AccessControlPolicy(APIClassTemplate):
    """
    The Access Control Policy Object in the FMC.
    """

    URL_SUFFIX = '/policy/accesspolicies'
    REQUIRED_FOR_POST = ['name']
    DEFAULT_ACTION_OPTIONS = ['BLOCK', 'NETWORK_DISCOVERY', 'IPS']  # Not implemented yet.
    FILTER_BY_NAME = True

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for AccessControlPolicy class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for AccessControlPolicy class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'description' in self.__dict__:
            json_data['description'] = self.description
        if 'defaultAction' in self.__dict__:
            json_data['defaultAction'] = self.defaultAction
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for AccessControlPolicy class.")
        if 'defaultAction' in kwargs:
            self.defaultAction = kwargs['defaultAction']
        else:
            self.defaultAction = {'action': 'BLOCK'}

    def put(self, **kwargs):
        logging.info('The put() method for the AccessControlPolicy() class can work but I need to write a '
                     'DefaultAction() class and accommodate for such before "putting".')
        pass


class ACPRule(APIClassTemplate):
    """
    The ACP Rule Object in the FMC.
    """

    PREFIX_URL = '/policy/accesspolicies'
    URL_SUFFIX = None
    REQUIRED_FOR_POST = ['name', 'acp_id']
    VALID_FOR_ACTION = ['ALLOW', 'TRUST', 'BLOCK', 'MONITOR', 'BLOCK_RESET', 'BLOCK_INTERACTIVE',
                        'BLOCK_RESET_INTERACTIVE']
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ACPRule class.")
        self.type = 'AccessRule'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ACPRule class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'action' in self.__dict__:
            json_data['action'] = self.action
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        if 'sendEventsToFMC' in self.__dict__:
            json_data['sendEventsToFMC'] = self.sendEventsToFMC
        if 'logFiles' in self.__dict__:
            json_data['logFiles'] = self.logFiles
        if 'logBegin' in self.__dict__:
            json_data['logBegin'] = self.logBegin
        if 'logEnd' in self.__dict__:
            json_data['logEnd'] = self.logEnd
        if 'variableSet' in self.__dict__:
            json_data['variableSet'] = self.variableSet
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'originalSourceNetworks' in self.__dict__:
            json_data['originalSourceNetworks'] = self.originalSourceNetworks
        if 'vlanTags' in self.__dict__:
            json_data['vlanTags'] = self.vlanTags
        if 'sourceNetworks' in self.__dict__:
            json_data['sourceNetworks'] = self.sourceNetworks
        if 'destinationNetworks' in self.__dict__:
            json_data['destinationNetworks'] = self.destinationNetworks
        if 'sourcePorts' in self.__dict__:
            json_data['sourcePorts'] = self.sourcePorts
        if 'destinationPorts' in self.__dict__:
            json_data['destinationPorts'] = self.destinationPorts
        if 'ipsPolicy' in self.__dict__:
            json_data['ipsPolicy'] = self.ipsPolicy
        if 'urls' in self.__dict__:
            json_data['urls'] = self.urls
        if 'sourceZones' in self.__dict__:
            json_data['sourceZones'] = self.sourceZones
        if 'destinationZones' in self.__dict__:
            json_data['destinationZones'] = self.destinationZones
        if 'applications' in self.__dict__:
            json_data['applications'] = self.applications
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ACPRule class.")
        if 'action' in kwargs:
            if kwargs['action'] in self.VALID_FOR_ACTION:
                self.action = kwargs['action']
            else:
                logging.warning('Action {} is not a valid action.'.format(kwargs['action']))
        else:
            self.action = 'BLOCK'
        if 'acp_name' in kwargs:
            self.acp(name=kwargs['acp_name'])
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']
        else:
            self.enabled = True
        if 'sendEventsToFMC' in kwargs:
            self.sendEventsToFMC = kwargs['sendEventsToFMC']
        else:
            self.sendEventsToFMC = True
        if 'logFiles' in kwargs:
            self.logFiles = kwargs['logFiles']
        else:
            self.logFiles = False
        if 'logBegin' in kwargs:
            self.logBegin = kwargs['logBegin']
        else:
            self.logBegin = False
        if 'logEnd' in kwargs:
            self.logEnd = kwargs['logEnd']
        else:
            self.logEnd = False
        if 'originalSourceNetworks' in kwargs:
            self.originalSourceNetworks = kwargs['originalSourceNetworks']
        if 'sourceZones' in kwargs:
            self.sourceZones = kwargs['sourceZones']
        if 'destinationZones' in kwargs:
            self.destinationZones = kwargs['destinationZones']
        if 'variableSet' in kwargs:
            self.variableSet = kwargs['variableSet']
        else:
            self.variable_set(action='set')
        if 'ipsPolicy' in kwargs:
            self.ipsPolicy = kwargs['ipsPolicy']
        if 'vlanTags' in kwargs:
            self.vlanTags = kwargs['vlanTags']
        if 'sourcePorts' in kwargs:
            self.sourcePorts = kwargs['sourcePorts']
        if 'destinationPorts' in kwargs:
            self.destinationPorts = kwargs['destinationPorts']
        if 'sourceNetworks' in kwargs:
            self.sourceNetworks = kwargs['sourceNetworks']
        if 'destinationNetworks' in kwargs:
            self.destinationNetworks = kwargs['destinationNetworks']
        if 'urls' in kwargs:
            self.urls = kwargs['urls']
        if 'applications' in kwargs:
            self.applications = kwargs['applications']

    def acp(self, name):
        logging.debug("In acp() for ACPRule class.")
        acp1 = AccessControlPolicy(fmc=self.fmc)
        acp1.get(name=name)
        if 'id' in acp1.__dict__:
            self.acp_id = acp1.id
            self.URL = '{}{}/{}/accessrules'.format(self.fmc.configuration_url, self.PREFIX_URL, self.acp_id)
            self.acp_added_to_url = True
        else:
            logging.warning('Access Control Policy {} not found.  Cannot set up accessPolicy for '
                            'ACPRule.'.format(name))

    def intrusion_policy(self, action, name=''):
        logging.debug("In intrusion_policy() for ACPRule class.")
        if action == 'clear':
            if 'ipsPolicy' in self.__dict__:
                del self.ipsPolicy
                logging.info('Intrusion Policy removed from this ACPRule object.')
        elif action == 'set':
            ips = IntrusionPolicy(fmc=self.fmc, name=name)
            ips.get()
            self.ipsPolicy = {'name': ips.name, 'id': ips.id, 'type': ips.type}
            logging.info('Intrusion Policy set to "{}" for this ACPRule object.'.format(name))

    def variable_set(self, action, name='Default-Set'):
        logging.debug("In variable_set() for ACPRule class.")
        if action == 'clear':
            if 'variableSet' in self.__dict__:
                del self.variableSet
                logging.info('Variable Set removed from this ACPRule object.')
        elif action == 'set':
            vs = VariableSet(fmc=self.fmc)
            vs.get(name=name)
            self.variableSet = {'name': vs.name, 'id': vs.id, 'type': vs.type}
            logging.info('VariableSet set to "{}" for this ACPRule object.'.format(name))

    def source_zone(self, action, name=''):
        logging.debug("In source_zone() for ACPRule class.")
        if action == 'add':
            sz = SecurityZone(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                if 'sourceZones' in self.__dict__:
                    new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
                    duplicate = False
                    for obj in self.sourceZones['objects']:
                        if obj['name'] == new_zone['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.sourceZones['objects'].append(new_zone)
                        logging.info('Adding "{}" to sourceZones for this ACPRule.'.format(name))
                else:
                    self.sourceZones = {'objects': [{'name': sz.name, 'id': sz.id, 'type': sz.type}]}
                    logging.info('Adding "{}" to sourceZones for this ACPRule.'.format(name))
            else:
                logging.warning('Security Zone, "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'remove':
            sz = SecurityZone(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                if 'sourceZones' in self.__dict__:
                    objects = []
                    for obj in self.sourceZones['objects']:
                        if obj['name'] != name:
                            objects.append(obj)
                    self.sourceZones['objects'] = objects
                    logging.info('Removed "{}" from sourceZones for this ACPRule.'.format(name))
                else:
                    logging.info("sourceZones doesn't exist for this ACPRule.  Nothing to remove.")
            else:
                logging.warning('Security Zone, "{}", not found.  Cannot remove from ACPRule.'.format(name))
        elif action == 'clear':
            if 'sourceZones' in self.__dict__:
                del self.sourceZones
                logging.info('All Source Zones removed from this ACPRule object.')

    def destination_zone(self, action, name=''):
        logging.debug("In destination_zone() for ACPRule class.")
        if action == 'add':
            sz = SecurityZone(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                if 'destinationZones' in self.__dict__:
                    new_zone = {'name': sz.name, 'id': sz.id, 'type': sz.type}
                    duplicate = False
                    for obj in self.destinationZones['objects']:
                        if obj['name'] == new_zone['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.destinationZones['objects'].append(new_zone)
                        logging.info('Adding "{}" to destinationZones for this ACPRule.'.format(name))
                else:
                    self.destinationZones = {'objects': [{'name': sz.name, 'id': sz.id, 'type': sz.type}]}
                    logging.info('Adding "{}" to destinationZones for this ACPRule.'.format(name))
            else:
                logging.warning('Security Zone, "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'remove':
            sz = SecurityZone(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                if 'destinationZones' in self.__dict__:
                    objects = []
                    for obj in self.destinationZones['objects']:
                        if obj['name'] != name:
                            objects.append(obj)
                    self.destinationZones['objects'] = objects
                    logging.info('Removed "{}" from destinationZones for this ACPRule.'.format(name))
                else:
                    logging.info("destinationZones doesn't exist for this ACPRule.  Nothing to remove.")
            else:
                logging.warning('Security Zone, {}, not found.  Cannot remove from ACPRule.'.format(name))
        elif action == 'clear':
            if 'destinationZones' in self.__dict__:
                del self.destinationZones
                logging.info('All Destination Zones removed from this ACPRule object.')

    def vlan_tags(self, action, name=''):
        logging.debug("In vlan_tags() for ACPRule class.")
        if action == 'add':
            vlantag = VlanTag(fmc=self.fmc)
            vlantag.get(name=name)
            if 'id' in vlantag.__dict__:
                if 'vlanTags' in self.__dict__:
                    new_vlan = {'name': vlantag.name, 'id': vlantag.id, 'type': vlantag.type}
                    duplicate = False
                    for obj in self.vlanTags['objects']:
                        if obj['name'] == new_vlan['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.vlanTags['objects'].append(new_vlan)
                        logging.info('Adding "{}" to vlanTags for this ACPRule.'.format(name))
                else:
                    self.vlanTags = {'objects': [{'name': vlantag.name, 'id': vlantag.id, 'type': vlantag.type}]}
                    logging.info('Adding "{}" to vlanTags for this ACPRule.'.format(name))
            else:
                logging.warning('VLAN Tag, "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'remove':
            vlantag = VlanTag(fmc=self.fmc)
            vlantag.get(name=name)
            if 'id' in vlantag.__dict__:
                if 'vlanTags' in self.__dict__:
                    objects = []
                    for obj in self.vlanTags['objects']:
                        if obj['name'] != name:
                            objects.append(obj)
                    self.vlanTags['objects'] = objects
                    logging.info('Removed "{}" from vlanTags for this ACPRule.'.format(name))
                else:
                    logging.info("vlanTags doesn't exist for this ACPRule.  Nothing to remove.")
            else:
                logging.warning('VLAN Tag, {}, not found.  Cannot remove from ACPRule.'.format(name))
        elif action == 'clear':
            if 'vlanTags' in self.__dict__:
                del self.vlanTags
                logging.info('All VLAN Tags removed from this ACPRule object.')

    def source_port(self, action, name=''):
        logging.debug("In source_port() for ACPRule class.")
        if action == 'add':
            pport_json = ProtocolPort(fmc=self.fmc)
            pport_json.get(name=name)
            if 'id' in pport_json.__dict__:
                item = pport_json
            else:
                item = PortObjectGroup(fmc=self.fmc)
                item.get(name=name)
            if 'id' in item.__dict__:
                if 'sourcePorts' in self.__dict__:
                    new_port = {'name': item.name, 'id': item.id, 'type': item.type}
                    duplicate = False
                    for obj in self.sourcePorts['objects']:
                        if obj['name'] == new_port['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.sourcePorts['objects'].append(new_port)
                        logging.info('Adding "{}" to sourcePorts for this ACPRule.'.format(name))
                else:
                    self.sourcePorts = {'objects': [{'name': item.name, 'id': item.id, 'type': item.type}]}
                    logging.info('Adding "{}" to sourcePorts for this ACPRule.'.format(name))
            else:
                logging.warning('Protocol Port or Protocol Port Group: "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'remove':
            pport_json = ProtocolPort(fmc=self.fmc)
            pport_json.get(name=name)
            if 'id' in pport_json.__dict__:
                item = pport_json
            else:
                item = PortObjectGroup(fmc=self.fmc)
                item.get(name=name)
            if 'id' in item.__dict__:
                if 'sourcePorts' in self.__dict__:
                    objects = []
                    for obj in self.sourcePorts['objects']:
                        if obj['name'] != name:
                            objects.append(obj)
                    self.sourcePorts['objects'] = objects
                    logging.info('Removed "{}" from sourcePorts for this ACPRule.'.format(name))
                else:
                    logging.info("sourcePorts doesn't exist for this ACPRule.  Nothing to remove.")
            else:
                logging.warning('Protocol Port or Protocol Port Group: "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'clear':
            if 'sourcePorts' in self.__dict__:
                del self.sourcePorts
                logging.info('All Source Ports removed from this ACPRule object.')

    def destination_port(self, action, name=''):
        logging.debug("In destination_port() for ACPRule class.")
        if action == 'add':
            pport_json = ProtocolPort(fmc=self.fmc)
            pport_json.get(name=name)
            if 'id' in pport_json.__dict__:
                item = pport_json
            else:
                item = PortObjectGroup(fmc=self.fmc)
                item.get(name=name)
            if 'id' in item.__dict__:
                if 'destinationPorts' in self.__dict__:
                    new_port = {'name': item.name, 'id': item.id, 'type': item.type}
                    duplicate = False
                    for obj in self.destinationPorts['objects']:
                        if obj['name'] == new_port['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.destinationPorts['objects'].append(new_port)
                        logging.info('Adding "{}" to destinationPorts for this ACPRule.'.format(name))
                else:
                    self.destinationPorts = {'objects': [{'name': item.name, 'id': item.id, 'type': item.type}]}
                    logging.info('Adding "{}" to destinationPorts for this ACPRule.'.format(name))
            else:
                logging.warning('Protocol Port or Protocol Port Group: "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'remove':
            pport_json = ProtocolPort(fmc=self.fmc)
            pport_json.get(name=name)
            if 'id' in pport_json.__dict__:
                item = pport_json
            else:
                item = PortObjectGroup(fmc=self.fmc)
                item.get(name=name)
            if 'id' in item.__dict__:
                if 'destinationPorts' in self.__dict__:
                    objects = []
                    for obj in self.destinationPorts['objects']:
                        if obj['name'] != name:
                            objects.append(obj)
                    self.destinationPorts['objects'] = objects
                    logging.info('Removed "{}" from destinationPorts for this ACPRule.'.format(name))
                else:
                    logging.info("destinationPorts doesn't exist for this ACPRule.  Nothing to remove.")
            else:
                logging.warning('Protocol Port or Protocol Port Group: "{}", not found.  Cannot add to ACPRule.'.format(name))
        elif action == 'clear':
            if 'destinationPorts' in self.__dict__:
                del self.destinationPorts
                logging.info('All Destination Ports removed from this ACPRule object.')

    def source_network(self, action, name=''):
        logging.debug("In source_network() for ACPRule class.")
        if action == 'add':
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            fqdns_json = FQDNS(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', []) + fqdns_json.get('items', [])
            new_net = None
            for item in items:
                if item['name'] == name:
                    new_net = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                    break
            if new_net is None:
                logging.warning('Network "{}" is not found in FMC.  Cannot add to sourceNetworks.'.format(name))
            else:
                if 'sourceNetworks' in self.__dict__:
                    duplicate = False
                    for obj in self.sourceNetworks['objects']:
                        if obj['name'] == new_net['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.sourceNetworks['objects'].append(new_net)
                        logging.info('Adding "{}" to sourceNetworks for this ACPRule.'.format(name))
                else:
                    self.sourceNetworks = {'objects': [new_net]}
                    logging.info('Adding "{}" to sourceNetworks for this ACPRule.'.format(name))
        elif action == 'remove':
            if 'sourceNetworks' in self.__dict__:
                objects = []
                for obj in self.sourceNetworks['objects']:
                    if obj['name'] != name:
                        objects.append(obj)
                self.sourceNetworks['objects'] = objects
                logging.info('Removed "{}" from sourceNetworks for this ACPRule.'.format(name))
            else:
                logging.info("sourceNetworks doesn't exist for this ACPRule.  Nothing to remove.")
        elif action == 'clear':
            if 'sourceNetworks' in self.__dict__:
                del self.sourceNetworks
                logging.info('All Source Networks removed from this ACPRule object.')

    def destination_network(self, action, name=''):
        logging.debug("In destination_network() for ACPRule class.")
        if action == 'add':
            ipaddresses_json = IPAddresses(fmc=self.fmc).get()
            networkgroup_json = NetworkGroup(fmc=self.fmc).get()
            fqdns_json = FQDNS(fmc=self.fmc).get()
            items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', []) + fqdns_json.get('items', [])
            new_net = None
            for item in items:
                if item['name'] == name:
                    new_net = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                    break
            if new_net is None:
                logging.warning('Network "{}" is not found in FMC.  Cannot add to '
                                'destinationNetworks.'.format(name))
            else:
                if 'destinationNetworks' in self.__dict__:
                    duplicate = False
                    for obj in self.destinationNetworks['objects']:
                        if obj['name'] == new_net['name']:
                            duplicate = True
                            break
                    if not duplicate:
                        self.destinationNetworks['objects'].append(new_net)
                        logging.info('Adding "{}" to destinationNetworks for this ACPRule.'.format(name))
                else:
                    self.destinationNetworks = {'objects': [new_net]}
                    logging.info('Adding "{}" to destinationNetworks for this ACPRule.'.format(name))
        elif action == 'remove':
            if 'destinationNetworks' in self.__dict__:
                objects = []
                for obj in self.destinationNetworks['objects']:
                    if obj['name'] != name:
                        objects.append(obj)
                self.destinationNetworks['objects'] = objects
                logging.info('Removed "{}" from destinationNetworks for this ACPRule.'.format(name))
            else:
                logging.info("destinationNetworks doesn't exist for this ACPRule.  Nothing to remove.")
        elif action == 'clear':
            if 'destinationNetworks' in self.__dict__:
                del self.destinationNetworks
                logging.info('All Destination Networks removed from this ACPRule object.')


class FTDNatPolicy(APIClassTemplate):
    """
    The FTDNATPolicy Object in the FMC.
    """

    URL_SUFFIX = '/policy/ftdnatpolicies'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for FTDNatPolicy class.")
        self.parse_kwargs(**kwargs)
        self.type = "FTDNatPolicy"

    def format_data(self):
        logging.debug("In format_data() for FTDNatPolicy class.")
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
        logging.debug("In parse_kwargs() for FTDNatPolicy class.")

class AutoNatRules(APIClassTemplate):
    """
    The AutoNatRules Object in the FMC.
    """

    PREFIX_URL = '/policy/ftdnatpolicies'
    REQUIRED_FOR_POST = ["nat_id"]

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for AutoNatRules class.")
        self.parse_kwargs(**kwargs)
        self.type = "FTDAutoNatRule"

    def format_data(self):
        logging.debug("In format_data() for AutoNatRules class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'originalNetwork' in self.__dict__:
            json_data['originalNetwork'] = self.originalNetwork
        if 'translatedNetwork' in self.__dict__:
            json_data['translatedNetwork'] = self.translatedNetwork
        if 'interfaceInTranslatedNetwork' in self.__dict__:
            json_data['interfaceInTranslatedNetwork'] = self.interfaceInTranslatedNetwork
        if 'natType' in self.__dict__:
            json_data['natType'] = self.natType
        if 'interfaceIpv6' in self.__dict__:
            json_data['interfaceIpv6'] = self.interfaceIpv6
        if 'fallThrough' in self.__dict__:
            json_data['fallThrough'] = self.fallThrough
        if 'dns' in self.__dict__:
            json_data['dns'] = self.dns
        if 'routeLookup' in self.__dict__:
            json_data['routeLookup'] = self.routeLookup
        if 'noProxyArp' in self.__dict__:
            json_data['noProxyArp'] = self.noProxyArp
        if 'netToNet' in self.__dict__:
            json_data['netToNet'] = self.netToNet
        if 'sourceInterface' in self.__dict__:
            json_data['sourceInterface'] = self.sourceInterface
        if 'destinationInterface' in self.__dict__:
            json_data['destinationInterface'] = self.destinationInterface
        if 'originalPort' in self.__dict__:
            json_data['originalPort'] = self.originalPort
        if 'translatedPort' in self.__dict__:
            json_data['translatedPort'] = self.translatedPort
        if 'serviceProtocol' in self.__dict__:
            json_data['serviceProtocol'] = self.serviceProtocol
        if 'patOptions' in self.__dict__:
            json_data['patOptions'] = self.patOptions
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for AutoNatRules class.")
        if 'originalNetwork' in kwargs:
            self.originalNetwork = kwargs['originalNetwork']
        if 'translatedNetwork' in kwargs and 'interfaceInTranslatedNetwork' is True:
            logging.warning("Cannot have both a translatedNetwork and interfaceInTranslatedNetwork")
        elif 'translatedNetwork' in kwargs:
            self.translatedNetwork = kwargs['translatedNetwork']
        elif 'interfaceInTranslatedNetwork' in kwargs:
            self.interfaceInTranslatedNetwork = kwargs['interfaceInTranslatedNetwork']
        if 'natType' in kwargs:
            self.natType = kwargs['natType']
        if 'interfaceIpv6' in kwargs:
            self.interfaceIpv6 = kwargs['interfaceIpv6']
        if 'fallThrough' in kwargs:
            self.fallThrough = kwargs['fallThrough']
        if 'dns' in kwargs:
            self.dns = kwargs['dns']
        if 'routeLookup' in kwargs:
            self.routeLookup = kwargs['routeLookup']
        if 'noProxyArp' in kwargs:
            self.noProxyArp = kwargs['noProxyArp']
        if 'netToNet' in kwargs:
            self.netToNet = kwargs['netToNet']
        if 'sourceInterface' in kwargs:
            self.sourceInterface = kwargs['sourceInterface']
        if 'destinationInterface' in kwargs:
            self.destinationInterface = kwargs['destinationInterface']
        if 'originalPort' in kwargs:
            self.originalPort = kwargs['originalPort']
        if 'translatedPort' in kwargs:
            self.translatedPort = kwargs['translatedPort']
        if 'serviceProtocol' in kwargs:
            self.serviceProtocol = kwargs['serviceProtocol']
        if 'patOptions' in kwargs:
            self.patOptions = kwargs['patOptions']

    def nat_policy(self,name):
        logging.debug("In nat_policy() for AutoNatRules class.")
        ftd_nat = FTDNatPolicy(fmc=self.fmc)
        ftd_nat.get(name=name)
        if 'id' in ftd_nat.__dict__:
            self.nat_id = ftd_nat.id
            self.URL = '{}{}/{}/autonatrules'.format(self.fmc.configuration_url, self.PREFIX_URL, self.nat_id)
            self.nat_added_to_url = True
        else:
            logging.warning('FTD NAT Policy {} not found.  Cannot set up AutoNatRule for '
                            'NAT Policy.'.format(name))

    def original_network(self, name):
        logging.debug("In original_network() for AutoNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to originalNetwork.'.format(name))
        else:
            self.originalNetwork = new_net
            logging.info('Adding "{}" to sourceNetworks for this AutoNatRule.'.format(name))

    def translated_network(self,name):
        #Auto Nat rules can't use network group objects
        logging.debug("In translated_network() for AutoNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to translatedNetwork.'.format(name))
        else:
            self.translatedNetwork = new_net
            logging.info('Adding "{}" to destinationNetworks for this AutoNatRule.'.format(name))

    def source_intf(self,name):
        logging.debug("In source_intf() for AutoNatRules class.")
        intf_obj = InterfaceObject(fmc=self.fmc).get()
        items = intf_obj.get('items', [])
        new_intf = None
        for item in items:
            if item["name"] == name:
                new_intf = {'id': item['id'], 'type': item['type']}
                break
        if new_intf == None:
            logging.warning('Interface Object "{}" is not found in FMC.  Cannot add to sourceInterface.'.format(name))
        else:
            if new_intf.type == "InterfaceGroup" and len(new_intf.interfaces) > 1:
                logging.warning('Interface Object "{}" contains more than one physical interface.  Cannot add to sourceInterface.'.format(name))
            else:
                self.sourceInterface = new_intf
                logging.info('Interface Object "{}" added to NAT Policy.'.format(name))

    def destination_intf(self,name):
        logging.debug("In destination_intf() for AutoNatRules class.")
        intf_obj = InterfaceObject(fmc=self.fmc).get()
        items = intf_obj.get('items', [])
        new_intf = None
        for item in items:
            if item["name"] == name:
                new_intf = {'id': item['id'], 'type': item['type']}
                break
        if new_intf == None:
            logging.warning('Interface Object "{}" is not found in FMC.  Cannot add to destinationInterface.'.format(name))
        else:
            if new_intf.type == "InterfaceGroup" and len(new_intf.interfaces) > 1:
                logging.warning('Interface Object "{}" contains more than one physical interface.  Cannot add to destinationInterface.'.format(name))
            else:
                self.destinationInterface = new_intf
                logging.info('Interface Object "{}" added to NAT Policy.'.format(name))

    def identity_nat(self, name):
        logging.debug("In identity_nat() for AutoNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to this AutoNatRule.'.format(name))
        else:
            self.natType = "STATIC"
            self.originalNetwork = new_net
            self.translatedNetwork = new_net
            logging.info('Adding "{}" to AutoNatRule.'.format(name))

    def patPool(self, name, options={}):
        #Network Group Object permitted for patPool
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to patPool.'.format(name))
        else:
            self.natType = "DYNAMIC"
            self.patOptions = {"patPoolAddress": new_net}
            self.patOptions["interfacePat"] = options.interfacePat if "interfacePat" in options.keys() else False
            self.patOptions["includeReserve"] = options.includeReserve if "includeReserve" in options.keys() else False
            self.patOptions["roundRobin"] = options.roundRobin if "roundRobin" in options.keys() else True
            self.patOptions["extendedPat"] = options.extendedPat if "extendedPat" in options.keys() else False
            self.patOptions["flatPortRange"] = options.flatPortRange if "flatPortRange" in options.keys() else False
            logging.info('Adding "{}" to patPool for this AutoNatRule.'.format(name))

class ManualNatRules(APIClassTemplate):
    #Host,Network,NetworkGroup objects
    """
    The ManualNatRules Object in the FMC.
    """

    PREFIX_URL = '/policy/ftdnatpolicies'
    REQUIRED_FOR_POST = ["nat_id"]

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ManualNatRules class.")
        self.parse_kwargs(**kwargs)
        self.type = "FTDManualNatRule"

    def format_data(self):
        logging.debug("In format_data() for ManualNatRules class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'originalSource' in self.__dict__:
            json_data['originalSource'] = self.originalSource
        if 'originalDestination' in self.__dict__:
            json_data['originalDestination'] = self.originalDestination
        if 'translatedSource' in self.__dict__:
            json_data['translatedSource'] = self.translatedSource
        if 'translatedDestination' in self.__dict__:
            json_data['translatedDestination'] = self.translatedDestination
        if 'interfaceInTranslatedSource' in self.__dict__:
            json_data['interfaceInTranslatedSource'] = self.interfaceInTranslatedSource
        if 'interfaceInOriginalDestination' in self.__dict__:
            json_data['interfaceInOriginalDestination'] = self.interfaceInOriginalDestination
        if 'natType' in self.__dict__:
            json_data['natType'] = self.natType
        if 'interfaceIpv6' in self.__dict__:
            json_data['interfaceIpv6'] = self.interfaceIpv6
        if 'fallThrough' in self.__dict__:
            json_data['fallThrough'] = self.fallThrough
        if 'dns' in self.__dict__:
            json_data['dns'] = self.dns
        if 'routeLookup' in self.__dict__:
            json_data['routeLookup'] = self.routeLookup
        if 'noProxyArp' in self.__dict__:
            json_data['noProxyArp'] = self.noProxyArp
        if 'netToNet' in self.__dict__:
            json_data['netToNet'] = self.netToNet
        if 'sourceInterface' in self.__dict__:
            json_data['sourceInterface'] = self.sourceInterface
        if 'destinationInterface' in self.__dict__:
            json_data['destinationInterface'] = self.destinationInterface
        if 'originalSourcePort' in self.__dict__:
            json_data['originalSourcePort'] = self.originalSourcePort
        if 'translatedSourcePort' in self.__dict__:
            json_data['translatedSourcePort'] = self.translatedSourcePort
        if 'originalDestinationPort' in self.__dict__:
            json_data['originalDestinationPort'] = self.originalDestinationPort
        if 'translatedDestinationPort' in self.__dict__:
            json_data['translatedDestinationPort'] = self.translatedDestinationPort
        if 'patOptions' in self.__dict__:
            json_data['patOptions'] = self.patOptions
        if 'unidirectional' in self.__dict__:
            json_data['unidirectional'] = self.unidirectional
        if 'enabled' in self.__dict__:
            json_data['enabled'] = self.enabled
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ManualNatRules class.")
        if 'originalSource' in kwargs:
            self.originalSource = kwargs['originalSource']
        if 'originalDestination' in kwargs:
            self.originalDestination = kwargs['originalDestination']
        if 'translatedSource' in kwargs and 'interfaceInTranslatedSource' is True:
            logging.warning("Cannot have both a translatedSource and interfaceInTranslatedSource")
        elif 'translatedSource' in kwargs:
            self.translatedSource = kwargs['translatedSource']
        elif 'interfaceInTranslatedSource' in kwargs:
            self.interfaceInTranslatedSource = kwargs['interfaceInTranslatedSource']
        if 'translatedDestination' in kwargs:
            self.translatedDestination = kwargs['translatedDestination']
        if 'interfaceInOriginalDestination' in kwargs:
            self.interfaceInOriginalDestination = kwargs['interfaceInOriginalDestination']
        if 'natType' in kwargs:
            self.natType = kwargs['natType']
        if 'interfaceIpv6' in kwargs:
            self.interfaceIpv6 = kwargs['interfaceIpv6']
        if 'fallThrough' in kwargs:
            self.fallThrough = kwargs['fallThrough']
        if 'dns' in kwargs:
            self.dns = kwargs['dns']
        if 'routeLookup' in kwargs:
            self.routeLookup = kwargs['routeLookup']
        if 'noProxyArp' in kwargs:
            self.noProxyArp = kwargs['noProxyArp']
        if 'netToNet' in kwargs:
            self.netToNet = kwargs['netToNet']
        if 'sourceInterface' in kwargs:
            self.sourceInterface = kwargs['sourceInterface']
        if 'destinationInterface' in kwargs:
            self.destinationInterface = kwargs['destinationInterface']
        if 'originalSourcePort' in kwargs:
            self.originalSourcePort = kwargs['originalSourcePort']
        if 'translatedSourcePort' in kwargs:
            self.translatedSourcePort = kwargs['translatedSourcePort']
        if 'originalDestinationPort' in kwargs:
            self.originalDestinationPort = kwargs['originalDestinationPort']
        if 'translatedDestinationPort' in kwargs:
            self.translatedDestinationPort = kwargs['translatedDestinationPort']
        if 'patOptions' in kwargs:
            self.patOptions = kwargs['patOptions']
        if 'unidirectional' in kwargs:
            self.unidirectional = kwargs['unidirectional']
        if 'enabled' in kwargs:
            self.enabled = kwargs['enabled']

    def nat_policy(self,name):
        logging.debug("In nat_policy() for ManualNatRules class.")
        ftd_nat = FTDNatPolicy(fmc=self.fmc)
        ftd_nat.get(name=name)
        if 'id' in ftd_nat.__dict__:
            self.nat_id = ftd_nat.id
            self.URL = '{}{}/{}/manualnatrules'.format(self.fmc.configuration_url, self.PREFIX_URL, self.nat_id)
            self.nat_added_to_url = True
        else:
            logging.warning('FTD NAT Policy {} not found.  Cannot set up ManualNatRule for '
                            'NAT Policy.'.format(name))

    def original_source(self, name):
        logging.debug("In original_source() for ManualNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to original_source.'.format(name))
        else:
            self.originalSource = new_net
            logging.info('Adding "{}" to original_source for this ManualNatRule.'.format(name))

    def translated_source(self,name):
        logging.debug("In translated_source() for ManualNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to translated_source.'.format(name))
        else:
            self.translatedSource = new_net
            logging.info('Adding "{}" to translated_source for this ManualNatRule.'.format(name))

    def original_destination(self, name):
        logging.debug("In original_destination() for ManualNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to original_destination.'.format(name))
        else:
            self.originalDestination = new_net
            logging.info('Adding "{}" to original_destination for this ManualNatRule.'.format(name))

    def translated_destination(self,name):
        logging.debug("In translated_destination() for ManualNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to translated_destination.'.format(name))
        else:
            self.translatedDestination = new_net
            logging.info('Adding "{}" to translated_destination for this ManualNatRule.'.format(name))

    def original_source_port(self, name):
        logging.debug("In original_source_port() for ManualNatRules class.")
        ports_json = ProtocolPort(fmc=self.fmc).get()
        portgroup_json = PortObjectGroup(fmc=self.fmc).get()
        items = ports_json.get('items', []) + portgroup_json.get('items', [])
        new_port = None
        for item in items:
            if item['name'] == name:
                new_port = {'id': item['id'], 'type': item['type']}
                break
        if new_port is None:
            logging.warning('Port "{}" is not found in FMC.  Cannot add to original_source_port.'.format(name))
        else:
            self.originalSourcePort = new_port
            logging.info('Adding "{}" to original_source_port for this ManualNatRule.'.format(name))

    def translated_source_port(self, name):
        logging.debug("In translated_source_port() for ManualNatRules class.")
        ports_json = ProtocolPort(fmc=self.fmc).get()
        portgroup_json = PortObjectGroup(fmc=self.fmc).get()
        items = ports_json.get('items', []) + portgroup_json.get('items', [])
        new_port = None
        for item in items:
            if item['name'] == name:
                new_port = {'id': item['id'], 'type': item['type']}
                break
        if new_port is None:
            logging.warning('Port "{}" is not found in FMC.  Cannot add to translated_source_port.'.format(name))
        else:
            self.translatedSourcePort = new_port
            logging.info('Adding "{}" to translated_source_port for this ManualNatRule.'.format(name))

    def original_destination_port(self, name):
        logging.debug("In original_destination_port() for ManualNatRules class.")
        ports_json = ProtocolPort(fmc=self.fmc).get()
        portgroup_json = PortObjectGroup(fmc=self.fmc).get()
        items = ports_json.get('items', []) + portgroup_json.get('items', [])
        new_port = None
        for item in items:
            if item['name'] == name:
                new_port = {'id': item['id'], 'type': item['type']}
                break
        if new_port is None:
            logging.warning('Port "{}" is not found in FMC.  Cannot add to original_destination_port.'.format(name))
        else:
            self.originalDestinationPort = new_port
            logging.info('Adding "{}" to original_destination_port for this ManualNatRule.'.format(name))

    def translated_destination_port(self, name):
        logging.debug("In translated_destination_port() for ManualNatRules class.")
        ports_json = ProtocolPort(fmc=self.fmc).get()
        portgroup_json = PortObjectGroup(fmc=self.fmc).get()
        items = ports_json.get('items', []) + portgroup_json.get('items', [])
        new_port = None
        for item in items:
            if item['name'] == name:
                new_port = {'id': item['id'], 'type': item['type']}
                break
        if new_port is None:
            logging.warning('Port "{}" is not found in FMC.  Cannot add to translated_destination_port.'.format(name))
        else:
            self.translatedDestinationPort = new_port
            logging.info('Adding "{}" to translated_destination_port for this ManualNatRule.'.format(name))

    def source_intf(self,name):
        logging.debug("In source_intf() for ManualNatRules class.")
        intf_obj = InterfaceObject(fmc=self.fmc).get()
        items = intf_obj.get('items', [])
        new_intf = None
        for item in items:
            if item["name"] == name:
                new_intf = {'id': item['id'], 'type': item['type']}
                break
        if new_intf == None:
            logging.warning('Interface Object "{}" is not found in FMC.  Cannot add to sourceInterface.'.format(name))
        else:
            self.sourceInterface = new_intf
            logging.info('Interface Object "{}" added to NAT Policy.'.format(name))

    def destination_intf(self,name):
        logging.debug("In destination_intf() for ManualNatRules class.")
        intf_obj = InterfaceObject(fmc=self.fmc).get()
        items = intf_obj.get('items', [])
        new_intf = None
        for item in items:
            if item["name"] == name:
                new_intf = {'id': item['id'], 'type': item['type']}
                break
        if new_intf == None:
            logging.warning('Interface Object "{}" is not found in FMC.  Cannot add to destinationInterface.'.format(name))
        else:
            self.destinationInterface = new_intf
            logging.info('Interface Object "{}" added to NAT Policy.'.format(name))

    def identity_nat(self, name):
        logging.debug("In identity_nat() for ManualNatRules class.")
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to this ManualNatRules.'.format(name))
        else:
            self.natType = "STATIC"
            self.originalSource = new_net
            self.translatedSource = new_net
            logging.info('Adding "{}" to ManualNatRules.'.format(name))

    def patPool(self, name, options={}):
        ipaddresses_json = IPAddresses(fmc=self.fmc).get()
        networkgroup_json = NetworkGroup(fmc=self.fmc).get()
        items = ipaddresses_json.get('items', []) + networkgroup_json.get('items', [])
        new_net = None
        for item in items:
            if item['name'] == name:
                new_net = {'name': item['name'], 'id': item['id'], 'type': item['type']}
                break
        if new_net is None:
            logging.warning('Network "{}" is not found in FMC.  Cannot add to patPool.'.format(name))
        else:
            self.natType = "DYNAMIC"
            self.unidirectional = True
            self.patOptions = {"patPoolAddress": new_net}
            self.patOptions["interfacePat"] = options.interfacePat if "interfacePat" in options.keys() else False
            self.patOptions["includeReserve"] = options.includeReserve if "includeReserve" in options.keys() else False
            self.patOptions["roundRobin"] = options.roundRobin if "roundRobin" in options.keys() else True
            self.patOptions["extendedPat"] = options.extendedPat if "extendedPat" in options.keys() else False
            self.patOptions["flatPortRange"] = options.flatPortRange if "flatPortRange" in options.keys() else False
            logging.info('Adding "{}" to patPool for this AutoNatRule.'.format(name))

class NatRules(APIClassTemplate):
    """
    The NatRules Object in the FMC.
    """

    PREFIX_URL = '/policy/ftdnatpolicies'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for NatRules class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for NatRules class.")
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
        logging.debug("In parse_kwargs() for NatRules class.")

    def nat_policy(self,name):
        logging.debug("In nat_policy() for NatRules class.")
        ftd_nat = FTDNatPolicy(fmc=self.fmc)
        ftd_nat.get(name=name)
        if 'id' in ftd_nat.__dict__:
            self.nat_id = ftd_nat.id
            self.URL = '{}{}/{}/natrules'.format(self.fmc.configuration_url, self.PREFIX_URL, self.nat_id)
            self.nat_added_to_url = True
        else:
            logging.warning('FTD NAT Policy {} not found.  Cannot set up NatRules for '
                            'NAT Policy.'.format(name))

    def post(self):
        logging.info('POST method for API for NatRules not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for NatRules not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for NatRules not supported.')
        pass


class PolicyAssignments(APIClassTemplate):
    """
    The PolicyAssignments Object in the FMC.
    """
    REQUIRED_FOR_POST = ['targets','policy']
    REQUIRED_FOR_PUT = ['id','targets','policy']
    URL_SUFFIX = '/assignment/policyassignments'
    FILTER_BY_NAME = True

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for PolicyAssignments class.")
        self.parse_kwargs(**kwargs)
        self.type = "PolicyAssignment"

    def format_data(self):
        logging.debug("In format_data() for PolicyAssignments class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'targets' in self.__dict__:
            json_data['targets'] = self.targets
        if 'policy' in self.__dict__:
            json_data['policy'] = self.policy
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for PolicyAssignments class.")
        if 'targets' in kwargs:
            self.targets = kwargs['targets']
        if 'policy' in kwargs:
            self.policy = kwargs['policy']

    def ftd_natpolicy(self, name, devices):
        logging.debug("In ftd_natpolicy() for PolicyAssignments class.")
        targets = []
        pol1 = FTDNatPolicy(fmc=self.fmc)
        pol1.get(name=name)
        if 'id' in pol1.__dict__:
            self.policy = {"type":pol1.type, "name":pol1.name, "id":pol1.id}
        else:
            logging.warning('FTD NAT Policy {} not found.  Cannot set up'
                            'PolicyAssignment.'.format(name))
        for device in devices:
            if device["type"] == 'device':
                dev1 = Device(fmc=self.fmc)
                dev1.get(name=device["name"])
            elif device["type"] == 'deviceHAPair':
                dev1 = DeviceHAPairs(fmc=self.fmc)
                dev1.get(name=device["name"])
            if 'id' in dev1.__dict__:
                logging.info('Adding "{}" to targets for this FTDNat PolicyAssignment.'.format(dev1.name))
                targets.append({"type":dev1.type, "id":dev1.id, "name":dev1.name})
            else:
                logging.warning('Device/DeviceHA {} not found.  Cannot add to '
                                'PolicyAssignment.'.format(dev1.name))
        self.targets = targets

    def accesspolicy(self, name, devices):
        logging.debug("In accesspolicy() for PolicyAssignments class.")
        targets = []
        pol1 = AccessControlPolicy(fmc=self.fmc)
        pol1.get(name=name)
        if 'id' in pol1.__dict__:
            self.policy = {"type":pol1.type, "name":pol1.name, "id":pol1.id}
        else:
            logging.warning('Access Control Policy {} not found.  Cannot set up'
                            'PolicyAssignment.'.format(name))
        for device in devices:
            if device["type"] == 'device':
                dev1 = Device(fmc=self.fmc)
                dev1.get(name=device["name"])
            elif device["type"] == 'deviceHAPair':
                dev1 = DeviceHAPairs(fmc=self.fmc)
                dev1.get(name=device["name"])
            if 'id' in dev1.__dict__:
                logging.info('Adding "{}" to targets for this Access Control Policy PolicyAssignment.'.format(dev1.name))
                targets.append({"type":dev1.type, "id":dev1.id, "name":dev1.name})
            else:
                logging.warning('Device/DeviceHA {} not found.  Cannot add to '
                                'PolicyAssignment.'.format(dev1.name))
        self.targets = targets

    def delete(self):
        logging.info('DELETE method for API for PolicyAssignments not supported.')
        pass
