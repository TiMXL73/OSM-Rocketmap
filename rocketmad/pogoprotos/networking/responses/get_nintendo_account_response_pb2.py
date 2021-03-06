# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_nintendo_account_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_nintendo_account_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpogoprotos/networking/responses/get_nintendo_account_response.proto\x12\x1fpogoprotos.networking.responses\"\xe1\x02\n\x1aGetNintendoAccountResponse\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.responses.GetNintendoAccountResponse.Status\x12\x13\n\x0blinked_naid\x18\x02 \x01(\t\x12!\n\x19pokemon_home_trainer_name\x18\x03 \x01(\t\x12\x12\n\nsupport_id\x18\x04 \x01(\t\"\xa2\x01\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_PLAYER_LEVEL_TOO_LOW\x10\x02\x12!\n\x1d\x45RROR_PLAYER_NOT_USING_PH_APP\x10\x03\x12\x17\n\x13\x45RROR_PHAPI_UNKNOWN\x10\x04\x12\"\n\x1e\x45RROR_RELOGIN_TO_PH_APP_NEEDED\x10\x05\x62\x06proto3')
)



_GETNINTENDOACCOUNTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetNintendoAccountResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_LEVEL_TOO_LOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_USING_PH_APP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PHAPI_UNKNOWN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RELOGIN_TO_PH_APP_NEEDED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=296,
  serialized_end=458,
)
_sym_db.RegisterEnumDescriptor(_GETNINTENDOACCOUNTRESPONSE_STATUS)


_GETNINTENDOACCOUNTRESPONSE = _descriptor.Descriptor(
  name='GetNintendoAccountResponse',
  full_name='pogoprotos.networking.responses.GetNintendoAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetNintendoAccountResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linked_naid', full_name='pogoprotos.networking.responses.GetNintendoAccountResponse.linked_naid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_home_trainer_name', full_name='pogoprotos.networking.responses.GetNintendoAccountResponse.pokemon_home_trainer_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='support_id', full_name='pogoprotos.networking.responses.GetNintendoAccountResponse.support_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETNINTENDOACCOUNTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=458,
)

_GETNINTENDOACCOUNTRESPONSE.fields_by_name['status'].enum_type = _GETNINTENDOACCOUNTRESPONSE_STATUS
_GETNINTENDOACCOUNTRESPONSE_STATUS.containing_type = _GETNINTENDOACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['GetNintendoAccountResponse'] = _GETNINTENDOACCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNintendoAccountResponse = _reflection.GeneratedProtocolMessageType('GetNintendoAccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNINTENDOACCOUNTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_nintendo_account_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetNintendoAccountResponse)
  ))
_sym_db.RegisterMessage(GetNintendoAccountResponse)


# @@protoc_insertion_point(module_scope)
