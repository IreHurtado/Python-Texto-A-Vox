"""Convertir texto a voz usando la libreria pyttsx3"""
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
with open("texto.txt", "r") as file:
        texto = file.read()
engine.say(texto)
engine.runAndWait()