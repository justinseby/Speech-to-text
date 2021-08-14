# Speech-transcribe-with-sentiment-value
To build a model to recognize emotion from speech and transcribed, then convert into a sentiment value


## Table of contents
* [General info](#general-info)
* [Technologies](#Technologies)
* [Code Examples](#codeexamples)
* [Contact](#contact)

## General info
AS an user i should be able to give path of the audio file and the program displays the sentiment score of the overall audio file.
(you are free to choose sentiments, opensource models and codes please ensure that there is no complete copy paste done)

## Technologies
Python (nltk, speech_recognition etc)

## Code Examples
  
import speech_recognition as sr
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

r = sr.Recognizer()


#Opening the audio file
with sr.AudioFile("1.wav") as source:
    print('Audio analysed')
    audio = r.listen(source)   
try:
    print("Working on.....")
    text =r.recognize_google(audio)
    print(text)


except Exception as e:
    print(e)
  
## Contact
created by [@justinseby] - feel free to contact me
