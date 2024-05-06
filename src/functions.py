import scipy.io.wavfile as wavfile
from scipy import signal


def read_file(filename):
    rate, amp_list = wavfile.read(filename)
    return rate, amp_list


def get_mono(amp_list):
    amp_list = amp_list.mean(axis=1) if len(amp_list.shape) > 1 else amp_list
    return amp_list


def convolve(amp_signal, amp_response):
    wet_signal = signal.fftconvolve(amp_signal, amp_response)
    return wet_signal


def normalize(amp_list):
    amp_list /= max(abs(amp_list))
    amp_list *= (2 ** 15 - 1)
    amp_list = amp_list.astype('int16')
    return amp_list


def write_file(amp_list, filename, rate):
    wavfile.write(filename, rate, amp_list)

def show_stats(rate,data,filename):

    N = data.shape[0]
    CHN = data.shape[1] if len(data.shape) == 2 else 1
    print(f"Audiodatei {filename} mit Abtastrate {rate} Hz")
    print(f"Anzahl der Abtastwerte in der Datei: {N}")
    print(f"Anzahl der Audio-Kanäle(1=Mono, 2=Stereo): {CHN}")
    print("Die ersten vier Abtastwerte:")
    print(data[:4])