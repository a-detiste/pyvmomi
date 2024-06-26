# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.host import DnsConfig
from pyVmomi.vim.host import IpRouteConfig
from pyVmomi.vim.host import IpRouteTableConfig
from pyVmomi.vim.host import NetCapabilities
from pyVmomi.vim.host import NetOffloadCapabilities
from pyVmomi.vim.host import NetworkConfig
from pyVmomi.vim.host import NetworkInfo
from pyVmomi.vim.host import PhysicalNic
from pyVmomi.vim.host import PortGroup
from pyVmomi.vim.host import VirtualNic
from pyVmomi.vim.host import VirtualSwitch

class NetworkSystem(ExtensibleManagedObject):
   @property
   def capabilities(self) -> Optional[NetCapabilities]: ...
   @property
   def networkInfo(self) -> Optional[NetworkInfo]: ...
   @property
   def offloadCapabilities(self) -> Optional[NetOffloadCapabilities]: ...
   @property
   def networkConfig(self) -> Optional[NetworkConfig]: ...
   @property
   def dnsConfig(self) -> Optional[DnsConfig]: ...
   @property
   def ipRouteConfig(self) -> Optional[IpRouteConfig]: ...
   @property
   def consoleIpRouteConfig(self) -> Optional[IpRouteConfig]: ...

   def UpdateNetworkConfig(self, config: NetworkConfig, changeMode: str) -> NetworkConfig.Result: ...
   def UpdateDnsConfig(self, config: DnsConfig) -> NoReturn: ...
   def UpdateIpRouteConfig(self, config: IpRouteConfig) -> NoReturn: ...
   def UpdateConsoleIpRouteConfig(self, config: IpRouteConfig) -> NoReturn: ...
   def UpdateIpRouteTableConfig(self, config: IpRouteTableConfig) -> NoReturn: ...
   def AddVirtualSwitch(self, vswitchName: str, spec: Optional[VirtualSwitch.Specification]) -> NoReturn: ...
   def RemoveVirtualSwitch(self, vswitchName: str) -> NoReturn: ...
   def UpdateVirtualSwitch(self, vswitchName: str, spec: VirtualSwitch.Specification) -> NoReturn: ...
   def AddPortGroup(self, portgrp: PortGroup.Specification) -> NoReturn: ...
   def RemovePortGroup(self, pgName: str) -> NoReturn: ...
   def UpdatePortGroup(self, pgName: str, portgrp: PortGroup.Specification) -> NoReturn: ...
   def UpdatePhysicalNicLinkSpeed(self, device: str, linkSpeed: Optional[PhysicalNic.LinkSpeedDuplex]) -> NoReturn: ...
   def QueryNetworkHint(self, device: list[str]) -> list[PhysicalNic.NetworkHint]: ...
   def AddVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveVirtualNic(self, device: str) -> NoReturn: ...
   def UpdateVirtualNic(self, device: str, nic: VirtualNic.Specification) -> NoReturn: ...
   def AddServiceConsoleVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveServiceConsoleVirtualNic(self, device: str) -> NoReturn: ...
   def UpdateServiceConsoleVirtualNic(self, device: str, nic: VirtualNic.Specification) -> NoReturn: ...
   def RestartServiceConsoleVirtualNic(self, device: str) -> NoReturn: ...
   def Refresh(self) -> NoReturn: ...
   def StartDpuFailover(self, dvsName: str, targetDpuAlias: Optional[str]) -> NoReturn: ...
