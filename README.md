# OpenAI Conversation
A wrapper around OpenAI's `davinci` GPT-3 model that allows you to talk to it. Using Google Cloud's
[Speech-to-Text](https://cloud.google.com/speech-to-text/) and [Text-to-Speech](https://cloud.google.com/text-to-speech/)
APIs, it transcribes speech to text, passes the text to GPT-3, and then speaks the response back to you.

## 🚀 Get Started
### 1. Clone repo and install requirements
#### Mac
```shell
# Clone the repository:
git clone https://github.com/AlecHaring/openai-conversation
# Open the project's directory:
cd openai-conversation
# Create new virtual environment:
python3 -m venv ./venv
# Activate the virtual environment:
source ./venv/bin/activate
# Install required packages:
pip3 install -r requirements
```

#### Windows
```shell
# Clone the repository:
git clone https://github.com/AlecHaring/openai-conversation
# Open the project's directory:
cd openai-conversation
# Create new virtual environment:
python -m venv .\venv
# Activate the virtual environment:
.\venv\Scripts\activate
# Install required packages:
pip3 install -r requirements
```

### 3. Set up Google Cloud Info
#### Google Cloud Platform
- Follow the instructions [here](https://cloud.google.com/speech-to-text/docs/before-you-begin) to set up Speech-to-Text.
- Follow the instructions [here](https://cloud.google.com/text-to-speech/docs/before-you-begin) to set up Text-to-Speech.

### 4. Get OpenAI API Key
- Go to [OpenAI's website](https://beta.openai.com/signup/) and sign up for an account.
- Go to [API keys page](https://beta.openai.com/account/api-keys) and copy the secret key.
  - Set the `API_KEY` variable in the `OpenAIDriver` class in `src/open_ai_driver.py`

### 3. 🔌 Run!
```shell
python3 src/main.py
```