# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from starship.voicebot.proto import voicebot_pb2 as starship_dot_voicebot_dot_proto_dot_voicebot__pb2


class VoicebotStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamingTalk = channel.stream_stream(
                '/skelterlabs.aiq.voicebot.v1alpha1.Voicebot/StreamingTalk',
                request_serializer=starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkRequest.SerializeToString,
                response_deserializer=starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkResponse.FromString,
                )


class VoicebotServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamingTalk(self, request_iterator, context):
        """streaming_talk_config of StreamingTalkRequest should be set on first
        request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoicebotServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamingTalk': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingTalk,
                    request_deserializer=starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkRequest.FromString,
                    response_serializer=starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'skelterlabs.aiq.voicebot.v1alpha1.Voicebot', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Voicebot(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamingTalk(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/skelterlabs.aiq.voicebot.v1alpha1.Voicebot/StreamingTalk',
            starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkRequest.SerializeToString,
            starship_dot_voicebot_dot_proto_dot_voicebot__pb2.StreamingTalkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)