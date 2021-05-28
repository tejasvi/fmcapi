"""Not yet implemented."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Settings(APIClassTemplate):
    """The Settings Object in the FMC."""

    def post(self):
        """POST method for API for Settings not supported."""
        logging.info("POST method for API for Settings not supported.")
        pass

    def delete(self):
        """DELETE method for API for Settings not supported."""
        logging.info("DELETE method for API for Settings not supported.")
        pass
