import numpy as np
import math

class DataMemory():
    def __init__(self, size_data, rate, cent_freq):
        self.size_data = size_data
        self.data = np.array([0] * size_data)
        self.data_array = np.array([0] * (15 * size_data), 'float64').reshape(15, size_data)
        self.max = 0
        self.curMax = 0
        self.cur_spectrum = np.array([0] * size_data)
        #self.list_freq1 = (cent_freq + (np.arange(0, rate, rate / size_data) - (rate / 2) + (rate / size_data))) / 1e6
        print(type(cent_freq), cent_freq)
        print(type(rate), rate)

        self.list_freq = np.linspace(cent_freq - rate/2, cent_freq + rate/2, size_data)/1e6
        #print('lens ', len(self.list_freq1), len(self.list_freq2))
        # print(self.list_freq1)
        # print(self.list_freq2)
        self.freq_max = 0
        self.detect_sygnals = []
        self.count_detect = 0
        self.status_exit = False
        self.rate = rate

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = np.copy(data)
        self.data_array = np.roll(self.data_array, 1, axis=0)
        spec = self.get_spectrum()
        self.data_array[0] = spec
        ##print('self_data_array=', self.data_array)
        self.cur_spectrum = np.copy(self.get_spectrum())
        self.curMax = np.max(self.cur_spectrum)
        if self.curMax > 0.1:
            self.detect_sygnals.append(data)
            self.count_detect += 1

        if self.curMax > self.max:
            self.max = self.curMax


    def get_spectrum(self):
        return 10 * math.log10(np.abs(np.fft.fftshift(np.fft.fft(self.data, self.size_data)/self.size_data)))


    def get_cur_max(self):
        return self.curMax


    def get_max(self):
        return self.max


    def get_index_max(self):
        return np.where(self.data == self.max)


    def get_list_freq(self):
        return self.list_freq


    def get_freq_of_max(self):
        return self.list_freq[np.where(self.cur_spectrum == self.curMax)]


    def get_status(self):
        return self.status_exit


    def get_detect(self):
        for detect in self.detect_sygnals:
            yield detect

    # def getAmplitudes(self):
    #     return signal.periodogram(self.data, self.rate, 'flattop', scaling='spectrum')

    def get_data_array(self):
        return self.data_array