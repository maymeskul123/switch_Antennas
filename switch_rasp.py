#import RPi.GPIO as GPIO
import time
from threading import Thread

class Switch_rasp(Thread):
    def __init__(self, swA = 11, swB = 13, swC = 15): #17, 27, 22 are default ports

        # Pin Definitons:
        super().__init__()
        self.switchA = swA
        self.switchB = swB
        self.switchC = swC
        self.rfs = ['000', '100', '010', '110', '001', '101']
        self.off = ['011', '111']
        self.index_sw = 0
        self.running = True
        self.rf_on = 0
        self.data = None
        self.pin_setup()

    def run(self):
        while self.running:
            print("data", self.data)

    def terminate_switch(self):
        self.running = False

    def run_switch_rfs(self, period):
        while self.running:
            for port in range(5):
                print("Set ", self.rfs[port])
                # self.set_rf(self.index_sw)
                self.rf_on = port
                time.sleep(period)

    def get_status_rf(self):
        return self.rf_on


    def set_data(self, dataSdr):
        self.data = dataSdr

    def pin_setup(self):
        pass
        # GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
        # GPIO.setup(self.switch1, GPIO.OUT)
        # GPIO.setup(self.switch2, GPIO.OUT)
        # GPIO.setup(self.switch3, GPIO.OUT)
    #
    def set_rf(self, rf):                               #0 = rf1, ....6, 7 = ALLOFF
        pass
    #     for i, sw in enumerate(self.allRf[rf]):
    #         if sw == '1':
    #             GPIO.output(self.switches[i], GPIO.HIGH)
    #         elif sw == '0':
    #             GPIO.output(self.switches[i], GPIO.LOW)
