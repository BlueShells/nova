# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.objects import base
from nova.objects import fields


# TODO(berrange): Remove NovaObjectDictCompat
@base.NovaObjectRegistry.register
class HVSpec(base.NovaObject,
             base.NovaObjectDictCompat):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'arch': fields.ArchitectureField(),
        'hv_type': fields.HVTypeField(),
        'vm_mode': fields.VMModeField(),
        }

    # NOTE(pmurray): for backward compatibility, the supported instance
    # data is stored in the database as a list.
    @classmethod
    def from_list(cls, data):
        return cls(arch=data[0],
                   hv_type=data[1],
                   vm_mode=data[2])

    def to_list(self):
        return [self.arch, self.hv_type, self.vm_mode]
