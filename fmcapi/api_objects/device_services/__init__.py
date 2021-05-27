"""Device Services Classes."""

import logging
from .copyconfigrequests import CopyConfigRequests
from .fpphysicalinterfaces import FPPhysicalInterfaces
from .fplogicalinterfaces import FPLogicalInterfaces
from .inlinesets import InlineSets
from .commands import Commands
from .metrics import Metrics
from .virtual_routers import VirtualRouters
from .virtual_bgp import VirtualBGP
from .virtual_static_routes import VirtualStaticRoutes
from .virtual_ospfv2_routes import VirtualOSPFv2Routes
from .virtual_ospf_interface import VirtualOSPFInterface
from .ospfv3_interfaces import OSPFv3Interfaces
from .ospf_interface import OSPFInterface
from .ospfv2_routes import OSPFv2Routes
from .ospfv3_routes import OSPFv3Routes
from .virtual_switches import VirtualSwitches
from .virtual_tunnel_interfaces import VirtualTunnelInterfaces
from .bridgegroupinterfaces import BridgeGroupInterfaces
from .devicerecords import DeviceRecords
from .etherchannelinterfaces import EtherchannelInterfaces
from .ipv4staticroutes import IPv4StaticRoutes
from .ipv6staticroutes import IPv6StaticRoutes
from .physicalinterfaces import PhysicalInterfaces
from .redundantinterfaces import RedundantInterfaces
from .staticroutes import StaticRoutes
from .subinterfaces import SubInterfaces
from .vlan_interfaces import VlanInterfaces
from .bgp_routing import BGPRouting
from .bgp_general_settings import BGPGeneralSettings
from .fpinterfacestatistics import FPInterfaceStatistics
from .interfaceevents import InterfaceEvents

logging.debug("In the device_services __init__.py file.")

__all__ = [
    "CopyConfigRequests",
    "FPPhysicalInterfaces",
    "FPLogicalInterfaces",
    "InlineSets",
    "Commands",
    "Metrics",
    "VirtualRouters",
    "VirtualStaticRoutes",
    "VirtualOSPFInterface",
    "VirtualOSPFv2Routes",
    "OSPFInterface",
    "OSPFv2Routes",
    "OSPFv3Routes",
    "OSPFv3Interfaces",
    "VirtualBGP",
    "DeviceRecords",
    "StaticRoutes",
    "IPv4StaticRoutes",
    "IPv6StaticRoutes",
    "PhysicalInterfaces",
    "BridgeGroupInterfaces",
    "RedundantInterfaces",
    "EtherchannelInterfaces",
    "SubInterfaces",
    "VirtualTunnelInterfaces",
    "VlanInterfaces",
    "BGPRouting",
    "BGPGeneralSettings",
    "FPInterfaceStatistics",
    "InterfaceEvents",
]
