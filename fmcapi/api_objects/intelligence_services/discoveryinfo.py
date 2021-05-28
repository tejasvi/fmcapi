"""Not yet implemented."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class DiscoveryInfo(APIClassTemplate):
    """The DiscoveryInfo Object in the FMC."""

    def get(self):
        """GET method for API for DiscoveryInfo not supported."""
        logging.info("GET method for API for DiscoveryInfo not supported.")
        pass

    def put(self):
        """PUT method for API for DiscoveryInfo not supported."""
        logging.info("PUT method for API for DiscoveryInfo not supported.")
        pass

    def delete(self):
        """DELETE method for API for DiscoveryInfo not supported."""
        logging.info("DELETE method for API for DiscoveryInfo not supported.")
        pass
