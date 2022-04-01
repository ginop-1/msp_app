import serial

class SerialConnection():
    def __init__(self, port: str):
        # init serial port
        self.conn = serial.Serial(port=port, baudrate=9600)

    def read(self):
        if self.conn.inWaiting() > 0:
            return self.conn.read(self.conn.inWaiting()).decode("ascii")

    def exit(self):
        self.conn.close()


if __name__ == "__main__":
    # main()
    pass
