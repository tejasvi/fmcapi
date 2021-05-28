"""Realms Class."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Realms(APIClassTemplate):
    """The Realms Object in the FMC."""

    VALID_JSON_DATA = ["id", "name", "type"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/object/realms"

    def __init__(self, fmc, **kwargs):
        """
        Initialize Realms object.

        :param fmc: (object) FMC object
        :param kwargs: Any other values passed during instantiation.
        :return: None
        """
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Realms class.")
        self.parse_kwargs(**kwargs)
