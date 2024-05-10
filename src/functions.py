#os für verschiedenes
#Library für Faltung
import scipy.io.wavfile as wavfile
from scipy import signal
#Library für Abspielen auf Soundkarte
import sounddevice as sd
#Library für Auswahl von Datei über Explorer
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
    normalize_gefaltet = normalize(gefaltet)
    return normalize_gefaltet, rate1


# Ergebnis ausgeben, entweder auf Soundkarte oder als .wav
def ausgabe(file_to_print, rate_to_print, is_speichern):
    # als .wav
    if is_speichern:
        wavfile.write(input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".wav", rate_to_print,
                      file_to_print)
    else:
        sd.play(file_to_print, rate_to_print)
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
def show_stats(file):
    rate, data = wavfile.read(file)
    N = data.shape[0]
    CHN = data.shape[1] if len(data.shape) == 2 else 1

    print(f"Audiodatei {file} mit Abtastrate {rate}Hz")
    print(f"Anzahl der Abtastwerte in der Datei: {N}")
    print(f"Anzahl der Audio-Kanäle (1=Mono, 2=Stereo): {CHN}")
    print(f"Dauer: {N / rate:.3f}s")
    print("Die ersten Vier Abtastwerte:")
    print(data[:4])
