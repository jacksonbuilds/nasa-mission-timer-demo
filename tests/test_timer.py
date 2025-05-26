from missiontimer.countdown_timer import CountdownTimer, TimerState

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

    # Start the timer
    timer.start()
    assert timer.state == TimerState.RUNNING

    # Advance one tick
    timer.tick()
    assert timer.remaining == 2

    # Pause it
    timer.pause()
    assert timer.state == TimerState.PAUSED

    # Resume and tick again
    timer.resume()
    assert timer.state == TimerState.RUNNING
    timer.tick()
    assert timer.remaining == 1
