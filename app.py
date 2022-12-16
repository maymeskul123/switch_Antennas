from PyQt5 import QtWidgets
from window import MainWindow
from controller import Controller

def start():
    app = QtWidgets.QApplication([])
    control = Controller()
    window = MainWindow(control)
    #data = DataMemory(N, RATE, CENTER_FREQ_HZ)
    window.show()
    app.exec()

if __name__ == '__main__':
    start()
