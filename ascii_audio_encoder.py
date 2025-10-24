import soundfile as sf
import numpy as np 
from pathlib import Path 

def generateAudioFile(duration, frequencies, output_filename, samplerate = 44100):
    extra_data_path = 'extra_data.txt'
    folder_path = Path('encoded_audio')
    folder_path.mkdir(parents= True, exist_ok= True)

    tone_duration = duration/len(frequencies)

    t = np.linspace(0, tone_duration, int(samplerate * tone_duration), endpoint=False)

    audio_data = np.concatenate([
        0.5 * np.sin(2 * np.pi * f * t) for f in frequencies
    ])


    sf.write(folder_path / output_filename, audio_data, samplerate)

    with open(folder_path/extra_data_path, 'w') as f:
        f.write('Tone Duration: ' + str(tone_duration) + '\n')
        f.close()



def generate_tones(text):
        return [110 + (ord(c) - 32) * 10 for c in text]


