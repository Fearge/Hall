

class File:
    def __init__(self, file):
        self.content, self.rate = wavfile.read(file)

