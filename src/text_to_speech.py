from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play
import io


class TextToSpeech:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code='en-US',
            name="en-US-Wavenet-J"
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

    def generate_mp3(self, text: str) -> bytes:
        """
        Converts text to speech and returns the mp3 data
        """
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        return response.audio_content

    def say(self, text: str) -> None:
        """
        Converts text to speech and plays it using pydub
        """
        mp3_data = self.generate_mp3(text)
        play(AudioSegment.from_file(io.BytesIO(mp3_data), format="mp3"))
