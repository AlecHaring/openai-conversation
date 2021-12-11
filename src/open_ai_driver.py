import openai


class OpenAIDriver:
    API_KEY = ""
    AI_SEQUENCE = "AI:"
    HUMAN_SEQUENCE = "Human:"

    def __init__(self):
        self.prompt = self.initial_prompt
        openai.api_key = self.API_KEY

    @property
    def initial_prompt(self) -> str:
        """
        The initial prompt to tell the AI the context of the conversation.
        """
        return "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n"

    @property
    def prompt_for_response(self) -> str:
        """
        Adds "AI:" at the end to make the AI respond to the human.
        """
        return self.prompt + self.AI_SEQUENCE

    def add_human_response(self, response: str) -> None:
        """
        Adds the human response to the conversation prompt.
        """
        print(f"{self.HUMAN_SEQUENCE} {response}")
        self.prompt += f"{self.HUMAN_SEQUENCE} {response}\n"

    def add_ai_response(self, response: str) -> None:
        """
        Adds the AI response to the conversation prompt.
        """
        print(f"{self.AI_SEQUENCE} {response}")
        self.prompt += f"{self.AI_SEQUENCE} {response}\n"

    def generate_ai_response(self) -> str:
        """
        Passes the conversation prompt to OpenAI and returns the response.
        """
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.prompt_for_response,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", self.HUMAN_SEQUENCE, self.AI_SEQUENCE]
        )
        response_text = response.choices[0].text
        # strip space from the beginning of the response
        response_text = response_text.lstrip()
        self.add_ai_response(response_text)
        return response_text

    def respond(self, response: str) -> str:
        """
        Add response and then generate the AI response
        """
        self.add_human_response(response)
        return self.generate_ai_response()

    def reset(self) -> None:
        """
        Reset the conversation back to the beginning.
        """
        self.prompt = self.initial_prompt



