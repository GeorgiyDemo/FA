class TransportClass():
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def coords_detector(self, coord_list):
        y_list, x_list = coord_list
        y1, y2 = y_list
        x1, x2 = x_list
        locale_x, locale_y = self.coords
        if x1 < locale_x < x2 and y1 < locale_y < y2:
            return True
        return False

    def coords_formater_str(self):
        x, y = self.coords
        return "[" + str(x) + ", " + str(y) + "]"

    def info(self):
        return "[Родительский класс транспорт]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str()
