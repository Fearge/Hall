#Library für Faltung
import scipy.io.wavfile as wavfile
from scipy import signal
#Library für Abspielen auf Soundcarte
import sounddevice as sd
#Library für Auswahl von Datei über Explorer
import tkinter as tk
from tkinter import filedialog

# Methode zum Falten
def convolve(file1, file2):
    rate1, x = wavfile.read(file1)
    rate2, h = wavfile.read(file2)

    assert (rate1 == rate2)

    # Umwandlung in Mono
    x = x.mean(axis=1) if len(x.shape) > 1 else x
    h = h.mean(axis=1) if len(h.shape) > 1 else h

    # Faltung
    gefaltet = signal.fftconvolve(x, h)

    # Skalierung auf +-32765 und umwandeln in Integer
    normalizeGefaltet = normalize(gefaltet)
    return normalizeGefaltet, rate1

# Ergebnis ausgeben, entweder auf Soundkarte oder als .wav
def ausgabe(fileToPrint,rateToPrint,isSpeichern):
    # als .wav
    if(isSpeichern):
        wavfile.write(input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".wav", rateToPrint, fileToPrint)
    else:
        sd.play(fileToPrint,rateToPrint)
        input("Drücke die Eingabetaste, um den Sound anzuhalten")
        sd.stop()

def normalize(amp_list):
    amp_list /= max(abs(amp_list))
    amp_list *= (2 ** 15 - 1)
    amp_list = amp_list.astype('int16')
    return amp_list

def select_file():
    file = filedialog.askopenfilename()
    print(file)
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
