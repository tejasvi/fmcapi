"""Not yet implemented."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Domain(APIClassTemplate):
    """The Domain Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "6.5.0"

    def post(self):
        """POST method for API for Domain not supported."""
        logging.info("POST method for API for Domain not supported.")
        pass

    def put(self):
        """PUT method for API for Domain not supported."""
        logging.info("PUT method for API for Domain not supported.")
        pass

    def delete(self):
        """DELETE method for API for Domain not supported."""
        logging.info("DELETE method for API for Domain not supported.")
        pass
