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
        assert isinstance(duration, int) and duration >= 0, "Duration must be a non-negative integer."
        self.duration = duration
        self.remaining = duration
        self.state = TimerState.IDLE

    def start(self):
        self.state = TimerState.RUNNING
        while self.remaining > 0:
            if self.state == TimerState.PAUSED:
                time.sleep(0.1)
                continue
            print(f"T-minus {self.remaining} seconds")
            logging.info(f"T-minus {self.remaining} seconds")
            time.sleep(1)
            self.remaining -= 1
        self.state = TimerState.COMPLETE
        print("Launch!")
        logging.info("Launch!")

    def pause(self):
        if self.state == TimerState.RUNNING:
            self.state = TimerState.PAUSED

    def resume(self):
        if self.state == TimerState.PAUSED:
            self.state = TimerState.RUNNING

    def reset(self):
        self.remaining = self.duration
        self.state = TimerState.IDLE

def main():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        timer = CountdownTimer(seconds)
        timer.start()
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
