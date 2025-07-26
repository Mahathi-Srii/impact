import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_path, wav_path="converted.wav"):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(mp3_file_path):
    wav_path = convert_mp3_to_wav(mp3_file_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results from Google API; {e}"
