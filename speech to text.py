### An open source contribution by Akash ###

#import the module speech_recognition
import speech_recognition as sr
r = sr.Recognizer()
sound_file = 'path to the audio file in .wav format'
file_audio = sr.AudioFile(sound_file)

# set the newly read audio file as the source to recognise as speech object
with file_audio as source:
    audio_text = r.record(source)

#save the recognised text in an object called 'text' for further processing
text= r.recognize_google(audio_text)

print(r.recognize_google(audio_text))

# Now create a text file for further processing
f = open("extracted.txt", "w")
f.write(text)
f.close()
