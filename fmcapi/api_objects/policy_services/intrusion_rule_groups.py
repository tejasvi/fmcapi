"""Not yet implemented. First seen in v7.0 release of FMC API"""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class IntrusionRuleGroups(APIClassTemplate):
    """The IntrusionRuleGroups Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "7.0"

    def delete(self):
        """DELETE method for API for IntrusionRuleGroups not supported."""
        logging.info("DELETE method for API for IntrusionRuleGroups not supported.")
        pass
