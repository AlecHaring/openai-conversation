from microphone import TranscribingMicrophone
from open_ai_driver import OpenAIDriver
from text_to_speech import TextToSpeech


def main():
    controller = OpenAIDriver()
    tts_client = TextToSpeech()
    print("Listening...")
    while True:
        with TranscribingMicrophone() as mic:
            transcribed_text = mic.listen_for_responses()
        if transcribed_text.lower().startswith('reset'):
            controller.reset()
            print("Reset")
            continue
        ai_response = controller.respond(transcribed_text)
        tts_client.say(ai_response)


if __name__ == '__main__':
    main()
