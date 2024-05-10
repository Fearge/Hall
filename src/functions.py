#os für verschiedenes
import os
#Library für Faltung
import scipy.io.wavfile as wavfile
from scipy import signal
#Library für Abspielen auf Soundcarte
import sounddevice as sd
#Library für Auswahl von Datei über Explorer
import tkinter as tk
from tkinter import filedialog

import file


# Methode zum Falten
def convolve(file1, file2):
    assert (file1.rate == file2.rate)
    # Faltung
    gefaltet = signal.fftconvolve(file1.content, file2.content)

    gefaltetFile = file.File(file1.rate, gefaltet,file1.name + '_gefaltet')
    return gefaltetFile


# Ergebnis ausgeben, entweder auf Soundkarte oder als .wav Datei
def ausgabe(fileOut, isSpeichern):
    # als .wav
    if (isSpeichern):
        wavfile.write(input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".wav", fileOut.rate,
                      fileOut.content)
    else:
        #Auf Soundkarte
        sd.play(fileOut.content, fileOut.rate)
        input("Drücke die Eingabetaste, um den Sound anzuhalten")
        sd.stop()

def select_file():
    file = filedialog.askopenfilename()
    return file


# Metadaten der Datei ausgeben


