from models import ImageInfo
import TKinter as tkinter


class ImageStorage:

    """Хранение информации об изображении и самого изображения"""

    def __init__(self, image_info, image):

        if not isinstance(image_info, ImageInfo):
            raise ValueError("Нужен экземпляр ImageInfo!")
        if not isinstance(image, tkinter.image.Image):
            raise ValueError("Нужен экземпляр tkinter.image для изображения!")

        self._image_info = image_info
        self._image = image

    @property
    def image(self):
        return self._image

    @property
    def info(self):
        return self._image_info
