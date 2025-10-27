import soundfile as sf
import numpy as np 
from pathlib import Path 

class AudioEncoder:
    def __init__(self, samplerate=44100,  output_dir="encoded_audio", decode_key_path = "key.txt"):

        self.START_ASCII_CODE = 32 
        
        self.samplerate = samplerate
        self.output_dir = Path(output_dir)        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.decode_key_path = decode_key_path
    
    def generateAudioFile(self, duration, text, output_filename, base_freq=110, freq_step=10, computer_location = ''):
        
        frequencies = self.generate_tones(text, base_freq, freq_step)

        tone_duration = duration/len(frequencies)

        t = np.linspace(0, tone_duration, int(self.samplerate * tone_duration), endpoint=False)
        audio_data = np.concatenate([
            0.5 * np.sin(2 * np.pi * f * t) for f in frequencies
        ])

        sf.write(Path(computer_location) / (output_filename + ".wav"), audio_data, self.samplerate)

        with open(Path(computer_location) / (output_filename + '_' + self.decode_key_path), 'w') as f:
            f.write("Tone Duration: " + str(tone_duration) + '\n')
            f.write("Base Frequency: " + str(base_freq) + '\n')
            f.write("Frequency Step: " + str(freq_step) + '\n')

            f.close()

        return "Files generated in " + computer_location 

    def generate_tones(self, text, base_freq, freq_step):
            return [ base_freq + (ord(c) - self.START_ASCII_CODE) * freq_step for c in text]

    #Decoding 
    def decodeAudio(self, tone_duration, base_freq, freq_step, audio_file_path):

        audio_data, samplerate = sf.read(audio_file_path)
        samples_per_tone = int(samplerate * tone_duration)
        num_tones = len(audio_data) // samples_per_tone

        segments = [
            audio_data[i * samples_per_tone : (i + 1) * samples_per_tone] for i in range(num_tones)
        ]
        
        frequencies = [self.estimate_frequency(seg, samplerate) for seg in segments]

        return  ''.join(
                    [chr(int(round((f - base_freq) / freq_step + self.START_ASCII_CODE))) for f in frequencies]
                )

    def estimate_frequency(self, segment, samplerate):
            
            fft_result = np.fft.fft(segment)
            freqs = np.fft.fftfreq(len(segment), 1 / samplerate)
            magnitude = np.abs(fft_result)
            positive_freqs = freqs[:len(freqs)//2]
            positive_magnitude = magnitude[:len(magnitude)//2]
            dominant_index = np.argmax(positive_magnitude)

            return positive_freqs[dominant_index]
        