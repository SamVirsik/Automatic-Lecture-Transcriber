# Automatic-Lecture-Transcriber
This project provides an automated transcription tool designed to capture and process spoken content from lectures, meetings, and system audio in real time. The program uses Vosk, a premade offline speech-to-text engine. The program enables users to record, transcribe, and store spoken words into text files for later review.

# Key Features
**Live Microphone Transcription:** Captures spoken words from a microphone input and transcribes them in real time.  
**System Audio Transcription:** Records and transcribes any sound output from a computer.  
**Automatic File Storage:** Saves transcriptions into a structured format for easy access and review.  
**Customizable Microphone Selection:** Allows users to test and select the appropriate audio input device.  

# Project Structure
## Audio Handling
The program uses pyaudio to manage audio streams, either pulling input from a microphone or a system output device.  
Users select the desired microphone or speaker to pull audio from.  
The scripts process audio in small chunks to acheive real-time transcription. 

## Speech-to-Text Processing
The program employs Vosk, an offline speech recognition model, to convert raw audio into structured text. (vosk-model-en-us-0.22-lgraph, 128MB)  
Audio is processed in small chunks and text output is printed as soon as it is recognized.  
Vosk’s recognition output is in JSON format, which is parsed to extract the final transcribed text.  

## File Management and Storage
All transcriptions are automatically saved to text files, making it easy to review lectures later.  
Uploading these transcripts to language models like ChatGPT allows for quick summarization and creating of detailed lecture notes. 
