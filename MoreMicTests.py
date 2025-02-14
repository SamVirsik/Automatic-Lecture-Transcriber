import pyaudio

# Initialize PyAudio
p = pyaudio.PyAudio()

# List all available audio devices
print("\nAvailable audio devices:\n")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device Index: {info['index']}")
    print(f"  Name: {info['name']}")
    print(f"  Input Channels: {info['maxInputChannels']}")
    print(f"  Sample Rate: {info['defaultSampleRate']}\n")

p.terminate()