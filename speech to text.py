### An open source contribution by Akash ###

#import the module speech_recognition
import speech_recognition as sr
r = sr.Recognizer()
sound_file = 'path to the audio file in .wav format'
file_audio = sr.AudioFile(sound_file)
        
try:
    # set the newly read audio file as the source to recognise as speech object
    with file_audio as source2: 
        # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level  
        r.adjust_for_ambient_noise(source2, duration=0.5) 

        #record the user's input  
        audio2 = r.record(source2) 

        #save the recognised text in an object called 'text' for further processing
        text = r.recognize_google(audio2,key=None, show_all = False) 
        
        # Now create a text file for further processing
        f = open("extracted.txt", "w")
        f.write(text)
        f.close()

# what if Error occur in Requesting the Endpoint
except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
# what if the API get Unknown Value Returned from Endpoint
except sr.UnknownValueError: 
        print("unknown error occured") 
