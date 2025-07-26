import os
from moviepy.config import change_settings

# Set FFmpeg binary path
ffmpeg_path = r"C:\Users\RAMYA S\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
change_settings({"FFMPEG_BINARY": ffmpeg_path})

import speech_recognition as sr
from pydub import AudioSegment
import os

# Step 1: Convert MP3 to WAV using pydub
mp3_file = "sample.mp3"
wav_file = "sample.wav"

sound = AudioSegment.from_mp3(mp3_file)
sound.export(wav_file, format="wav")

# Step 2: Initialize recognizer and read the audio
recognizer = sr.Recognizer()

with sr.AudioFile(wav_file) as source:
    audio_data = recognizer.record(source)

# Step 3: Try recognizing the speech
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcribed Text:\n", text)
except sr.UnknownValueError:
    print("Speech was unintelligible.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
