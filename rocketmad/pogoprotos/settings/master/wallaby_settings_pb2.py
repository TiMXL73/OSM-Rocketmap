# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/wallaby_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/wallaby_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/settings/master/wallaby_settings.proto\x12\x1apogoprotos.settings.master\"O\n\x0fWallabySettings\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x19\n\x11\x61\x63tivity_length_s\x18\x02 \x01(\x02\x12\x11\n\ttest_mask\x18\x03 \x01(\rb\x06proto3')
)




_WALLABYSETTINGS = _descriptor.Descriptor(
  name='WallabySettings',
  full_name='pogoprotos.settings.master.WallabySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='pogoprotos.settings.master.WallabySettings.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_length_s', full_name='pogoprotos.settings.master.WallabySettings.activity_length_s', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_mask', full_name='pogoprotos.settings.master.WallabySettings.test_mask', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['WallabySettings'] = _WALLABYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WallabySettings = _reflection.GeneratedProtocolMessageType('WallabySettings', (_message.Message,), dict(
  DESCRIPTOR = _WALLABYSETTINGS,
  __module__ = 'pogoprotos.settings.master.wallaby_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.WallabySettings)
  ))
_sym_db.RegisterMessage(WallabySettings)


# @@protoc_insertion_point(module_scope)
