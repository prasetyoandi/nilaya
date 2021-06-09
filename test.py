# from beeply import notes
# n = notes.beeps()

# import snowboy.snowboydecoder as snowboydecoder
# def detected_callback():
#     print("hotword detected")
# detector = snowboydecoder.HotwordDetector("nilaya.pmdl", sensitivity=0.5, audio_gain=1)
# detector.start(detected_callback)

# import speech_recognition as sr
# recognizer = sr.Recognizer()
# mic = sr.Microphone()
# while 1 :
#     with mic as source :
#         recognizer.adjust_for_ambient_noise(source)
#         print('siap')
#         audio = recognizer.listen(source)
#         response = recognizer.recognize_google(audio, language='id-ID')
#         print(response)