import ascii_audio_encoder 
import tkinter as tk 
from tkinter import filedialog

encoder = ascii_audio_encoder.AudioEncoder()

#setup of tkinter window
root = tk.Tk()
root.title("Audio Encoder")
root.geometry("800x600")

#Encoder

#Get text
tk.Label(root, text="Text to Encode:").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack()

#Get file name
tk.Label(root, text="Output Audio Filename (.wav):").pack(pady=5)
filename_entry = tk.Entry(root, width=40)
filename_entry.pack()

#Get duration 
tk.Label(root, text="Duration (seconds):").pack(pady=5)
encode_duration_entry = tk.Entry(root, width=30)
encode_duration_entry.pack()

#Get base frequency 
tk.Label(root, text=" Base Frequency (Hz):").pack(pady=5)
encode_base_entry = tk.Entry(root, width=30)
encode_base_entry.pack()

#Get frequency step 
tk.Label(root, text=" Frequency Step (Hz):").pack(pady=5)
encode_step_entry = tk.Entry(root, width=30)
encode_step_entry.pack()

#Define output label
encode_output_label = tk.Label(root, text="", wraplength=300)


#encode method
def encode_audio():
    try: 
        text = text_entry.get()
        duration = float(encode_duration_entry.get())
        base_freq = float(encode_base_entry.get())
        freq_step = float(encode_step_entry.get())
        output_dir = filedialog.askdirectory()
    except: 
        encode_output_label.config(text= "Please fill out all fields with an the proper value.")
        return
    
    out_filepath = filename_entry.get()
    
    if out_filepath == '':
        encode_output_label.config(text= "No folder chosen.")
        return
    
    save_dir = encoder.generateAudioFile(
        text=text, 
        duration=duration, 
        base_freq=base_freq, 
        freq_step=freq_step,
        output_dir=output_dir
    )
    
    encode_output_label.config(text=save_dir)

#Encode button
tk.Button(root, text="Encode Text to Audio", command=encode_audio).pack(pady=10)

encode_output_label.pack(pady=10)

#Decode

#Get tone duration
tk.Label(root, text="Tone Duration (seconds):").pack(pady=5)
duration_entry = tk.Entry(root, width=30)
duration_entry.pack()

#Get base frequency
tk.Label(root, text="Base Frequency (Hz):").pack(pady=5)
base_freq_entry = tk.Entry(root, width=30)
base_freq_entry.pack()

#Get frequency step
tk.Label(root, text="Frequency Step (Hz):").pack(pady=5)
freq_step_entry = tk.Entry(root, width=30)
freq_step_entry.pack()

# Define output label
decode_output_label = tk.Label(root, text="", wraplength=300)

# Decode function
def decode_audio():
    decode_output_label.config(text= "")

    try: 
        tone_duration = float(duration_entry.get())
        base_freq = float(base_freq_entry.get())
        freq_step = float(freq_step_entry.get())
    except: 
        decode_output_label.config(text= "Please fill out all fields with an the proper value.")
        return

    try:
        audio_file_path = filedialog.askopenfilename()
    except:
        decode_output_label.config(text="No file chosen")
        return 
    
    decoded_audio = encoder.decodeAudio(
        tone_duration=tone_duration,
        base_freq=base_freq, 
        freq_step=freq_step, 
        audio_file_path=audio_file_path
    )

    decode_output_label.config(text=f"Decoded Text: {decoded_audio}")
    
#Decode button
tk.Button(root, text="Decode Audio", command=decode_audio).pack(pady=10)
decode_output_label.pack(pady=10)

#Main loop
root.mainloop()



