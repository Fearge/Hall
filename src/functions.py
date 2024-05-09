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


def setUp(wav):
    fileBack = file.File()
    fileBack.rate, fileBack.content = wavfile.read(wav)
    return fileBack


# Methode zum Falten
def convolve(file1=file.File(),
             file2=file.File()):

    assert (file1.rate == file2.rate)

    # Umwandlung in Mono
    file1.makeMono()
    file2.makeMono()

    # Faltung
    gefaltet = signal.fftconvolve(file1.content, file2.content)

    # Skalierung auf +-32765 und umwandeln in Integer / Normalisieren
    normalizeGefaltet = normalize(gefaltet)
    return file.File(file1.rate, normalizeGefaltet)


# Ergebnis ausgeben, entweder auf Soundkarte oder als .wav Datei
def ausgabe(isSpeichern, fileOut = file.File()):
    # als .wav
    if (isSpeichern):
        wavfile.write(input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".wav", fileOut.content,
                      fileOut.rate)
    else:
        #Auf Soundkarte
        sd.play(fileOut.content, fileOut.rate)
        input("Drücke die Eingabetaste, um den Sound anzuhalten")
        sd.stop()


def normalize(amp_list):
    amp_list /= max(abs(amp_list))
    amp_list *= (2 ** 15 - 1)
    amp_list = amp_list.astype('int16')
    return amp_list


def select_file():
    file = filedialog.askopenfilename()
    return file


# Metadaten der Datei ausgeben
def showStats(file):
    rate, data = wavfile.read(file)
    N = data.shape[0]
    CHN = data.shape[1] if len(data.shape) == 2 else 1

    print(f"Audiodatei {file} mit Abtastrate {rate}Hz")
    print(f"Anzahl der Abtastwerte in der Datei: {N}")
    print(f"Anzahl der Audio-Kanäle (1=Mono, 2=Stereo): {CHN}")
    print(f"Dauer: {N / rate:.3f}s")
    print("Die ersten Vier Abtastwerte:")
    print(data[:4])
