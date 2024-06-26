# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import Datastore

from pyVmomi.vim.fault import VirtualHardwareCompatibilityIssue

class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
   datastore: Datastore
   memorySizeMB: int
   maxMemorySizeMB: int
