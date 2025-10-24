import ascii_audio_encoder 

encoder = ascii_audio_encoder.AudioEncoder()

# text = input('Enter text here: ')
# out_filepath = input('Enter audio file name: ')
# duration = float(input('Enter duration here: '))

# print(encoder.generateAudioFile(duration, text, out_filepath))

audio_file_name = input("enter audio file name: ") 
tone_duration = float(input("enter tone duration: "))
base_freq = float(input("enter base frequency: "))
freq_step = float(input("enter frequency step: "))

out = encoder.decodeAudio(tone_duration, base_freq, freq_step, f'encoded_audio\\{audio_file_name}.wav')

print(out)