class File:
    def __init__(self, rate = 44100, content = ""):
        self.rate = rate
        self.content = content

    def makeMono(self):
        self.content = self.content.mean(axis=1) if len(self.content.shape) > 1 else self.content


    #Skalierung auf +-32765 und umwandeln in Integer / Normalisieren
    def normalize(self):
        self.content /= max(abs(self.content))
        self.content *= (2 ** 15 - 1)
        self.content = self.content.astype('int16')