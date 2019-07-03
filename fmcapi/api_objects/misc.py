"""
This module contains the "miscellaneous" class objects that represent the various objects in the FMC.
"""

from .api_template import *
from .helper_functions import *
from .api_template import *
from .devices import *
from .misc import *
from .objects import *
from .policy import *


class TaskStatuses(APIClassTemplate):
    """
    The Task Status Object in the FMC.
    """

    URL_SUFFIX = '/job/taskstatuses'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for TaskStatuses class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for TaskStatuses class.")
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
        logging.debug("In parse_kwargs() for TaskStatuses class.")

    def post(self):
        logging.info('POST method for API for TaskStatuses not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for TaskStatuses not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for TaskStatuses not supported.')
        pass


class UpgradePackage(APIClassTemplate):
    """
    The UpgradePackage Object in the FMC.
    """

    URL_SUFFIX = '/updates/upgradepackages'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for UpgradePackage class.")
        self.type = 'UpgradePackage'
        self.URL = '{}{}'.format(self.fmc.platform_url, self.URL_SUFFIX)
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for UpgradePackage class.")
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
        logging.debug("In parse_kwargs() for UpgradePackage class.")

    def post(self):
        logging.info('POST method for API for UpgradePackage not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for UpgradePackage not supported.')
        pass


class ApplicableDevices(APIClassTemplate):
    """
    The ApplicableDevices Object in the FMC.
    """

    URL_SUFFIX = '/updates/upgradepackages'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicableDevices class.")
        self.type = 'UpgradePackage'
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ApplicableDevices class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'upgadePackage' in self.__dict__:
            json_data['upgadePackage'] = self.upgadePackage
        if 'model' in self.__dict__:
            json_data['model'] = self.model
        if 'modelId' in self.__dict__:
            json_data['modelId'] = self.modelId
        if 'modelNumber' in self.__dict__:
            json_data['modelNumber'] = self.modelNumber
        if 'modelType' in self.__dict__:
            json_data['modelType'] = self.modelType
        if 'healthStatus' in self.__dict__:
            json_data['healthStatus'] = self.healthStatus
        if 'sw_version' in self.__dict__:
            json_data['sw_version'] = self.sw_version
        if 'isPartofContainer' in self.__dict__:
            json_data['isPartofContainer'] = self.isPartofContainer
        if 'containerType' in self.__dict__:
            json_data['containerType'] = self.containerType
        if 'healthPolicy' in self.__dict__:
            json_data['healthPolicy'] = self.healthPolicy
        if 'accessPolicy' in self.__dict__:
            json_data['accessPolicy'] = self.accessPolicy
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicableDevices class.")

    def upgrade_package(self, package_name):
        logging.debug("In upgrade_package() for ApplicableDevices class.")
        package1 = UpgradePackage(fmc=self.fmc)
        package1.get(name=package_name)
        if 'id' in package1.__dict__:
            self.package_id = package1.id
            self.URL = '{}{}/{}/applicabledevices'.format(self.fmc.platform_url, self.URL_SUFFIX, self.package_id)
            self.package_added_to_url = True
        else:
            logging.warning('UpgradePackage {} not found.  Cannot get list of '
                            'ApplicableDevices.'.format(package_name))

    def post(self):
        logging.info('POST method for API for ApplicableDevices not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicableDevices not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicableDevices not supported.')
        pass


class Upgrades(APIClassTemplate):
    """
    The Upgrades Object in the FMC.
    """

    URL_SUFFIX = '/updates/upgrades'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Upgrades class.")
        self.type = 'Upgrade'
        self.URL = '{}{}'.format(self.fmc.platform_url, self.URL_SUFFIX)
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for Upgrades class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'upgradePackage' in self.__dict__:
            json_data['upgradePackage'] = self.upgradePackage
        if 'targets' in self.__dict__:
            json_data['targets'] = self.targets
        if 'pushUpgradeFileOnly' in self.__dict__:
            json_data['pushUpgradeFileOnly'] = self.pushUpgradeFileOnly
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for Upgrades class.")
        if 'upgradePackage' in kwargs:
            self.upgradePackage = kwargs['upgradePackage']
        if 'targets' in kwargs:
            self.targets = kwargs['targets']
        if 'pushUpgradeFileOnly' in kwargs:
            self.pushUpgradeFileOnly = kwargs['pushUpgradeFileOnly']

    def upgrade_package(self, package_name):
        logging.debug("In upgrade_package() for Upgrades class.")
        package1 = UpgradePackage(fmc=self.fmc)
        package1.get(name=package_name)
        if 'id' in package1.__dict__:
            self.upgradePackage = {"id":package1.id, "type":package1.type}
        else:
            logging.warning('UpgradePackage {} not found.  Cannot add package to '
                            'Upgrades.'.format(package_name))

    def devices(self, devices):
        logging.debug("In devices() for Upgrades class.")
        for device in devices:
            device1 = Device(fmc=self.fmc)
            device1.get(name=device)
            if 'id' in device1.__dict__ and 'targets' in self.__dict__:
                self.targets.append({"id":device1.id, "type":device1.type, "name":device1.name})
            elif 'id' in device1.__dict__:
                self.targets = [{"id":device1.id, "type":device1.type, "name":device1.name}]
            else:
                logging.warning('Device {} not found.  Cannot prepare devices for '
                                'Upgrades.'.format(device))

    def get(self):
        logging.info('GET method for API for Upgrades not supported.')
        pass

    def post(self, **kwargs):
        # returns a task status object
        logging.debug("In post() for Upgrades class.")
        self.fmc.autodeploy = False
        return super().post(**kwargs)

    def put(self):
        logging.info('PUT method for API for Upgrades not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for Upgrades not supported.')
        pass
