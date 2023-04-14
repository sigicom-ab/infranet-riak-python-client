# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_ts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import riak.pb.riak_pb2 as riak__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rriak_ts.proto\x1a\nriak.proto\"[\n\nTsQueryReq\x12\x1f\n\x05query\x18\x01 \x01(\x0b\x32\x10.TsInterpolation\x12\x15\n\x06stream\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rcover_context\x18\x03 \x01(\x0c\"^\n\x0bTsQueryResp\x12%\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x02 \x03(\x0b\x32\x06.TsRow\x12\x12\n\x04\x64one\x18\x03 \x01(\x08:\x04true\"@\n\x08TsGetReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x14\n\x03key\x18\x02 \x03(\x0b\x32\x07.TsCell\x12\x0f\n\x07timeout\x18\x03 \x01(\r\"H\n\tTsGetResp\x12%\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x02 \x03(\x0b\x32\x06.TsRow\"V\n\x08TsPutReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12%\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x03 \x03(\x0b\x32\x06.TsRow\"\x0b\n\tTsPutResp\"P\n\x08TsDelReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x14\n\x03key\x18\x02 \x03(\x0b\x32\x07.TsCell\x12\x0e\n\x06vclock\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\r\"\x0b\n\tTsDelResp\"A\n\x0fTsInterpolation\x12\x0c\n\x04\x62\x61se\x18\x01 \x02(\x0c\x12 \n\x0einterpolations\x18\x02 \x03(\x0b\x32\x08.RpbPair\"@\n\x13TsColumnDescription\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x1b\n\x04type\x18\x02 \x02(\x0e\x32\r.TsColumnType\"\x1f\n\x05TsRow\x12\x16\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x07.TsCell\"{\n\x06TsCell\x12\x15\n\rvarchar_value\x18\x01 \x01(\x0c\x12\x14\n\x0csint64_value\x18\x02 \x01(\x12\x12\x17\n\x0ftimestamp_value\x18\x03 \x01(\x12\x12\x15\n\rboolean_value\x18\x04 \x01(\x08\x12\x14\n\x0c\x64ouble_value\x18\x05 \x01(\x01\"/\n\rTsListKeysReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x0f\n\x07timeout\x18\x02 \x01(\r\"4\n\x0eTsListKeysResp\x12\x14\n\x04keys\x18\x01 \x03(\x0b\x32\x06.TsRow\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"q\n\rTsCoverageReq\x12\x1f\n\x05query\x18\x01 \x01(\x0b\x32\x10.TsInterpolation\x12\r\n\x05table\x18\x02 \x02(\x0c\x12\x15\n\rreplace_cover\x18\x03 \x01(\x0c\x12\x19\n\x11unavailable_cover\x18\x04 \x03(\x0c\"3\n\x0eTsCoverageResp\x12!\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x10.TsCoverageEntry\"[\n\x0fTsCoverageEntry\x12\n\n\x02ip\x18\x01 \x02(\x0c\x12\x0c\n\x04port\x18\x02 \x02(\r\x12\x15\n\rcover_context\x18\x03 \x02(\x0c\x12\x17\n\x05range\x18\x04 \x01(\x0b\x32\x08.TsRange\"\x93\x01\n\x07TsRange\x12\x12\n\nfield_name\x18\x01 \x02(\x0c\x12\x13\n\x0blower_bound\x18\x02 \x02(\x12\x12\x1d\n\x15lower_bound_inclusive\x18\x03 \x02(\x08\x12\x13\n\x0bupper_bound\x18\x04 \x02(\x12\x12\x1d\n\x15upper_bound_inclusive\x18\x05 \x02(\x08\x12\x0c\n\x04\x64\x65sc\x18\x06 \x02(\x0c*Y\n\x0cTsColumnType\x12\x0b\n\x07VARCHAR\x10\x00\x12\n\n\x06SINT64\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\r\n\tTIMESTAMP\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\x12\x08\n\x04\x42LOB\x10\x05\x42#\n\x17\x63om.basho.riak.protobufB\x08RiakTsPB')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'riak_ts_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.basho.riak.protobufB\010RiakTsPB'
  _globals['_TSCOLUMNTYPE']._serialized_start=1359
  _globals['_TSCOLUMNTYPE']._serialized_end=1448
  _globals['_TSQUERYREQ']._serialized_start=29
  _globals['_TSQUERYREQ']._serialized_end=120
  _globals['_TSQUERYRESP']._serialized_start=122
  _globals['_TSQUERYRESP']._serialized_end=216
  _globals['_TSGETREQ']._serialized_start=218
  _globals['_TSGETREQ']._serialized_end=282
  _globals['_TSGETRESP']._serialized_start=284
  _globals['_TSGETRESP']._serialized_end=356
  _globals['_TSPUTREQ']._serialized_start=358
  _globals['_TSPUTREQ']._serialized_end=444
  _globals['_TSPUTRESP']._serialized_start=446
  _globals['_TSPUTRESP']._serialized_end=457
  _globals['_TSDELREQ']._serialized_start=459
  _globals['_TSDELREQ']._serialized_end=539
  _globals['_TSDELRESP']._serialized_start=541
  _globals['_TSDELRESP']._serialized_end=552
  _globals['_TSINTERPOLATION']._serialized_start=554
  _globals['_TSINTERPOLATION']._serialized_end=619
  _globals['_TSCOLUMNDESCRIPTION']._serialized_start=621
  _globals['_TSCOLUMNDESCRIPTION']._serialized_end=685
  _globals['_TSROW']._serialized_start=687
  _globals['_TSROW']._serialized_end=718
  _globals['_TSCELL']._serialized_start=720
  _globals['_TSCELL']._serialized_end=843
  _globals['_TSLISTKEYSREQ']._serialized_start=845
  _globals['_TSLISTKEYSREQ']._serialized_end=892
  _globals['_TSLISTKEYSRESP']._serialized_start=894
  _globals['_TSLISTKEYSRESP']._serialized_end=946
  _globals['_TSCOVERAGEREQ']._serialized_start=948
  _globals['_TSCOVERAGEREQ']._serialized_end=1061
  _globals['_TSCOVERAGERESP']._serialized_start=1063
  _globals['_TSCOVERAGERESP']._serialized_end=1114
  _globals['_TSCOVERAGEENTRY']._serialized_start=1116
  _globals['_TSCOVERAGEENTRY']._serialized_end=1207
  _globals['_TSRANGE']._serialized_start=1210
  _globals['_TSRANGE']._serialized_end=1357
# @@protoc_insertion_point(module_scope)
