import ascii_audio_encoder as encoder
import ascii_audio_decoder as decoder

text = input('Enter text here: ')
out_filepath = 'output_audio.wav'
duration = int(input('Enter duration here: '))

encoder.generateAudioFile(duration, encoder.generate_tones(text), out_filepath)

decoder.decodeAudio(0.2857142857142857, 'encoded_audio\output_audio.wav')

