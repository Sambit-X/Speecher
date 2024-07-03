import speech_recognition as sr

def speech_process(file):
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio_text = r.listen(source)
        
        try:
            text = r.recognize_google(audio_text)
            return(text)
        except:
            return("Error in process module!")
        
