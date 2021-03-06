# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: starship/voicebot/proto/voicebot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from starship.voicebot.proto import speech_pb2 as starship_dot_voicebot_dot_proto_dot_speech__pb2
from starship.voicebot.proto import tts_pb2 as starship_dot_voicebot_dot_proto_dot_tts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='starship/voicebot/proto/voicebot.proto',
  package='skelterlabs.aiq.voicebot.v1alpha1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&starship/voicebot/proto/voicebot.proto\x12!skelterlabs.aiq.voicebot.v1alpha1\x1a$starship/voicebot/proto/speech.proto\x1a!starship/voicebot/proto/tts.proto\"\xc3\x03\n\x14StreamingTalkRequest\x12j\n\x15streaming_talk_config\x18\x01 \x01(\x0b\x32K.skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig\x12\x15\n\raudio_content\x18\x02 \x01(\x0c\x1a\xa7\x02\n\x13StreamingTalkConfig\x12\x63\n\x1cstreaming_recognition_config\x18\x01 \x01(\x0b\x32=.skelterlabs.aiq.voicebot.v1alpha1.StreamingRecognitionConfig\x12\x62\n\x18synthesize_speech_config\x18\x02 \x01(\x0b\x32@.skelterlabs.aiq.voicebot.v1alpha1.SynthesizeSpeechRequestConfig\x12\x0f\n\x07talk_id\x18\x03 \x01(\t\x12\x12\n\nsession_id\x18\x05 \x01(\t\x12\"\n\x1astarting_user_context_json\x18\x04 \x01(\t\"\x8d\x03\n\x15StreamingTalkResponse\x12r\n$streaming_synthesize_speech_response\x18\x01 \x01(\x0b\x32\x44.skelterlabs.aiq.voicebot.v1alpha1.StreamingSynthesizeSpeechResponse\x12V\n\ntalk_event\x18\x02 \x01(\x0e\x32\x42.skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.TalkEvent\x12\x10\n\x08user_say\x18\x03 \x01(\t\x12\x14\n\x0c\x61gent_answer\x18\x04 \x01(\t\x12\x12\n\nsession_id\x18\x05 \x01(\t\"l\n\tTalkEvent\x12\x0b\n\x07NOTHING\x10\x00\x12\r\n\tLISTENING\x10\x01\x12\x16\n\x12PROCESSING_STARTED\x10\x02\x12\x14\n\x10SPEAKING_STARTED\x10\x03\x12\x15\n\x11SPEAKING_FINISHED\x10\x04\x32\x95\x01\n\x08Voicebot\x12\x88\x01\n\rStreamingTalk\x12\x37.skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest\x1a\x38.skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[starship_dot_voicebot_dot_proto_dot_speech__pb2.DESCRIPTOR,starship_dot_voicebot_dot_proto_dot_tts__pb2.DESCRIPTOR,])



_STREAMINGTALKRESPONSE_TALKEVENT = _descriptor.EnumDescriptor(
  name='TalkEvent',
  full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.TalkEvent',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTHING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LISTENING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING_STARTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPEAKING_STARTED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPEAKING_FINISHED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=894,
  serialized_end=1002,
)
_sym_db.RegisterEnumDescriptor(_STREAMINGTALKRESPONSE_TALKEVENT)


_STREAMINGTALKREQUEST_STREAMINGTALKCONFIG = _descriptor.Descriptor(
  name='StreamingTalkConfig',
  full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='streaming_recognition_config', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig.streaming_recognition_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='synthesize_speech_config', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig.synthesize_speech_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='talk_id', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig.talk_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig.session_id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_user_context_json', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig.starting_user_context_json', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=307,
  serialized_end=602,
)

_STREAMINGTALKREQUEST = _descriptor.Descriptor(
  name='StreamingTalkRequest',
  full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='streaming_talk_config', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.streaming_talk_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.audio_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STREAMINGTALKREQUEST_STREAMINGTALKCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=602,
)


