from microphone import TranscribingMicrophone
from open_ai_driver import OpenAIDriver
from text_to_speech import TextToSpeech


def main():
    controller = OpenAIDriver()
    tts_client = TextToSpeech()
    print("Listening...")
    while True:
        with TranscribingMicrophone() as mic:
            transcribed_text = mic.listen_for_responses()  # blocking until transcription is done
        if transcribed_text.lower().startswith('reset'):
            # Start the conversation over by saying "Reset"
            controller.reset()
            print("Conversation reset")
            continue
        ai_response = controller.respond(transcribed_text)  # passes the user's message to the AI
        tts_client.say(ai_response)  # speaks the response from the AI


if __name__ == '__main__':
    main()
