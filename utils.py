# utils.py
import time
import threading

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.time_left = duration

    def start(self):
        def countdown():
            while self.time_left > 0:
                time.sleep(1)
                self.time_left -= 1

        threading.Thread(target=countdown).start()
