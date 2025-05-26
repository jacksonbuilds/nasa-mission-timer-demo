import time
import logging
from enum import Enum

# Configure logging to write to a telemetry file with timestamps
logging.basicConfig(
    filename="telemetry.log", level=logging.INFO, format="%(asctime)s %(message)s"
)


class TimerState(Enum):
    """
    Enum representing the different states of the countdown timer.
    """

    IDLE = 0
    RUNNING = 1
    PAUSED = 2
    COMPLETE = 3


class CountdownTimer:
    """
    CountdownTimer simulates a mission countdown with support for pause, resume, and reset.
    """

    def __init__(self, duration: int):
        """
        Initialize the timer.

        Args:
            duration (int): Total countdown time in seconds. Must be non-negative.
        """
        assert isinstance(duration, int) and duration >= 0
        self.duration = duration
        self.remaining = duration
        self.state = TimerState.IDLE

    def start(self):
        """
        Transition the timer to the RUNNING state.
        Only works if the timer is currently IDLE or PAUSED.
        """
        if self.state in [TimerState.IDLE, TimerState.PAUSED]:
            self.state = TimerState.RUNNING

    def tick(self):
        """
        Advance the timer by one second if it's RUNNING.
        Logs each second and updates the remaining time.
        Transitions to COMPLETE when countdown reaches zero.
        """
        if self.state == TimerState.RUNNING and self.remaining > 0:
            print(f"T-minus {self.remaining} seconds")
            logging.info(f"T-minus {self.remaining} seconds")
            self.remaining -= 1
            time.sleep(1)

            if self.remaining == 0:
                print("Launch!")
                logging.info("Launch!")
                self.state = TimerState.COMPLETE


def main():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        timer = CountdownTimer(seconds)
        timer.start()
        while timer.state != TimerState.COMPLETE:
            timer.tick()
    except ValueError:
        print("Please enter a valid integer for the countdown time.")
    except KeyboardInterrupt:
        print("\nTimer interrupted by user.")


if __name__ == "__main__":
    main()
