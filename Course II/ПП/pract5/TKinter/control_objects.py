# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

try:
    import Tkinter as tkinter
    import tkFont as tkfont
except ImportError:
    import tkinter
    import tkinter.font as tkfont

_BaseString = ('This is a really boring basic string used for width '
               'calculations.')


class Widget:
    def __init__(self, widget, width):
        self._widget = widget
        if width is not None:
            font = tkfont.Font(font=widget.cget('font'))
            avg_char_width = int(font.measure(_BaseString) // len(_BaseString))
            self._widget.config(width=int(width // avg_char_width))

        self._widget.grid(column=0, sticky=tkinter.W)


class Button(Widget):
    def __init__(self, master, text, button_handler, width=None):
        button = tkinter.Button(master, text=text, command=button_handler)
        super(Button, self).__init__(button, width)
        self.set_text(text)

    def set_text(self, text):
        self._widget.config(text=text)


class Label(Widget):
    def __init__(self, master, text):
        label = tkinter.Label(master, text=text)
        super(Label, self).__init__(label, None)
        self._widget.config(wraplength=350, justify=tkinter.LEFT)

    def set_text(self, text):
        self._widget.config(text=text)


class Input(Widget):
    def __init__(self, master, text, input_handler, width):
        self._label = Label(master, text)
        self._content = tkinter.StringVar()
        entry = tkinter.Entry(master, textvariable=self._content)
        super(Input, self).__init__(entry, width)

        self._input_handler_fn = input_handler
        self._widget.bind('<Return>', self._input_handler)

    def _input_handler(self, _):
        if self._input_handler_fn is not None:
            self._input_handler_fn(self._content.get())

    def set_text(self, text):
        self._content.set(text)
