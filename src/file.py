import scipy.io.wavfile as wavfile

class File:
    def __init__(self, rate,content, name):
        self.rate = rate
        self.content = content
        self.name = name

    def makeMono(self):
        self.content = self.content.mean(axis=1) if len(self.content.shape) > 1 else self.content

    # Skalierung auf +-32765 und umwandeln in Integer / Normalisieren
    def normalize(self):
        self.content /= max(abs(self.content))
        self.content *= (2 ** 15 - 1)
        self.content = self.content.astype('int16')

    def showStats(self):

        rate = self.rate
        data = self.content
        name = self.name

        N = data.shape[0]
        CHN = data.shape[1] if len(data.shape) == 2 else 1
        print(f"+----------------------------------------+")
        print(f"Audiodatei {name} mit Abtastrate {rate}Hz")
        print(f"Anzahl der Abtastwerte in der Datei: {N}")
        print(f"Anzahl der Audio-Kanäle (1=Mono, 2=Stereo): {CHN}")
        print(f"Dauer: {N / rate:.3f}s")
        print("Die ersten Vier Abtastwerte:")
        print(data[:4])
        print(f"+----------------------------------------+")


def setUp(wav):
    rate, content = wavfile.read(wav)
    return File(rate, content, wav)
