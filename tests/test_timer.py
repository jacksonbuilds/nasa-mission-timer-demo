from src.countdown_timer import CountdownTimer, TimerState

def test_timer_initialization():
    timer = CountdownTimer(10)
    assert timer.remaining == 10
    assert timer.state == TimerState.IDLE

def test_reset_functionality():
    timer = CountdownTimer(5)
    timer.remaining = 1
    timer.reset()
    assert timer.remaining == 5
    assert timer.state == TimerState.IDLE

def test_pause_resume_transitions():
    timer = CountdownTimer(3)
    timer.pause()
    assert timer.state == TimerState.IDLE  # cannot pause before start
    timer.start()
    timer.pause()
    assert timer.state == TimerState.PAUSED
    timer.resume()
    assert timer.state == TimerState.RUNNING