_STREAMINGTALKRESPONSE = _descriptor.Descriptor(
  name='StreamingTalkResponse',
  full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='streaming_synthesize_speech_response', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.streaming_synthesize_speech_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='talk_event', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.talk_event', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_say', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.user_say', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_answer', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.agent_answer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse.session_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STREAMINGTALKRESPONSE_TALKEVENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=1002,
)

_STREAMINGTALKREQUEST_STREAMINGTALKCONFIG.fields_by_name['streaming_recognition_config'].message_type = starship_dot_voicebot_dot_proto_dot_speech__pb2._STREAMINGRECOGNITIONCONFIG
_STREAMINGTALKREQUEST_STREAMINGTALKCONFIG.fields_by_name['synthesize_speech_config'].message_type = starship_dot_voicebot_dot_proto_dot_tts__pb2._SYNTHESIZESPEECHREQUESTCONFIG
_STREAMINGTALKREQUEST_STREAMINGTALKCONFIG.containing_type = _STREAMINGTALKREQUEST
_STREAMINGTALKREQUEST.fields_by_name['streaming_talk_config'].message_type = _STREAMINGTALKREQUEST_STREAMINGTALKCONFIG
_STREAMINGTALKRESPONSE.fields_by_name['streaming_synthesize_speech_response'].message_type = starship_dot_voicebot_dot_proto_dot_tts__pb2._STREAMINGSYNTHESIZESPEECHRESPONSE
_STREAMINGTALKRESPONSE.fields_by_name['talk_event'].enum_type = _STREAMINGTALKRESPONSE_TALKEVENT
_STREAMINGTALKRESPONSE_TALKEVENT.containing_type = _STREAMINGTALKRESPONSE
DESCRIPTOR.message_types_by_name['StreamingTalkRequest'] = _STREAMINGTALKREQUEST
DESCRIPTOR.message_types_by_name['StreamingTalkResponse'] = _STREAMINGTALKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamingTalkRequest = _reflection.GeneratedProtocolMessageType('StreamingTalkRequest', (_message.Message,), {

  'StreamingTalkConfig' : _reflection.GeneratedProtocolMessageType('StreamingTalkConfig', (_message.Message,), {
    'DESCRIPTOR' : _STREAMINGTALKREQUEST_STREAMINGTALKCONFIG,
    '__module__' : 'starship.voicebot.proto.voicebot_pb2'
    # @@protoc_insertion_point(class_scope:skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest.StreamingTalkConfig)
    })
  ,
  'DESCRIPTOR' : _STREAMINGTALKREQUEST,
  '__module__' : 'starship.voicebot.proto.voicebot_pb2'
  # @@protoc_insertion_point(class_scope:skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkRequest)
  })
_sym_db.RegisterMessage(StreamingTalkRequest)
_sym_db.RegisterMessage(StreamingTalkRequest.StreamingTalkConfig)

StreamingTalkResponse = _reflection.GeneratedProtocolMessageType('StreamingTalkResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGTALKRESPONSE,
  '__module__' : 'starship.voicebot.proto.voicebot_pb2'
  # @@protoc_insertion_point(class_scope:skelterlabs.aiq.voicebot.v1alpha1.StreamingTalkResponse)
  })
_sym_db.RegisterMessage(StreamingTalkResponse)



_VOICEBOT = _descriptor.ServiceDescriptor(
  name='Voicebot',
  full_name='skelterlabs.aiq.voicebot.v1alpha1.Voicebot',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1005,
  serialized_end=1154,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamingTalk',
    full_name='skelterlabs.aiq.voicebot.v1alpha1.Voicebot.StreamingTalk',
    index=0,
    containing_service=None,
    input_type=_STREAMINGTALKREQUEST,
    output_type=_STREAMINGTALKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VOICEBOT)

DESCRIPTOR.services_by_name['Voicebot'] = _VOICEBOT

# @@protoc_insertion_point(module_scope)
