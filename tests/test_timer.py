from missiontimer.countdown_timer import CountdownTimer, TimerState
from unittest.mock import patch

def test_timer_initialization():
    timer = CountdownTimer(10)
    assert timer.remaining == 10
    assert timer.state == TimerState.IDLE

@patch('time.sleep', return_value=None)
def test_pause_resume_transitions(mock_sleep):
    timer = CountdownTimer(3)

    # Start the timer
    timer.start()
    assert timer.state == TimerState.RUNNING

    # Advance one tick
    timer.tick()
    assert timer.remaining == 2
