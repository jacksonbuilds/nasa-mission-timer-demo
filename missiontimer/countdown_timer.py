import time
import logging
from enum import Enum

logging.basicConfig(filename='telemetry.log', level=logging.INFO, format='%(asctime)s %(message)s')

class TimerState(Enum):
    IDLE = 0
    RUNNING = 1
    PAUSED = 2
    COMPLETE = 3

class CountdownTimer:
    def __init__(self, duration: int):
        assert isinstance(duration, int) and duration >= 0
        self.duration = duration
        self.remaining = duration
        self.state = TimerState.IDLE

    def start(self):
        if self.state in [TimerState.IDLE, TimerState.PAUSED]:
            self.state = TimerState.RUNNING

    def tick(self):
        if self.state == TimerState.RUNNING and self.remaining > 0:
            print(f"T-minus {self.remaining} seconds")
            logging.info(f"T-minus {self.remaining} seconds")
            self.remaining -= 1
            time.sleep(1)
            if self.remaining == 0:
                print("Launch!")
                logging.info("Launch!")
                self.state = TimerState.COMPLETE

    def pause(self):
        if self.state == TimerState.RUNNING:
            self.state = TimerState.PAUSED
            logging.info("Timer paused")

    def resume(self):
        if self.state == TimerState.PAUSED:
            self.state = TimerState.RUNNING
            logging.info("Timer resumed")

    def reset(self):
        self.remaining = self.duration
        self.state = TimerState.IDLE
        logging.info("Timer reset")
