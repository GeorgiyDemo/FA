"""
Задача  9. Создайте класс ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ с методами, 
позволяющими вывести на экран информацию о программном обеспечении,
а также определить соответствие возможности использования (на текущую дату).

Создайте дочерние классы СВОБОДНОЕ (название, производитель),
УСЛОВНО БЕСПЛАТНОЕ (название, производитель, дата установки, срок бесплатного использования),
КОММЕРЧЕСКОЕ (название, производитель, дата установки, срок использования, цена) 

со своими методами вывода информации на экран и определения возможности использования на текущую дату.

Создайте список из п видов программного обеспечения, выведите полную информацию из базы на экран,
а также организуйте поиск программного обеспечения, которое допустимо использовать на текущую дату.
"""
import datetime

class SoftwareClass:
    """
    Класс ПО
    """
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.date = datetime.datetime.now()

    def software_info(self):
        return "[Родительский класс ПО]\nНазвание: "+self.name+"\nПроизводитель: "+self.manufacturer
    
    def opportunity_detector(self):
        #Его все равно переопределят
        ...

class FreewareClass(SoftwareClass):
    """
    Свободное ПО
    """
    def __init__(self, name, manufacturer):
        #Можно и через super, но в нашей жизни очень мало разнообразия
        self.name = name
        self.manufacturer = manufacturer
    
    def software_info(self):
        return "[Свободное ПО]\nНазвание: "+self.name+"\nПроизводитель: "+self.manufacturer

    def opportunity_detector(self):
        #Т.к. свободное ПО всегда можно использовать
        return True


class TrialClass(SoftwareClass):
    """
    Условно бесплатное ПО
    """
    def __init__(self, name, manufacturer, install_date, days_trial):
        super().__init__(name, manufacturer)
        self.install_date = datetime.datetime.strptime(install_date, "%d.%m.%Y")
        self.days_trial = int(days_trial)
    
    def opportunity_detector(self):
        #Если дата установки + кол-во дней тестирования >= текущей даты, то ок
        if self.install_date + datetime.timedelta(days=self.days_trial) >= self.date:
            return True
        return False
    
    def __days_calculation(self):
        days_left = self.install_date + datetime.timedelta(days=self.days_trial)-self.date
        return str(abs(days_left.days))
    
    def software_info(self):
        
        days_left_str = self.__days_calculation()
        install_date = self.install_date.strftime("%d.%m.%Y")

        if self.opportunity_detector() == True:
            status_msg = "Активировано, осталось "+days_left_str+" дня/дней"
        else:
            status_msg = "Проблемы с активацией, просрочено на "+days_left_str+" дня/дней"

        return "[Условно бесплатное ПО]\nНазвание: "+self.name+"\nПроизводитель: "+self.manufacturer+"\nДата установки: "+install_date+"\nКоличество дней: "+str(self.days_trial)+"\nСтатус: "+status_msg

class CommercialClass(SoftwareClass):
    """
    Коммерческое ПО
    """
    def __init__(self, name, manufacturer, install_date, days_pay):
        super().__init__(name, manufacturer)
        self.install_date = datetime.datetime.strptime(install_date, '%d.%m.%Y')
        self.days_pay = int(days_pay)
    
    def opportunity_detector(self):
        #Если дата установки + кол-во оплаченных дней >= текущей даты, то ок
        if self.install_date + datetime.timedelta(days=self.days_pay) >= self.date:
            return True
        return False

def main():
    obj = TrialClass("ПО","ПРОИХЗВОДИТЕЛЬ ПОО","06.05.2019",5)
    result = obj.software_info()
    print(result)

if __name__ == "__main__":
    main()