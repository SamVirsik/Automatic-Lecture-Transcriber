import queue
import pyaudio
import vosk
import json

print("What is this class?")
curr_class = input()
print("What is a date identifier?")
date = input()

model = vosk.Model(r"C:\Users\samvi\Documents\Coding Projects\Automatic Notetaking\vosk-model-en-us-0.22-lgraph")

q = queue.Queue()
def callback(in_data, frame_count, time_info, status):
    q.put(in_data)
    return None, pyaudio.paContinue

audio = pyaudio.PyAudio()
# 2 8

mic_index = 2  # Replace with your actual mic index 
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000, stream_callback=callback, input_device_index=mic_index)


#mic_index = 1  # or try 1, 5, 14, 15
#stream = audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=4000, stream_callback=callback, input_device_index=mic_index)


stream.start_stream()

output_file = curr_class + '_' + date + ".txt"

recognizer = vosk.KaldiRecognizer(model, 16000)
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