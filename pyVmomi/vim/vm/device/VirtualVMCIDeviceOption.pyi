# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualVMCIDeviceOption(VirtualDeviceOption):
   class FilterSpecOption(DynamicData):
      action: ChoiceOption
      protocol: ChoiceOption
      direction: ChoiceOption
      lowerDstPortBoundary: LongOption
      upperDstPortBoundary: LongOption

   allowUnrestrictedCommunication: BoolOption
   filterSpecOption: Optional[FilterSpecOption] = None
   filterSupported: Optional[BoolOption] = None
