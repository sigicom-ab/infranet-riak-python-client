# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nriak.proto\"/\n\x0cRpbErrorResp\x12\x0e\n\x06\x65rrmsg\x18\x01 \x02(\x0c\x12\x0f\n\x07\x65rrcode\x18\x02 \x02(\r\"<\n\x14RpbGetServerInfoResp\x12\x0c\n\x04node\x18\x01 \x01(\x0c\x12\x16\n\x0eserver_version\x18\x02 \x01(\x0c\"%\n\x07RpbPair\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"/\n\x0fRpbGetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\x0c\"2\n\x10RpbGetBucketResp\x12\x1e\n\x05props\x18\x01 \x02(\x0b\x32\x0f.RpbBucketProps\"O\n\x0fRpbSetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x1e\n\x05props\x18\x02 \x02(\x0b\x32\x0f.RpbBucketProps\x12\x0c\n\x04type\x18\x03 \x01(\x0c\"1\n\x11RpbResetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\x0c\"#\n\x13RpbGetBucketTypeReq\x12\x0c\n\x04type\x18\x01 \x02(\x0c\"C\n\x13RpbSetBucketTypeReq\x12\x0c\n\x04type\x18\x01 \x02(\x0c\x12\x1e\n\x05props\x18\x02 \x02(\x0b\x32\x0f.RpbBucketProps\"-\n\tRpbModFun\x12\x0e\n\x06module\x18\x01 \x02(\x0c\x12\x10\n\x08\x66unction\x18\x02 \x02(\x0c\"9\n\rRpbCommitHook\x12\x1a\n\x06modfun\x18\x01 \x01(\x0b\x32\n.RpbModFun\x12\x0c\n\x04name\x18\x02 \x01(\x0c\"\xc7\x05\n\x0eRpbBucketProps\x12\r\n\x05n_val\x18\x01 \x01(\r\x12\x12\n\nallow_mult\x18\x02 \x01(\x08\x12\x17\n\x0flast_write_wins\x18\x03 \x01(\x08\x12!\n\tprecommit\x18\x04 \x03(\x0b\x32\x0e.RpbCommitHook\x12\x1c\n\rhas_precommit\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\"\n\npostcommit\x18\x06 \x03(\x0b\x32\x0e.RpbCommitHook\x12\x1d\n\x0ehas_postcommit\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x0c\x63hash_keyfun\x18\x08 \x01(\x0b\x32\n.RpbModFun\x12\x1b\n\x07linkfun\x18\t \x01(\x0b\x32\n.RpbModFun\x12\x12\n\nold_vclock\x18\n \x01(\r\x12\x14\n\x0cyoung_vclock\x18\x0b \x01(\r\x12\x12\n\nbig_vclock\x18\x0c \x01(\r\x12\x14\n\x0csmall_vclock\x18\r \x01(\r\x12\n\n\x02pr\x18\x0e \x01(\r\x12\t\n\x01r\x18\x0f \x01(\r\x12\t\n\x01w\x18\x10 \x01(\r\x12\n\n\x02pw\x18\x11 \x01(\r\x12\n\n\x02\x64w\x18\x12 \x01(\r\x12\n\n\x02rw\x18\x13 \x01(\r\x12\x14\n\x0c\x62\x61sic_quorum\x18\x14 \x01(\x08\x12\x13\n\x0bnotfound_ok\x18\x15 \x01(\x08\x12\x0f\n\x07\x62\x61\x63kend\x18\x16 \x01(\x0c\x12\x0e\n\x06search\x18\x17 \x01(\x08\x12)\n\x04repl\x18\x18 \x01(\x0e\x32\x1b.RpbBucketProps.RpbReplMode\x12\x14\n\x0csearch_index\x18\x19 \x01(\x0c\x12\x10\n\x08\x64\x61tatype\x18\x1a \x01(\x0c\x12\x12\n\nconsistent\x18\x1b \x01(\x08\x12\x12\n\nwrite_once\x18\x1c \x01(\x08\x12\x15\n\rhll_precision\x18\x1d \x01(\r\">\n\x0bRpbReplMode\x12\t\n\x05\x46\x41LSE\x10\x00\x12\x0c\n\x08REALTIME\x10\x01\x12\x0c\n\x08\x46ULLSYNC\x10\x02\x12\x08\n\x04TRUE\x10\x03\",\n\nRpbAuthReq\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x10\n\x08password\x18\x02 \x02(\x0c\x42!\n\x17\x63om.basho.riak.protobufB\x06RiakPB')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'riak.pb.riak_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.basho.riak.protobufB\006RiakPB'
  _globals['_RPBERRORRESP']._serialized_start=14
  _globals['_RPBERRORRESP']._serialized_end=61
  _globals['_RPBGETSERVERINFORESP']._serialized_start=63
  _globals['_RPBGETSERVERINFORESP']._serialized_end=123
  _globals['_RPBPAIR']._serialized_start=125
  _globals['_RPBPAIR']._serialized_end=162
  _globals['_RPBGETBUCKETREQ']._serialized_start=164
  _globals['_RPBGETBUCKETREQ']._serialized_end=211
  _globals['_RPBGETBUCKETRESP']._serialized_start=213
  _globals['_RPBGETBUCKETRESP']._serialized_end=263
  _globals['_RPBSETBUCKETREQ']._serialized_start=265
  _globals['_RPBSETBUCKETREQ']._serialized_end=344
  _globals['_RPBRESETBUCKETREQ']._serialized_start=346
  _globals['_RPBRESETBUCKETREQ']._serialized_end=395
  _globals['_RPBGETBUCKETTYPEREQ']._serialized_start=397
  _globals['_RPBGETBUCKETTYPEREQ']._serialized_end=432
  _globals['_RPBSETBUCKETTYPEREQ']._serialized_start=434
  _globals['_RPBSETBUCKETTYPEREQ']._serialized_end=501
  _globals['_RPBMODFUN']._serialized_start=503
  _globals['_RPBMODFUN']._serialized_end=548
  _globals['_RPBCOMMITHOOK']._serialized_start=550
  _globals['_RPBCOMMITHOOK']._serialized_end=607
  _globals['_RPBBUCKETPROPS']._serialized_start=610
  _globals['_RPBBUCKETPROPS']._serialized_end=1321
  _globals['_RPBBUCKETPROPS_RPBREPLMODE']._serialized_start=1259
  _globals['_RPBBUCKETPROPS_RPBREPLMODE']._serialized_end=1321
  _globals['_RPBAUTHREQ']._serialized_start=1323
  _globals['_RPBAUTHREQ']._serialized_end=1367
# @@protoc_insertion_point(module_scope)
