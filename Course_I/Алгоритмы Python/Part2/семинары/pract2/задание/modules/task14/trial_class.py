import datetime

from .software_class import SoftwareClass


class TrialClass(SoftwareClass):
    def __init__(self, name, manufacturer, install_date, days_trial):
        super().__init__(name, manufacturer)
        self.install_date = datetime.datetime.strptime(install_date, "%d.%m.%Y")
        self.days_trial = int(days_trial)

    def opportunity_detector(self):
        if self.install_date + datetime.timedelta(days=self.days_trial) >= self.date:
            return True
        return False

    def __days_calculation(self):
        days_left = (
            self.install_date + datetime.timedelta(days=self.days_trial) - self.date
        )
        return str(abs(days_left.days))

    def software_info(self):
        days_left_str = self.__days_calculation()
        install_date = self.install_date.strftime("%d.%m.%Y")
        if self.opportunity_detector() == True:
            status_msg = "Активировано, осталось " + days_left_str + " дня/дней"
        else:
            status_msg = (
                "Проблемы с активацией, просрочено на " + days_left_str + " дня/дней"
            )
        return (
            "[Условно бесплатное ПО]\nНазвание: "
            + self.name
            + "\nПроизводитель: "
            + self.manufacturer
            + "\nДата установки: "
            + install_date
            + "\nКоличество дней: "
            + str(self.days_trial)
            + "\nСтатус: "
            + status_msg
        )
