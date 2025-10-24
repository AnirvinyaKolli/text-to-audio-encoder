import ascii_audio_encoder as encoder
import ascii_audio_decoder as decoder

text = input('Enter text here: ')
out_filepath = 'output_audio.wav'
duration = float(input('Enter duration here: '))

encoder.generateAudioFile(duration, encoder.generate_tones(text), out_filepath)

tone_duration = float(input("enter tone duration: "))

print(decoder.decodeAudio(tone_duration, 'encoded_audio\output_audio.wav'))

