import scipy.io.wavfile as wavfile
from scipy import signal

isSpeichern = True

eingabe = input("Hallo :) Möchtest du eigene Dateien mit Hall belegen oder welche von unseren Presets nutzen? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")
if (eingabe == "E"):
    zuFaltendeDatei = input("Geben Sie den Pfad für die zu faltende Datei an: ")
    impulsAntwort = input("Geben Sie den Pfad für die Impulsantwort an: ")

elif(eingabe == "P"):
    zuFaltendeDatei = 'spoken.wav'
    impulsAntwort = 'big_hall.wav'
"""
else:
    print("Sie haben keinen gültigen Buchstaben eingeben!")
"""

# Dateien einlesen
rate1, x = wavfile.read(zuFaltendeDatei)
rate2, h = wavfile.read(impulsAntwort)

# Methode zum Falten
def convolve(file1, file2):
    assert (rate1 == rate2)
    x = x.mean(axis=1) if len(x.shape) > 1 else x
    h = h.mean(axis=1) if len(h.shape) > 1 else x
    #Faltung
    gefaltet = signal.fftconvolve(x, h)
    # Skalierung auf +-32765 und umwandeln in Integer
    gefaltet /= max(abs(gefaltet))
    gefaltet *= (2 ** 15 - 1)
    gefaltet = gefaltet.astype('int16')
    return gefaltet

# Metadaten der Datei ausgeben
def showStats(file):

    roomfn = file
    rate, data = wavfile.read(roomfn)
    N = data.shape[0]
    CHN = data.shape[1] if len(data.shape) == 2 else 1

    print(f"Audiodatei {roomfn} mit Abtastrate {rate}Hz")
    print(f"Anzahl der Abtastwerte in der Datei: {N}")
    print(f"Anzahl der Audio-Kanäle (1=Mono, 2=Stereo): {CHN}")
    print(f"Dauer: {N / rate:.3f}s")
    print("Die ersten Vier Abtastwerte:")
    print(data[:4])

# Ergebnis abspeichern
wavfile.write('presetOutput.wav', rate1, y)

if __name__ == '__main__':
    pass