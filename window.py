from PyQt5 import QtCore, QtWidgets, QtGui
import test_ant

class MainWindow(QtWidgets.QWidget, test_ant.Ui_Form):
    def __init__(self, control):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start_test)
        self.stopButton.clicked.connect(self.stop_test)
        self.control = control
        self.control.load_window(self)

    def start_test(self):
        self.control.start_event()

    def stop_test(self):
        self.control.stop_event()

    def get_freq_value(self):
        return float(self.lineFrequency.text())*1e6

    def get_gain_value(self):
        return float(self.lineGain.text())

    def get_samprate_value(self):
        return float(self.lineRate.text()) * 1e6

    def set_max_val(self, max):
        self.label_max.setText(max)

    def set_color_label_ant(self, num, r, g, b):
        labels =\
            [
                self.label_lev1.setStyleSheet,
                self.label_lev2.setStyleSheet,
                self.label_lev3.setStyleSheet,
                self.label_lev4.setStyleSheet,
                self.label_lev5.setStyleSheet
            ]
        if num >= 0 and num < 5:
            labels[num](f'background-color: rgb({str(r)}, {str(g)}, {str(b)});')

    def get_periodic(self):
        return float(self.linePeriodic.text())

    def set_label_lev(self, num, val):
        labels = \
            [
                self.label_lev1,
                self.label_lev2,
                self.label_lev3,
                self.label_lev4,
                self.label_lev5
            ]
        labels[num].setText(val)

    #def set_antenna(self, num):

