#!/usr/bin/env python3
"""
Dependencies:
    SoX - Sound eXchange 14.4.2
    python 3.7

Usage:
    $ ./grpc_mic.py --api_key <AIQ api_key>
"""
import subprocess
import time

from absl import app
from absl import flags
import grpc

import grpc_utils
# NOTE: It will be replaced to Skelter Lab's pip package.
from starship.voicebot.proto import speech_pb2
from starship.voicebot.proto import voicebot_pb2
from starship.voicebot.proto import voicebot_pb2_grpc

flags.DEFINE_string('api_url', 'aiq.skelterlabs.com:443', 'AIQ portal address.')
flags.DEFINE_string('api_key', None, 'AIQ project api key.')
flags.DEFINE_boolean('insecure', None,
                     'Use plaintext and insecure connection.')
flags.DEFINE_string('talk_id', 'test', 'ID to distinguish user.')
flags.DEFINE_string('user_context', None,
                    'Additional user context to initialize')
FLAGS = flags.FLAGS


def _make_talk_config(talk_id, user_context_json):
    """Make StreamingTalkConfig."""
    recognition_config = speech_pb2.RecognitionConfig(
        encoding='LINEAR16',
        sample_rate_hertz=16000,
    )
    return voicebot_pb2.StreamingTalkRequest.StreamingTalkConfig(
        streaming_recognition_config=speech_pb2.StreamingRecognitionConfig(
            config=recognition_config),
        talk_id=talk_id,
        starting_user_context_json=user_context_json,
    )


def _init_mic_in():
    command = ' '.join([
        'sox',
        '--default-device',
        '-t',
        'wav',
        '-r',
        '16000',
        '-b',
        '16',
        '-c',
        '1',
        '-q',
        '-',
    ])
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)


def _init_audio_out():
    command = ' '.join([
        'play',
        '-t',
        'raw',
        '-r',
        '16000',
        '-b',
        '16',
        '-e',
        'signed-integer',
        '-c',
        '1',
        '-q',
        '-',
    ])
    return subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)


def main(args):
    del args  # Unused

    channel = grpc_utils.create_channel(
        FLAGS.api_url, api_key=FLAGS.api_key, insecure=FLAGS.insecure)
    stub = voicebot_pb2_grpc.VoicebotStub(channel)

    mic_in = _init_mic_in()
    state = voicebot_pb2.StreamingTalkResponse.LISTENING

    def _generate_requests(chunk_size=16000):
        talk_config = _make_talk_config(FLAGS.talk_id, FLAGS.user_context)
        yield voicebot_pb2.StreamingTalkRequest(
            streaming_talk_config=talk_config)

        while True:
            audio_content = mic_in.stdout.read(chunk_size)
            if not audio_content:
                try:
                    mic_in.wait(0.05)
                    return
                except subprocess.TimeoutExpired:
                    continue
            if state == voicebot_pb2.StreamingTalkResponse.LISTENING:
                yield voicebot_pb2.StreamingTalkRequest(
                    audio_content=audio_content)

    audio_out = _init_audio_out()
    responses = stub.StreamingTalk(_generate_requests())
    start_time = time.time()
    for i, response in enumerate(responses):
        audio_content = (
            response.streaming_synthesize_speech_response.audio_content)
        if audio_content:
            audio_out.stdin.write(audio_content)

        if (response.talk_event ==
                voicebot_pb2.StreamingTalkResponse.PROCESSING_STARTED):
            end_time = time.time()
            print(f'message: {i}'
                  f'  event: {response.talk_event}'
                  f'  user say: {response.user_say}'
                  f'  elapsed time: {end_time - start_time:0.2f}s')
            start_time = end_time
        elif (response.talk_event ==
              voicebot_pb2.StreamingTalkResponse.SPEAKING_STARTED):
            end_time = time.time()
            print(f'message: {i}'
                  f'  event: {response.talk_event}'
                  f'  user say: {response.user_say}'
                  f'  chatbot answer: {response.agent_answer}'
                  f'  elapsed time: {end_time - start_time:0.2f}s')
            state = response.talk_event
        elif (response.talk_event ==
              voicebot_pb2.StreamingTalkResponse.SPEAKING_FINISHED):
            audio_out.stdin.close()
            audio_out.wait()
            audio_out = _init_audio_out()
            time.sleep(0.5)
            print('LISTENING...')
            state = voicebot_pb2.StreamingTalkResponse.LISTENING
            start_time = time.time()


if __name__ == '__main__':
    app.run(main)
