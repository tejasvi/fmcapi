"""Not yet implemented."""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class CloudRegions(APIClassTemplate):
    """The CloudRegions Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "6.5.0"

    def post(self):
        """POST method for API for CloudRegions not supported."""
        logging.info("POST method for API for CloudRegions not supported.")
        pass

    def delete(self):
        """DELETE method for API for CloudRegions not supported."""
        logging.info("DELETE method for API for CloudRegions not supported.")
        pass
