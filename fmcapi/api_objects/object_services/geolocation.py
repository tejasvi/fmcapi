"""Geolocation Class."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Geolocation(APIClassTemplate):
    """The Geolocation Object in the FMC."""

    VALID_JSON_DATA = [
        "id",
        "name",
        "type",
        "continentId",
        "continents",
        "countries",
        "continentUUID",
    ]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/object/geolocations"

    def __init__(self, fmc, **kwargs):
        """
        Initialize Geolocation object.

        :param fmc: (object) FMC object
        :param kwargs: Any other values passed during instantiation.
        :return: None
        """
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Geolocation class.")
        self.parse_kwargs(**kwargs)
