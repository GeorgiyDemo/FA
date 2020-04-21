class ObjectKilledClass:
    """
    Класс Объекты поражения (название, тип)
    Как я понял, используются в PlaneClass.murder_opportunity
    Тип: наземный, летательный
    """

    def __init__(self, name, type_):
        self.name = name
        self.type = type_

    def info(self):
        """Вывод информации об объекте."""

        d_formater = {}
        d_formater["Имя"] = self.name
        d_formater["Тип"] = self.type

        out_str = "*Общая информация об объекте поражения*\n"
        out_str += "\n".join(list([str(k) + ": " + str(v) for k, v in d_formater.items()]))
        print(out_str)
