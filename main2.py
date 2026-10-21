import scipy.io.wavfile as wav
import sounddevice as sd
import speech_recognition as sr
import random
import time

words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banana", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"]
}

puntos = 0

while True:
    dificultad = input("🔴¿Que nivel quieres?(facil, medio, dificil)")
    for i in range(5):
        if dificultad == "facil":
            word = random.choice(words_by_level["facil"])
            print(word)

        elif dificultad == "medio":
            word = random.choice(words_by_level["medio"])
            print(word)

        elif dificultad == "dificil":
            word = random.choice(words_by_level["dificil"])
            print(word)


        duration = 2
        samplerate = 44100
        print("🟢Iniciando la grabación de audio...")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        wav.write("grabacion.wav", samplerate, recording)
        print("🔵Grabación completada. Procesando el audio...")

        recognizer = sr.Recognizer()
        with sr.AudioFile("./grabacion.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            print("Texto reconocido: " + text)
            if text == word:
                print("🏁🏁🏁Lo dijiste muy bien🏁🏁🏁")
                print("mas un punto")
                puntos += 1
            else:
                print("sigue practicando")


        except sr.UnknownValueError:
            print("No se pudo entender el audio.")

        print(puntos)
        time.sleep(6)


