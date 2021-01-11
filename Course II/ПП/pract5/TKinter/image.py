# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

import math

from PIL import Image as PILImage
from PIL import ImageTk


class Image:
    def __init__(self, path):
        self._image = PILImage.open(path)
        self._versions = {}

    def get_width(self):
        return self._image.size[0]

    def get_height(self):
        return self._image.size[1]

    def _get_tkimage(self, center, wh_src, wh_dst, rot):

        rot = -int(math.degrees(rot))
        version = ",".join([str(center), str(wh_src), str(wh_dst), str(rot)])
        if version not in self._versions:
            image = self._image
            crop = (
                int(center[0] - wh_src[0] // 2),
                int(center[1] - wh_src[1] // 2),
                int(center[0] + wh_src[0] // 2),
                int(center[1] + wh_src[1] // 2),
            )
            image = image.crop([int(x) for x in crop])
            if wh_src != wh_dst:
                image = image.resize(
                    [int(x) for x in wh_dst], resample=PILImage.BILINEAR
                )
            if rot != 0:
                image = image.rotate(rot, resample=PILImage.BICUBIC, expand=1)
            self._versions[version] = ImageTk.PhotoImage(image)
        return self._versions[version]


def load_image(path):
    return Image(path)


def get_width(image):
    return image.get_width()


def get_height(image):
    return image.get_height()
