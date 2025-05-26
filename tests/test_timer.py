from missiontimer.countdown_timer import CountdownTimer, TimerState
from unittest.mock import patch


def test_start_does_not_run_when_complete():
    timer = CountdownTimer(3)
    timer.state = TimerState.COMPLETE
    timer.start()
    assert timer.state == TimerState.COMPLETE


@patch("time.sleep", return_value=None)
def test_tick_only_runs_when_running(mock_sleep):
    timer = CountdownTimer(3)

    # Timer should do nothing if not started
    timer.tick()
    assert timer.remaining == 3  # No change

    # Set to RUNNING and tick
    timer.start()
    timer.tick()
    assert timer.remaining == 2


@patch("time.sleep", return_value=None)
def test_start_only_changes_state_when_idle_or_paused(mock_sleep):
    timer = CountdownTimer(1)
    timer.state = TimerState.COMPLETE  # Set invalid start state
    timer.start()
    assert timer.state == TimerState.COMPLETE  # Should not change
