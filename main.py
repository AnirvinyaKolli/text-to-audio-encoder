import ascii_audio_encoder 
import tkinter as tk 
from tkinterdnd2 import DND_FILES, TkinterDnD

encoder = ascii_audio_encoder.AudioEncoder()

root = TkinterDnD.Tk()
root.title("Audio Encoder")
root.geometry("800x600")

#encode
tk.Label(root, text="Text to Encode:").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack()

tk.Label(root, text="Output Audio Filename (.wav):").pack(pady=5)
filename_entry = tk.Entry(root, width=40)
filename_entry.pack()

tk.Label(root, text="Tone Duration for Encoding (seconds):").pack(pady=5)
encode_duration_entry = tk.Entry(root, width=30)
encode_duration_entry.pack()

tk.Label(root, text=" Base Frequency (Hz) for Encoding :").pack(pady=5)
encode_base_entry = tk.Entry(root, width=30)
encode_base_entry.pack()

tk.Label(root, text=" Frequency Step (Hz) for Encoding :").pack(pady=5)
encode_step_entry = tk.Entry(root, width=30)
encode_step_entry.pack()

encode_output_label = tk.Label(root, text="", wraplength=300)
encode_output_label.pack(pady=10)

def encode_audio():
    entries = [
    text_entry.get(),
    filename_entry.get(),
    encode_duration_entry.get(),
    encode_base_entry.get(),
    encode_step_entry.get()
    ]
    if any(not e for e in entries):
        encode_output_label.config(text="Please fill in all fields before encoding.")
        return

    text = text_entry.get()
    out_filepath = filename_entry.get()
    duration = float(encode_duration_entry.get())
    base_freq = float(encode_base_entry.get())
    freq_step = float(encode_step_entry.get())
    result = encoder.generateAudioFile(duration, text, out_filepath, base_freq, freq_step)
    encode_output_label.config(text=result)

tk.Button(root, text="Encode Text to Audio", command=encode_audio).pack(pady=10)

#decode
def on_drop(event):
    global audio_path

    file_path = event.data.strip("{}")  
    if file_path.lower().endswith((".wav")):
        audio_path = file_path
        entry_field.config(text=file_path)
    else:
        entry_field.config(text = "WRONG!")

entry_field = tk.Label(root, text="Drag and drop the .wav file here", bg="#A7A7A7", padx=10, pady=30)
entry_field.pack(expand=True, fill="both", padx=20, pady=20)

entry_field.drop_target_register(DND_FILES)
entry_field.dnd_bind('<<Drop>>', on_drop)

tk.Label(root, text="Tone Duration (seconds):").pack(pady=5)
duration_entry = tk.Entry(root, width=30)
duration_entry.pack()

tk.Label(root, text="Base Frequency (Hz):").pack(pady=5)
base_freq_entry = tk.Entry(root, width=30)
base_freq_entry.pack()

tk.Label(root, text="Frequency Step (Hz):").pack(pady=5)
freq_step_entry = tk.Entry(root, width=30)
freq_step_entry.pack()

output_label = tk.Label(root, text="", wraplength=300)
output_label.pack(pady=10)


    
def decode_audio():
    if not audio_path:
        output_label.config(text="none provided")
        return 
    
    tone_duration = float(duration_entry.get())
    base_freq = float(base_freq_entry.get())
    freq_step = float(freq_step_entry.get())

    result = encoder.decodeAudio(tone_duration, base_freq, freq_step, audio_path)
    output_label.config(text=f"Decoded Text: {result}")
    

tk.Button(root, text="Decode Audio", command=decode_audio).pack(pady=10)

root.mainloop()



