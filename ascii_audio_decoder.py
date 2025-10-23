import soundfile as sf
import numpy as np 
from pathlib import Path

def decodeAudio(tone_duration,audio_file_path):
    audio_data = sf.read(audio_file_path)
    print("decoded: ", audio_data[0].shape)
