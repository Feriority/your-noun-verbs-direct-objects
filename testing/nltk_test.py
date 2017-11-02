from os import path

import nltk
import speech_recognition as sr


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "dts.wav")


text = None
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


if text is None:
    exit(1)
tokens = nltk.word_tokenize(text)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
