# Copyright 2010-present Basho Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from six import *
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_yokozuna.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='riak_yokozuna.proto',
  package='',
  serialized_pb=b'\n\x13riak_yokozuna.proto\"?\n\x10RpbYokozunaIndex\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x0e\n\x06schema\x18\x02 \x01(\x0c\x12\r\n\x05n_val\x18\x03 \x01(\r\"&\n\x16RpbYokozunaIndexGetReq\x12\x0c\n\x04name\x18\x01 \x01(\x0c\";\n\x17RpbYokozunaIndexGetResp\x12 \n\x05index\x18\x01 \x03(\x0b\x32\x11.RpbYokozunaIndex\"K\n\x16RpbYokozunaIndexPutReq\x12 \n\x05index\x18\x01 \x02(\x0b\x32\x11.RpbYokozunaIndex\x12\x0f\n\x07timeout\x18\x02 \x01(\r\")\n\x19RpbYokozunaIndexDeleteReq\x12\x0c\n\x04name\x18\x01 \x02(\x0c\"2\n\x11RpbYokozunaSchema\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"=\n\x17RpbYokozunaSchemaPutReq\x12\"\n\x06schema\x18\x01 \x02(\x0b\x32\x12.RpbYokozunaSchema\"\'\n\x17RpbYokozunaSchemaGetReq\x12\x0c\n\x04name\x18\x01 \x02(\x0c\">\n\x18RpbYokozunaSchemaGetResp\x12\"\n\x06schema\x18\x01 \x02(\x0b\x32\x12.RpbYokozunaSchemaB)\n\x17\x63om.basho.riak.protobufB\x0eRiakYokozunaPB')




_RPBYOKOZUNAINDEX = _descriptor.Descriptor(
  name='RpbYokozunaIndex',
  full_name='RpbYokozunaIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndex.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaIndex.schema', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_val', full_name='RpbYokozunaIndex.n_val', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=86,
)


_RPBYOKOZUNAINDEXGETREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexGetReq',
  full_name='RpbYokozunaIndexGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndexGetReq.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=88,
  serialized_end=126,
)


_RPBYOKOZUNAINDEXGETRESP = _descriptor.Descriptor(
  name='RpbYokozunaIndexGetResp',
  full_name='RpbYokozunaIndexGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='RpbYokozunaIndexGetResp.index', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=128,
  serialized_end=187,
)


_RPBYOKOZUNAINDEXPUTREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexPutReq',
  full_name='RpbYokozunaIndexPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='RpbYokozunaIndexPutReq.index', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='RpbYokozunaIndexPutReq.timeout', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=189,
  serialized_end=264,
)


_RPBYOKOZUNAINDEXDELETEREQ = _descriptor.Descriptor(
  name='RpbYokozunaIndexDeleteReq',
  full_name='RpbYokozunaIndexDeleteReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaIndexDeleteReq.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=266,
  serialized_end=307,
)


_RPBYOKOZUNASCHEMA = _descriptor.Descriptor(
  name='RpbYokozunaSchema',
  full_name='RpbYokozunaSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaSchema.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='RpbYokozunaSchema.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=309,
  serialized_end=359,
)


_RPBYOKOZUNASCHEMAPUTREQ = _descriptor.Descriptor(
  name='RpbYokozunaSchemaPutReq',
  full_name='RpbYokozunaSchemaPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaSchemaPutReq.schema', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=361,
  serialized_end=422,
)


_RPBYOKOZUNASCHEMAGETREQ = _descriptor.Descriptor(
  name='RpbYokozunaSchemaGetReq',
  full_name='RpbYokozunaSchemaGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbYokozunaSchemaGetReq.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=424,
  serialized_end=463,
)


_RPBYOKOZUNASCHEMAGETRESP = _descriptor.Descriptor(
  name='RpbYokozunaSchemaGetResp',
  full_name='RpbYokozunaSchemaGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='RpbYokozunaSchemaGetResp.schema', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=465,
  serialized_end=527,
)

_RPBYOKOZUNAINDEXGETRESP.fields_by_name['index'].message_type = _RPBYOKOZUNAINDEX
_RPBYOKOZUNAINDEXPUTREQ.fields_by_name['index'].message_type = _RPBYOKOZUNAINDEX
_RPBYOKOZUNASCHEMAPUTREQ.fields_by_name['schema'].message_type = _RPBYOKOZUNASCHEMA
_RPBYOKOZUNASCHEMAGETRESP.fields_by_name['schema'].message_type = _RPBYOKOZUNASCHEMA
DESCRIPTOR.message_types_by_name['RpbYokozunaIndex'] = _RPBYOKOZUNAINDEX
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexGetReq'] = _RPBYOKOZUNAINDEXGETREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexGetResp'] = _RPBYOKOZUNAINDEXGETRESP
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexPutReq'] = _RPBYOKOZUNAINDEXPUTREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaIndexDeleteReq'] = _RPBYOKOZUNAINDEXDELETEREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchema'] = _RPBYOKOZUNASCHEMA
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaPutReq'] = _RPBYOKOZUNASCHEMAPUTREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaGetReq'] = _RPBYOKOZUNASCHEMAGETREQ
DESCRIPTOR.message_types_by_name['RpbYokozunaSchemaGetResp'] = _RPBYOKOZUNASCHEMAGETRESP

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaIndex(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNAINDEX

  # @@protoc_insertion_point(class_scope:RpbYokozunaIndex)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaIndexGetReq(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNAINDEXGETREQ

  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexGetReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaIndexGetResp(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNAINDEXGETRESP

  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexGetResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaIndexPutReq(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNAINDEXPUTREQ

  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexPutReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaIndexDeleteReq(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNAINDEXDELETEREQ

  # @@protoc_insertion_point(class_scope:RpbYokozunaIndexDeleteReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaSchema(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNASCHEMA

  # @@protoc_insertion_point(class_scope:RpbYokozunaSchema)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaSchemaPutReq(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNASCHEMAPUTREQ

  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaPutReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaSchemaGetReq(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNASCHEMAGETREQ

  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaGetReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class RpbYokozunaSchemaGetResp(_message.Message):
  DESCRIPTOR = _RPBYOKOZUNASCHEMAGETRESP

  # @@protoc_insertion_point(class_scope:RpbYokozunaSchemaGetResp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\027com.basho.riak.protobufB\016RiakYokozunaPB')
# @@protoc_insertion_point(module_scope)
