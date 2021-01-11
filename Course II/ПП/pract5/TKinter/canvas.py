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

import time

from .constants import map_color


class Canvas:
    Fps = 60
    IntervalMs = int(1000 // Fps)
    MinRefreshMs = 1

    def _next_refresh(self):
        ms = int(round(time.time() * 1000))
        elapsed = ms - self._time
        self._time = ms

        if Canvas.IntervalMs < elapsed:
            return Canvas.MinRefreshMs

        return max(Canvas.IntervalMs - elapsed, Canvas.MinRefreshMs)

    def __init__(self, master, width, height):
        self._canvas = tkinter.Canvas(master, width=width, height=height, bd=2,
                                      bg='black', highlightthickness=0)
        self._canvas.pack(fill=tkinter.BOTH, expand=True)

        self._draw_handler_fn = None
        self._time = int(round(time.time() * 1000))
        self._draw_handler(master)

    def _get_widget(self):
        return self._canvas

    def _draw_handler(self, master):
        if self._draw_handler_fn is not None:
            self._canvas.delete(tkinter.ALL)
            self._draw_handler_fn(self)

        if self._draw_handler_fn is not None:
            self._canvas.update_idletasks()

        master.after(self._next_refresh(), self._draw_handler, master)

    def destroy(self):
        self._draw_handler_fn = None

    def set_background(self, color):
        self._canvas.config(background=map_color(color))

    def get_textwidth(self, text, size, face):
        return tkfont.Font(size=int(size), family=face).measure(text)

    def set_draw_handler(self, draw_handler):
        self._draw_handler_fn = draw_handler

    def draw_text(self, text, point, font_size, font_color, font_face='serif'):
        self._canvas.create_text(point, text=text, fill=map_color(font_color),
                                 anchor=tkinter.SW,
                                 font=(font_face, int(font_size)))

    def draw_line(self, point1, point2, line_width, line_color):
        self._canvas.create_line([point1[0], point1[1], point2[0], point2[1]],
                                 width=line_width, fill=map_color(line_color))

    def draw_polyline(self, point_list, line_width, line_color):
        for i in range(1, len(point_list)):
            self.draw_line(point_list[i - 1], point_list[i], line_width,
                           map_color(line_color))

    def draw_polygon(self, point_list, line_width, line_color,
                     fill_color=''):
        points = [y for x in point_list for y in x]
        self._canvas.create_polygon(points, width=line_width,
                                    fill=map_color(fill_color),
                                    outline=map_color(line_color))

    def draw_circle(self, center_point, radius, line_width, line_color,
                    fill_color=None):
        points = [(center_point[0] - radius), (center_point[1] - radius),
                  (center_point[0] + radius), (center_point[1] + radius)]
        self._canvas.create_oval(points, outline=map_color(line_color),
                                 fill=map_color(fill_color), width=line_width)

    def draw_point(self, point, color):
        self._canvas.create_line([point[0], point[1], point[0] + 1, point[1]],
                                 fill=map_color(color))

    def draw_image(self, image, center_source, width_height_source,
                   center_dest, width_height_dest, rotation=0):
        img = image._get_tkimage(center_source, width_height_source,
                                 width_height_dest, rotation)
        self._canvas.create_image(center_dest, image=img)
