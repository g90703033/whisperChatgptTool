import whisper
import gradio as gr
import time
from pyChatGPT import ChatGPT
import warnings

warnings.filterwarnings("ignore")

secret_session_token = ""

api = ChatGPT(secret_session_token)

response  = api.send_message("explain how to use chatgpt api")

print(response['message'])
