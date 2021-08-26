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

#Tokenization into seneteses 
words=word_tokenize(text)

#Stop word filtration 
stop_words= stopwords.words('english')
 
filtered_Sentense =[w for w in words if not w.lower() in stop_words]

filtered_Sentense=" ".join(filtered_Sentense)
print(filtered_Sentense)
analysis = TextBlob(filtered_Sentense).sentiment
print(analysis)


