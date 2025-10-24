import ascii_audio_encoder 

encoder = ascii_audio_encoder.AudioEncoder()

text = input('Enter text here: ')
out_filepath = input('Enter audio file name: ')
duration = float(input('Enter duration here: '))

print(encoder.generateAudioFile(duration, text, out_filepath))


# tone_duration = float(input("enter tone duration: "))
# base_freq = float(input("enter base frequency duration: "))
# freq_step = float(input("enter frequency step duration: "))

# out = encoder.decodeAudio(tone_duration, 'encoded_audio\output_audio.wav')

