import threading
from PIL import Image as PilImage
from PIL import ImageTk
import tkinter
import io
import math
from urllib.request import urlopen
import sys

class Image:
    def __init__(self, url):

        if url.startswith('http'):
            image = urlopen(url).read()
            self._image = PilImage.open(io.BytesIO(image)).convert('RGBA')
        else:
            self._image = PilImage.open(url,'rb').convert('RGBA')
        self._versions = {}

    def get_width(self):
        return self._image.size[0]

    def get_height(self):
        return self._image.size[1]

    def _get_tkimage(self, center, wh_src, wh_dst, rot):

        rot = -int(math.degrees(rot))
        version = ','.join([str(center), str(wh_src), str(wh_dst), str(rot)])
        if version not in self._versions:
            image = self._image
            crop = (int(center[0] - wh_src[0] // 2),
                    int(center[1] - wh_src[1] // 2),
                    int(center[0] + wh_src[0] // 2),
                    int(center[1] + wh_src[1] // 2))
            image = image.crop([int(x) for x in crop])
            if wh_src != wh_dst:
                image = image.resize([int(x) for x in wh_dst],
                                     resample=PilImage.BILINEAR)
            if rot != 0:
                image = image.rotate(rot, resample=PilImage.BICUBIC, expand=1)
            self._versions[version] = ImageTk.PhotoImage(image)
        return self._versions[version]


def load_image(URL):
    return Image(URL)


def get_width(image):
    return image.get_width()


def get_height(image):
    return image.get_height()



class Sound(object):
    def __init__(self, url):
        import pygame
        self._channel = None
        if url.startswith('http'):
            soundfile = urlopen(url).read()
            stream = io.BytesIO(soundfile).read()
            self._sound = pygame.mixer.Sound(stream)
        else:
            self._sound = pygame.mixer.Sound(url)
        self._paused = False

    def play(self):
        self._paused = False
        if self._channel is not None:
            if not self._channel.get_busy():
                self._channel.play(self._sound)
            elif self._paused:
                self._channel.unpause()
        else:
            self._channel = self._sound.play()

    def pause(self):
        if self._channel is not None:
            self._paused = True
            self._channel.pause()

    def rewind(self):
        if self._channel is not None:
            self._channel.stop()

    def set_volume(self, volume):
        self._sound.set_volume(volume)

_initialized = False


def sound_init():
    global _initialized
    import pygame
    pygame.mixer.init()
    _initialized = True


def load_sound(URL):
    global _next_channel
    if not _initialized:
        sound_init()

    return Sound(URL)


class Timer(object):
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

def destroy_timers():
    for timer in _timers:
        timer.stop()


def create_timer(interval, timer_handler):
    timer = Timer(interval, timer_handler)
    _timers.append(timer)
    return timer

class Frame:

    def __init__(self, title, canvas_width, canvas_height, control_width):
        self._root = self._create_root(title)

        self._canvas_frame = None
        self._canvas = None
        self._canvas_init(canvas_width, canvas_height)

        self._control_frame = None
        self._controls = []
        self._control_frame_init(control_width)

        self._input = None
        self._key_label = None
        self._mouse_label = None
        self._input_init()

    def _create_root(self, title):
        root = tkinter.Tk()
        root.wm_title(title)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        return root

    def _canvas_init(self, width, height):
        canvas_frame = tkinter.Frame(self._root)
        self._canvas = tkinter.Canvas(canvas_frame, width=width, height=height)
        canvas_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5,
                          sticky=(tkinter.N, tkinter.S, tkinter.W, tkinter.E))

    def _control_frame_init(self, width):
        self._control_frame = tkinter.Frame(self._root, width=width)
        self._control_frame.grid(row=0, column=0, padx=5, pady=5)

    def _input_init(self):
        status_frame = tkinter.Frame(self._root, width=120, height=85)
        status_frame.pack_propagate(0)
        canvas_widget = self._canvas._get_widget()
        self._input = tkinter.InputAdapter(status_frame, self._root, canvas_widget)
        status_frame.grid(row=1, column=0, sticky=(tkinter.W, tkinter.E),
                          padx=5, pady=5)

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
        button = tkinter.Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)
        return button

    def add_label(self, text):
        label = tkinter.Label(self._control_frame, text)
        self._controls.append(label)
        return label

    def add_input(self, text, input_handler, width):
        inp = tkinter.Input(self._control_frame, text, input_handler, width)
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

