# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_tag_color.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokemon_tag_color.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/enums/pokemon_tag_color.proto\x12\x10pogoprotos.enums*\x95\x02\n\x0fPokemonTagColor\x12\x1b\n\x17POKEMON_TAG_COLOR_UNSET\x10\x00\x12\x1a\n\x16POKEMON_TAG_COLOR_BLUE\x10\x01\x12\x1b\n\x17POKEMON_TAG_COLOR_GREEN\x10\x02\x12\x1c\n\x18POKEMON_TAG_COLOR_PURPLE\x10\x03\x12\x1c\n\x18POKEMON_TAG_COLOR_YELLOW\x10\x04\x12\x19\n\x15POKEMON_TAG_COLOR_RED\x10\x05\x12\x1c\n\x18POKEMON_TAG_COLOR_ORANGE\x10\x06\x12\x1a\n\x16POKEMON_TAG_COLOR_GREY\x10\x07\x12\x1b\n\x17POKEMON_TAG_COLOR_BLACK\x10\x08\x62\x06proto3')
)

_POKEMONTAGCOLOR = _descriptor.EnumDescriptor(
  name='PokemonTagColor',
  full_name='pogoprotos.enums.PokemonTagColor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_BLUE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_GREEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_PURPLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_YELLOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_RED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_ORANGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_GREY', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_TAG_COLOR_BLACK', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=63,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_POKEMONTAGCOLOR)

PokemonTagColor = enum_type_wrapper.EnumTypeWrapper(_POKEMONTAGCOLOR)
POKEMON_TAG_COLOR_UNSET = 0
POKEMON_TAG_COLOR_BLUE = 1
POKEMON_TAG_COLOR_GREEN = 2
POKEMON_TAG_COLOR_PURPLE = 3
POKEMON_TAG_COLOR_YELLOW = 4
POKEMON_TAG_COLOR_RED = 5
POKEMON_TAG_COLOR_ORANGE = 6
POKEMON_TAG_COLOR_GREY = 7
POKEMON_TAG_COLOR_BLACK = 8


DESCRIPTOR.enum_types_by_name['PokemonTagColor'] = _POKEMONTAGCOLOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
