# AIQ.TALK Voicebot Python Example

This repository contains simple example CLI programs that recognizes
stream audio from microphone, handle those streams by using Voicebot
streaming api.

## Before you begin

Our examples are based on python 3.7 runtime.

Before running the examples, make sure you've followed the steps.

```shell
$ pip install -U -r ./requirements.txt
```

[SoX](http://sox.sourceforge.net/) must be installed and available in 
your $PATH and microphone must be working.

- OSX: brew install sox
- Linux: apt-get install sox

Get your AIQ API key from the
[AIQ Console](https://aiq.skelterlabs.com/console), configure
the Voicebot with your desired target Chatbot.

NOTE. We temporarily offer management API before support GUI console
for Voicebot.

```shell
curl --location --request PUT \
	'https://aiq.skelterlabs.com/voicebot-setting/v1/projects/<AIQ project id>/project-setting' \
	--header 'Content-Type: application/json' \
	--header 'x-api-key: <AIQ project api key>' \
	--data-raw '{
			"chatbotSetting": {
					"apiKey": "<Chatbot api key>",
					"endpoint": "<Chatbot endpoint URL>"
			},
			"projectId": "<AIQ project id>",
			"sttSetting": {
					"model": "default"
			},
			"wordSubstitutionPairs": []
	}'

```

## Samples

```shell
$ ./grpc_mic.py --api-key=<your API key>
```
