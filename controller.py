from dataMemory import DataMemory
from device import Device_sdr
import numpy as np
from threading import Thread
import time
from switch_rasp import Switch_rasp

CHANK_SIZE = 16000

class Controller:

    def __init__(self):
        self.window = None
        self.data = None
        self.device = None
        self.event_status = False

    def load_window(self, window):
        self.window = window

    def start_event(self):
        self.data = DataMemory(CHANK_SIZE, self.window.get_samprate_value(), \
                          self.window.get_freq_value())
        self.device = Device_sdr(CHANK_SIZE, self.window, self.data)
        self.event_status = True
        self.device.start_thread_rcv()
        self.rasp = Switch_rasp()
        self.thread_max = Thread(target=self.find_max_min).start()
        self.thread_ras = Thread(target=self.rasp.run_switch_rfs, args=[self.window.get_periodic(), ]).start()

    def stop_event(self):
        self.device.stop_thread_rcv()
        self.event_status = False
        self.rasp.terminate_switch()

    def find_max_min(self):
        prev_rf = 0
        change = False
        while self.event_status:
            cur_rf = self.rasp.get_status_rf()
            #print(cur_rf)
            if cur_rf == prev_rf and not change:
                self.window.set_color_label_ant(cur_rf, 0, 0, 255)
                change = True
            elif cur_rf != prev_rf:
                self.window.set_color_label_ant(prev_rf, 190, 191, 188)
                self.window.set_label_lev(prev_rf, "0.0")
                change = False
            #max_f = self.data.get_freq_of_max()
            max = self.data.get_cur_max()
            self.window.set_label_lev(cur_rf, str(np.around(max, decimals=2)))
            time.sleep(0.1)
            self.window.set_max_val(str(np.around(max, decimals=2)))
            time.sleep(0.1)
            prev_rf = cur_rf

            #self.window.set_max_val("ura")
        print('Close Find_max_min')
        quit()
