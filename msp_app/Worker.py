from PyQt5.QtCore import QObject, pyqtSignal
import time

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self._isRunning = True

    def run(self):
        """Long-running task."""
        while True and self._isRunning:
            time.sleep(0.25)
            self.progress.emit()
        
        self.finished.emit()
    
    def stop(self):
        self._isRunning = False
