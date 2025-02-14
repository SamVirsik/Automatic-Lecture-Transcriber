import queue
import pyaudio
import vosk
import json

print("What is this class?")
curr_class = input()
print("What is a date identifier?")
date = input()

# Load model
model = vosk.Model(r"C:\Users\samvi\Documents\Coding Projects\Automatic Notetaking\vosk-model-en-us-0.22-lgraph")

# Set up audio streaming from system output
q = queue.Queue()

def callback(in_data, frame_count, time_info, status):
    q.put(in_data)
    return None, pyaudio.paContinue

audio = pyaudio.PyAudio()

# Find the correct system output device
system_audio_index = 25  # Replace with the correct index from the device list

stream = audio.open(format=pyaudio.paInt16, channels=2, rate=48000,  # Change sample rate if needed
                    input=True, frames_per_buffer=4000, 
                    stream_callback=callback, input_device_index=system_audio_index)

# Open a file to store transcriptions
output_file = f"{curr_class}_{date}.txt"

# Process audio continuously
recognizer = vosk.KaldiRecognizer(model, 44100)  # Match sample rate
with open(output_file, "a") as f:
    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())  # Parse as JSON
            text = result.get("text", "").strip()
            if text:  # Only print and save if there's actual text
                print(text)
                f.write(text + "\n")
                f.flush()  # Ensure it's written immediately