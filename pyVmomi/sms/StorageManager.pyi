# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.sms import FaultDomainFilter
from pyVmomi.sms import ReplicationGroupFilter
from pyVmomi.sms import Task

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem

from pyVmomi.sms.provider import Provider
from pyVmomi.sms.provider import ProviderSpec

from pyVmomi.sms.storage import BackingStoragePool
from pyVmomi.sms.storage import DatastoreBackingPoolMapping
from pyVmomi.sms.storage import DrsMigrationCapabilityResult
from pyVmomi.sms.storage import StorageArray
from pyVmomi.sms.storage import StorageCapability
from pyVmomi.sms.storage import StorageContainerResult
from pyVmomi.sms.storage import StorageContainerSpec
from pyVmomi.sms.storage import StorageFileSystem
from pyVmomi.sms.storage import StorageLun
from pyVmomi.sms.storage import StoragePort
from pyVmomi.sms.storage import StorageProcessor

from pyVmomi.sms.storage.replication import GroupOperationResult

from pyVmomi.vim.vm.replication import FaultDomainId

class StorageManager(ManagedObject):
   def RegisterProvider(self, providerSpec: ProviderSpec) -> Task: ...
   def UnregisterProvider(self, providerId: str) -> Task: ...
   def QueryProvider(self) -> list[Provider]: ...
   def QueryArray(self, providerId: list[str]) -> list[StorageArray]: ...
   def QueryProcessorAssociatedWithArray(self, arrayId: str) -> list[StorageProcessor]: ...
   def QueryPortAssociatedWithArray(self, arrayId: str) -> list[StoragePort]: ...
   def QueryPortAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> Optional[StoragePort]: ...
   def QueryLunAssociatedWithPort(self, portId: str, arrayId: str) -> list[StorageLun]: ...
   def QueryArrayAssociatedWithLun(self, canonicalName: str) -> Optional[StorageArray]: ...
   def QueryPortAssociatedWithProcessor(self, processorId: str, arrayId: str) -> list[StoragePort]: ...
   def QueryLunAssociatedWithArray(self, arrayId: str) -> list[StorageLun]: ...
   def QueryFileSystemAssociatedWithArray(self, arrayId: str) -> list[StorageFileSystem]: ...
   def QueryDatastoreCapability(self, datastore: Datastore) -> Optional[StorageCapability]: ...
   def QueryHostAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> list[HostSystem]: ...
   def QueryVmfsDatastoreAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> Optional[Datastore]: ...
   def QueryNfsDatastoreAssociatedWithFileSystem(self, fileSystemId: str, arrayId: str) -> Optional[Datastore]: ...
   def QueryDrsMigrationCapabilityForPerformance(self, srcDatastore: Datastore, dstDatastore: Datastore) -> bool: ...
   def QueryDrsMigrationCapabilityForPerformanceEx(self, datastore: list[Datastore]) -> DrsMigrationCapabilityResult: ...
   def QueryStorageContainer(self, containerSpec: Optional[StorageContainerSpec]) -> Optional[StorageContainerResult]: ...
   def QueryAssociatedBackingStoragePool(self, entityId: Optional[str], entityType: Optional[str]) -> list[BackingStoragePool]: ...
   def QueryDatastoreBackingPoolMapping(self, datastore: list[Datastore]) -> list[DatastoreBackingPoolMapping]: ...
   def RefreshCACertificatesAndCRLs(self, providerId: list[str]) -> Task: ...
   def QueryFaultDomain(self, filter: Optional[FaultDomainFilter]) -> list[FaultDomainId]: ...
   def QueryReplicationGroupInfo(self, rgFilter: ReplicationGroupFilter) -> list[GroupOperationResult]: ...
