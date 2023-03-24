import whisper
import openai
import gradio as gr
import time
from pyChatGPT import ChatGPT
import warnings

warnings.filterwarnings("ignore")

# it seems will do download everytime, how to save and reuse it
model = whisper.load_model('base')

model.device
openai.api_key="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"

def transcribe_02(audio):
    audio_file = open(audio, "r")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    secret_key = "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"
    return transcript.text
    
    

def transcribe_01(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    # mel spectrogram https://zhuanlan.zhihu.com/p/351956040
    # transfer audio wave freq to a relation curve relative to human sensibility to sound (not linear) 
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, prob = whisper.detect_language(model, mel)
    
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    
    return result.text

#transcribe()

#gradle ui
output_1 = gr.Textbox(label='text to speech')
#output_2 = gr.Textbox(label='ChatGpt output')

gr.Interface(
    title= 'title',
    fn = transcribe_01,
    inputs=[gr.inputs.Audio(source='microphone', type='filepath')],
    outputs=[output_1],
    live=True
).launch()
