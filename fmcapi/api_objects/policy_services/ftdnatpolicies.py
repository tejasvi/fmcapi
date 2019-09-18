from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging
import warnings


class FTDNatPolicies(APIClassTemplate):
    """
    The FTDNatPolicies Object in the FMC.
    """

    url_suffix = '/policy/ftdnatpolicies'
    valid_characters_for_name = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for FTDNatPolicies class.")
        self.parse_kwargs(**kwargs)
        self.type = "FTDNatPolicy"

    def format_data(self):
        logging.debug("In format_data() for FTDNatPolicies class.")
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
        logging.debug("In parse_kwargs() for FTDNatPolicies class.")


class FTDNatPolicy(FTDNatPolicies):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: FTDNatPolicy() should be called via FTDNatPolicies().")
        super().__init__(fmc, **kwargs)
