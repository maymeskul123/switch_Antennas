import SoapySDR
import numpy as np
from threading import Thread

class Device_sdr:
    def __init__(self, chank_size, ref_window, data_mem):
        self.results = None
        self.results = self.find_devices()
        self.rcv_status = False
        self.data = data_mem
        for result in self.results:
            print('-', result)
            d = dict(result)
            if d['driver'] == 'rtlsdr':
                dev = d['driver']
                print(f'Found {dev}')
                self.sdr = SoapySDR.Device(dict(driver=d['driver']))
                self.sdr.setSampleRate(SoapySDR.SOAPY_SDR_RX, 0, ref_window.get_samprate_value())
                self.sdr.setFrequency(SoapySDR.SOAPY_SDR_RX, 0, ref_window.get_freq_value())
                self.sdr.setGain(SoapySDR.SOAPY_SDR_RX, 0, ref_window.get_gain_value())
                #self.rx_stream = self.sdr.setupStream(SoapySDR.SOAPY_SDR_RX, 'CF32', [chank_size])
                self.rx_stream = self.sdr.setupStream(SoapySDR.SOAPY_SDR_RX, SoapySDR.SOAPY_SDR_CF32)
                self.sdr.activateStream(self.rx_stream)
                self.buff = np.array([0] * chank_size, np.complex64)


    def start_thread_rcv(self):
        self.rcv_status = True
        start = Thread(target=self.receive_signal).start()


    def stop_thread_rcv(self):
        self.rcv_status = False


    def find_devices(self):
        return SoapySDR.Device.enumerate()


    def receive_signal(self):
        while self.rcv_status:
            self.sdr.readStream(self.rx_stream, [self.buff], len(self.buff))
            self.data.set_data(self.buff)
            print(self.buff)
        self.sdr.deactivateStream(self.rx_stream)
        self.sdr.closeStream(self.rx_stream)
        exit()


    def set_rcv_status(self, rcv_status):
        self.rcv_status = rcv_status