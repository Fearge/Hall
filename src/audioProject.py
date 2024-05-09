import scipy.io.wavfile as wavfile
from scipy import signal

import sounddevice as sd
import functions

#Todo: Fehlerbehandlung
sampleRate = 44100
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei =""

#Todo: Redundanzen reduzieren, vlt files als Liste



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
    normalizeGefaltet = functions.normalize(gefaltet)
    return normalizeGefaltet, rate1

if __name__ == '__main__':

    eingabe = input("Hallo :) Möchtest du eigene Dateien mit Hall belegen oder welche von unseren Presets nutzen? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

    if (eingabe.upper() == "E"):
        zuFaltendeDatei = input("Geben Sie den Pfad für die zu faltende Datei an: ")
        impulsAntwort = input("Geben Sie den Pfad für die Impulsantwort an: ")

    elif (eingabe.upper() == "P"):
        zuFaltendeDatei = 'WiiShopChannel.wav'
        impulsAntwort = 'big_hall.wav'

    #Todo: abfragen wie ausgegeben werden soll

    gefalteteDatei, sampleRate = convolve(zuFaltendeDatei, impulsAntwort)

    eingabe = (input("Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? (S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

    if (eingabe.upper() == "S"):
        ausgabe(gefalteteDatei, sampleRate, 1)

    elif (eingabe.upper() == "A"):
        ausgabe(gefalteteDatei, sampleRate, 0)



    """
    else:
        print("Sie haben keinen gültigen Buchstaben eingeben!")
    """