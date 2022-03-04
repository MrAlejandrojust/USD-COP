import datetime
import sched
import time
import threading


def repeat_at_interval(scheduler, event, interval=60, add_n=10, start_t=None):
    """Adds 'add_n' more calls to "event" at each "interval" seconds"""
    # Unix timestamp
    if start_t is None:
        t = time.time()
        # round to next interval -
        t = t - (t % interval) + interval
    else:
        t = start_t

    for i in range(add_n):
        scheduler.enterabs(t, 0, event)
        t += interval

    # Schedule call to self, to add "add_n" extra events
    # when these are over:
    scheduler.enterabs(t - interval, 0, repeat_at_interval, kwargs={
        "scheduler": scheduler,
        "event": event,
        "interval": interval,
        "add_n": add_n,
        "start_t": t
    })


def test():
    print(datetime.datetime.now())
