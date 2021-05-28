"""Not yet implemented. First seen in v7.0 release of FMC API"""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class DynamicObjectMappings(APIClassTemplate):
    """The DynamicObjectMappings Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "7.0"

    def get(self):
        """GET method for API for DynamicObjectMappings not supported."""
        logging.info("GET method for API for DynamicObjectMappings not supported.")
        pass

    def put(self):
        """PUT method for API for DynamicObjectMappings not supported."""
        logging.info("PUT method for API for DynamicObjectMappings not supported.")
        pass
