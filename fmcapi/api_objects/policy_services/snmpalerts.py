"""Not yet implemented."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class SNMPAlerts(APIClassTemplate):
    """The SNMPAlerts Object in the FMC."""

    def post(self):
        """POST method for API for SNMPAlerts not supported."""
        logging.info("POST method for API for SNMPAlerts not supported.")
        pass

    def put(self):
        """PUT method for API for SNMPAlerts not supported."""
        logging.info("PUT method for API for SNMPAlerts not supported.")
        pass

    def delete(self):
        """DELETE method for API for SNMPAlerts not supported."""
        logging.info("DELETE method for API for SNMPAlerts not supported.")
        pass
