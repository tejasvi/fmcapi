"""Not yet implemented. First seen in v7.0 release of FMC API"""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Mappings(APIClassTemplate):
    """The Mappings Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "7.0"

    def get(self):
        """GET method for API for Mappings not supported."""
        logging.info("GET method for API for Mappings not supported.")
        pass

    def put(self):
        """PUT method for API for Mappings not supported."""
        logging.info("PUT method for API for Mappings not supported.")
        pass

    def delete(self):
        """DELETE method for API for Mappings not supported."""
        logging.info("DELETE method for API for Mappings not supported.")
        pass
