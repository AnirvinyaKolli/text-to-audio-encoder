import soundfile as sf
import numpy as np 
from pathlib import Path 

class AudioEncoder:
    def __init__(self, samplerate=44100):
        self.START_ASCII_CODE = 32 
        self.SAMPLE_RATE = samplerate
        self.DECODE_KEY_PATH =  "key.txt"
    
    def generateAudioFile(self, text, audio_filename = 'encoded_audio', duration = 10, base_freq=110, freq_step=10, output_dir = ''):
        
        frequencies, tone_duration = self.generate_tones(text, base_freq, freq_step, duration)

        t = np.linspace(0, tone_duration, int(self.SAMPLE_RATE * tone_duration), endpoint=False)
        audio_data = np.concatenate([
            0.5 * np.sin(2 * np.pi * f * t) for f in frequencies
        ])

        sf.write(Path(output_dir) / (audio_filename + ".wav"), audio_data, self.SAMPLE_RATE)

        with open(Path(output_dir) / (audio_filename + '_' + self.DECODE_KEY_PATH), 'w') as f:
            f.write("Tone Duration: " + str(tone_duration) + '\n')
            f.write("Base Frequency: " + str(base_freq) + '\n')
            f.write("Frequency Step: " + str(freq_step) + '\n')

            f.close()

        return "Files generated in " + output_dir 

    def generate_tones(self, text, base_freq, freq_step, duration):
            f = [base_freq + (ord(c) - self.START_ASCII_CODE) * freq_step for c in text]
            return f , duration/len(f)

    #Decoding 
    def decodeAudio(self, audio_file_path, tone_duration, base_freq, freq_step):

        audio_data = sf.read(audio_file_path)
        samples_per_tone = int(samplerate * tone_duration)
        num_tones = len(audio_data) // samples_per_tone

        segments = [
            audio_data[i * samples_per_tone : (i + 1) * samples_per_tone] for i in range(num_tones)
        ]
        
        frequencies = [self.estimate_frequency(seg) for seg in segments]

        return  ''.join(
                    [chr(int(round((f - base_freq) / freq_step + self.START_ASCII_CODE))) for f in frequencies]
                )

    def estimate_frequency(self, segment):
            
            fft_result = np.fft.fft(segment)
            freqs = np.fft.fftfreq(len(segment), 1 / self.SAMPLE_RATE)
            magnitude = np.abs(fft_result)
            positive_freqs = freqs[:len(freqs)//2]
            positive_magnitude = magnitude[:len(magnitude)//2]
            dominant_index = np.argmax(positive_magnitude)

            return positive_freqs[dominant_index]
        