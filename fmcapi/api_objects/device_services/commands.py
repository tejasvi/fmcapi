"""Not yet implemented. First seen in v7.0 release of FMC API"""

from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class Commands(APIClassTemplate):
    """The Commands Object in the FMC."""

    FIRST_SUPPORTED_FMC_VERSION = "7.0"
    Note_from_docs = """
    The below table lists the commands which can be used with the commands service. Some commands are only allowed with certain parameters, or specific parameters may not be allowed, as specificed in the Blocked column.

    Command	:: Blocked
    show version	
    show failover	
    show dhcpd :: show dhcpd binding, show dhcpd statistics
    show ip	
    show aaa-server	
    show logging :: show logging asdm, show logging queue
    show snmp-server	
    show running-config {any} :: show running-config {no parameters}
    show ssl	
    show firewall	
    show logging	
    show network	
    show ntp	
    show banner	
    """

    def post(self):
        """POST method for API for Commands not supported."""
        logging.info("POST method for API for Commands not supported.")
        pass

    def put(self):
        """PUT method for API for Commands not supported."""
        logging.info("PUT method for API for Commands not supported.")
        pass

    def delete(self):
        """DELETE method for API for Commands not supported."""
        logging.info("DELETE method for API for Commands not supported.")
        pass
