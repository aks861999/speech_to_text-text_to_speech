import speech_recognition as sr
r = sr.Recognizer()
sound_file = 'path to the audio file in .wav format'
file_audio = sr.AudioFile(sound_file)
with file_audio as source:
    audio_text = r.record(source)
print(r.recognize_google(audio_text))
