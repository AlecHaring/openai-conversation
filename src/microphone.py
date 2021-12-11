from google.cloud import speech

from microphone_stream import MicrophoneStream


class TranscribingMicrophone:
    LANGUAGE_CODE = "en-US"
    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms

    def __init__(self):
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.RATE,
            language_code=self.LANGUAGE_CODE,
            enable_automatic_punctuation=True,
        )
        self.streaming_config = speech.StreamingRecognitionConfig(
            config=self.config, interim_results=False
        )
        self.microphone_stream = MicrophoneStream(self.RATE, self.CHUNK)

    def __enter__(self):
        """
        Start the microphone stream and start listening for speech.
        """
        self.microphone_stream.__enter__()
        audio_generator = self.microphone_stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        self.responses = self.client.streaming_recognize(self.streaming_config, requests)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the microphone stream.
        """
        self.microphone_stream.__exit__(exc_type, exc_val, exc_tb)

    def listen_for_responses(self):
        """
        Loop through the responses and wait for Google to determine the user is done speaking.
        (this function blocks until the user is done speaking)
        :return: the final transcript of the user
        """
        for response in self.responses:
            if not response.results:
                continue
            result = response.results[0]
            if not result.alternatives:
                continue
            transcript = result.alternatives[0].transcript
            if result.is_final:
                # remove leading and trailing whitespace
                transcript = transcript.strip()
                return transcript
