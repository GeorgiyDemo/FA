from .transport_class import TransportClass


class CarClass(TransportClass):
    def __init__(self, name, coords, number, year):
        super().__init__(name, coords)
        self.number = number
        self.year = year

    def info(self):
        return (
            "[Класс автомобиль]\nМодель: "
            + self.name
            + "\nКоординаты: "
            + self.coords_formater_str()
            + "\nНомер: "
            + str(self.number)
            + "\nГод выпуска: "
            + str(self.year)
        )
