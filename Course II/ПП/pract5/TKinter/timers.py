# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

import threading


class Timer:
    def __init__(self, interval, timer_handler):
        self._interval = interval
        self._timer = None
        self._timer_handler = timer_handler
        self._running = False

    def __repr__(self):
        s = ['Timer(', str(self._interval), ', ',
             repr(self._timer_handler), ')']
        if self._running:
            s += [': running']
        return ''.join(s)

    def _schedule(self):
        if self._running:
            interval = self._interval / 1000.0
            self._timer = threading.Timer(interval, self._handler)
            self._timer.start()

    def _handler(self):
        self._timer_handler()
        self._schedule()

    def start(self):
        self._running = True
        self._schedule()

    def stop(self):
        self._running = False
        if self._timer is not None:
            self._timer.cancel()

    def is_running(self):
        return self._running


_timers = []


def destroy():
    for timer in _timers:
        timer.stop()


def create_timer(interval, timer_handler):
    timer = Timer(interval, timer_handler)
    _timers.append(timer)
    return timer
