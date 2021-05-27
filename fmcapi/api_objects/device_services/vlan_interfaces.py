"""
Not yet implemented.
First seen in v6.5.0 release of FMC API.
Appears to only be valid for Firepower 1010 devices.
"""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class VlanInterfaces(APIClassTemplate):
    """The VlanInterfaces Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "6.5.0"
