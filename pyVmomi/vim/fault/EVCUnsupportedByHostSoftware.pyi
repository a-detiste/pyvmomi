# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import HostSystem

from pyVmomi.vim.fault import EVCConfigFault

class EVCUnsupportedByHostSoftware(EVCConfigFault):
   host: list[HostSystem] = []
   hostName: list[str] = []
