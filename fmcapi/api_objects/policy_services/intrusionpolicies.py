"""Intrusion Policies Classes."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class IntrusionPolicies(APIClassTemplate):
    """The IntrusionPolicies Object in the FMC."""

    VALID_JSON_DATA = ["id", "name", "type"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/policy/intrusionpolicies"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        """
        Initialize IntrusionPolicies object.

        :param fmc (object): FMC object
        :param **kwargs: Any other values passed during instantiation.
        :return: None
        """
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IntrusionPolicies class.")
        self.parse_kwargs(**kwargs)
