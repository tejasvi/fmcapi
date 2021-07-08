"""Advanced Settings Class."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
from .ftds2svpns import FTDS2SVPNs
import logging


class AdvancedSettings(APIClassTemplate):
    """The AdvancedSettings Object in the FMC."""

    VALID_JSON_DATA = [
        "id",
        "name",
        "type",
        "advancedIkeSetting",
        "advancedTunnelSetting",
        "advancedIpsecSetting",
        "version",
    ]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    FIRST_SUPPORTED_FMC_VERSION = "6.3"
    PREFIX_URL = "/policy/ftds2svpns"
    REQUIRED_FOR_POST = ["vpn_id"]

    def __init__(self, fmc, **kwargs):
        """
        Initialize AdvancedSettings object.

        :param fmc: (object) FMC object
        :param **kwargs: Set initial variables during instantiation of AdvancedSettings object.
        :return: None
        """
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for AdvancedSettings class.")
        self.parse_kwargs(**kwargs)
        self.type = "AdvancedSettings"

    def vpn_policy(self, pol_name=None, vpn_id=None):
        """
        Associate a Policy with this VPN.

        :param pol_name: (str) Name of policy.
        :param vpn_id: (str) VPN topology ID. (default is None)
        :return: None
        """
        logging.debug("In vpn_policy() for AdvancedSettings class.")
        if vpn_id is None:
            if pol_name is not None:
                ftd_s2s = FTDS2SVPNs(fmc=self.fmc)
                ftd_s2s.get(name=pol_name)
                if "id" in ftd_s2s.__dict__:
                    vpn_id = ftd_s2s.id

        if vpn_id is not None:
            self.vpn_id = vpn_id
            self.URL = f"{self.fmc.configuration_url}{self.PREFIX_URL}/{self.vpn_id}/advancedsettings"
            self.vpn_added_to_url = True
        else:
            logging.warning(
                f'FTD S2S VPN Policy "{pol_name}" not found.  Cannot set up AdvancedSettings for FTDS2SVPNs Policy.'
            )
