import soundfile as sf
import numpy as np 
from pathlib import Path

def decodeAudio(tone_duration,audio_file_path):
    audio_data, samplerate = sf.read(audio_file_path)

    samples_per_tone = int(samplerate * tone_duration)
    num_tones = len(audio_data) // samples_per_tone

    segments = [
        audio_data[i * samples_per_tone : (i + 1) * samples_per_tone] for i in range(num_tones)
    ]
    
    frequencies = [estimate_frequency(seg, samplerate) for seg in segments]
    return ''.join([chr(int(round((f - 110) / 10 + 32))) for f in frequencies])

def estimate_frequency(segment, samplerate):
        fft_result = np.fft.fft(segment)
        freqs = np.fft.fftfreq(len(segment), 1 / samplerate)
        magnitude = np.abs(fft_result)

        positive_freqs = freqs[:len(freqs)//2]
        positive_magnitude = magnitude[:len(magnitude)//2]

        dominant_index = np.argmax(positive_magnitude)
        return positive_freqs[dominant_index]
    