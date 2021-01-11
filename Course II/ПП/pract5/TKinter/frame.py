# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

import sys

from .canvas import Canvas
from .control_objects import Button
from .control_objects import Input
from .control_objects import Label
from .input import InputAdapter
from .timers import destroy as destroy_timers


class Frame:
    def _create_root(self, title):
        root = tkinter.Tk()
        root.wm_title(title)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        return root

    def _canvas_init(self, width, height):
        canvas_frame = tkinter.Frame(self._root)
        self._canvas = Canvas(canvas_frame, width, height)
        canvas_frame.grid(row=0, column=0, rowspan=1, padx=0, pady=0,
                          sticky=(tkinter.N, tkinter.S, tkinter.W, tkinter.E))

    def _control_frame_init(self, width):
        self._control_frame = tkinter.Frame(self._root, width=width)

    def _input_init(self):
        status_frame = tkinter.Frame(self._root, width=0, height=0)
        canvas_widget = self._canvas._get_widget()
        self._input = InputAdapter(status_frame, self._root, canvas_widget)

    def __init__(self, title, canvas_width, canvas_height, control_width):
        self._root = self._create_root(title)

        self._canvas_frame = None
        self._canvas = None
        self._canvas_init(canvas_width, canvas_height)

        self._control_frame = None
        self._controls = []
        self._control_frame_init(control_width)

        self._input = None
        self._input_init()

    def _shutdown(self):
        destroy_timers()
        self._canvas.destroy()
        self._root.destroy()
        sys.exit(0)

    def start(self):
        try:
            self._root.mainloop()
        except KeyboardInterrupt:
            pass
        finally:
            self._shutdown()

    def set_draw_handler(self, draw_handler):
        self._canvas.set_draw_handler(draw_handler)

    def add_button(self, text, button_handler, width=None):
        button = Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)
        return button

    def add_label(self, text):
        label = Label(self._control_frame, text)
        self._controls.append(label)
        return label

    def add_input(self, text, input_handler, width):
        inp = Input(self._control_frame, text, input_handler, width)
        self._controls.append(inp)
        return inp

    def set_keydown_handler(self, key_handler):
        self._input.set_keydown_handler(key_handler)

    def set_keyup_handler(self, key_handler):
        self._input.set_keyup_handler(key_handler)

    def set_mouseclick_handler(self, mouse_handler):
        self._input.set_mouseclick_handler(mouse_handler)

    def set_mousedrag_handler(self, mouse_handler):
        self._input.set_mousedrag_handler(mouse_handler)

    def set_canvas_background(self, color):
        self._canvas.set_background(color)

    def get_canvas_textwidth(self, text, size, face='serif'):
        return self._canvas.get_textwidth(text, size, face)


def create_frame(title, canvas_width, canvas_height, control_width=200):
    return Frame(title, canvas_width, canvas_height, control_width)
