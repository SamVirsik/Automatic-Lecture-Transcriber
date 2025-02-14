import pyaudio
import numpy as np

# List all devices to find the right index
def list_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']} (Channels: {info['maxInputChannels']}, Sample Rate: {info['defaultSampleRate']})")
    p.terminate()

# Change this to the correct mic index
MIC_INDEX = 2  # Update this based on your selected mic

def check_mic_input(mic_index, rate=48000, channels=1, chunk=1024):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=int(rate),
                    input=True,
                    frames_per_buffer=chunk,
                    input_device_index=mic_index)

    print(f"Listening to Mic {mic_index}... Speak into it!")

    try:
        while True:
            data = np.frombuffer(stream.read(chunk, exception_on_overflow=False), dtype=np.int16)
            volume = np.linalg.norm(data) / np.sqrt(len(data))
            print(f"Volume Level: {volume:.2f}")
    except KeyboardInterrupt:
        print("\nStopping...")
        stream.stop_stream()
        stream.close()
        p.terminate()

# Run this first to find the right mic index
list_devices()

# Then, test a specific mic
check_mic_input(MIC_INDEX)