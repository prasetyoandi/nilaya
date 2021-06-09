import speech_recognition as sr # mengambil library python untuk STT 
import config # mengambil file konfigurasi
from subprocess import call # mengambil library python untuk menjalankan command, disini digunakan untuk menjalankan file wav
from intent_recognition import getIntent # mengambil untuk mengolah text hasil dari STT google
import hass # mengambil file program untuk mengirim perintah ke hass.io
import snowboy.snowboydecoder as snowboydecoder # mengambil program dari snowboy
import time

def console(message) : # fungsi untuk menampilkan pesan pada console dan menuliskannya pada log file
    print(message)
    f=open("log.out.log", "a+")
    f.write(message + '\n')
    f.close()

def detected_callback(): # fungsi yang berjalan saat nilaya terdeteksi
    console('DIPANGGIL')
    r = sr.Recognizer()
    mic = sr.Microphone() # menyiapkan microphone untuk stt
    voice = ''
    with mic as source :
        call(['aplay', '-q', 'snowboy/resources/ding.wav']) # play suara ding
        r.adjust_for_ambient_noise(source) # digunakan untuk merekam noise, sehingga nantinya tidak dianggap suara
        audio = r.listen(source) # mendengarkan perintah
        call(['aplay', '-q', 'snowboy/resources/dong.wav']) # play suara dong
        try :
            voice = r.recognize_google(audio, language='id-ID') # mengirim suara ke google untuk melakukan STT
        except : {}
        voice = voice.lower()
    console('command : ' + voice)
    intent = getIntent(voice) # melakukan analisa teks yang diterima dari google
    if intent is not None :
        console('intent  : ' + intent)
        res = hass.call(intent) # mengirim perintah ke hass.io
        console('hassio  : ' + res)
    time.sleep(1)
    console('SIAP')

# dibawah ini adalah fungsi dari snowboy
detector = snowboydecoder.HotwordDetector(config.wake_file, sensitivity=config.wake_sensitivity, audio_gain=config.wake_audio_gain)
detector.start(detected_callback)
