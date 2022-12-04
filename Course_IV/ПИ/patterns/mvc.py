"""
  Попытался сделать консольный MVC

  Три главные класса данного шаблона:
• Model: Определяет бизнес-логику или операции связанные с определенными задачами клиента
• View: Определяет представление для клиента. Модель предоставляет данные Представлению (view) на основе бизнес-логики.
• Controller: Интерфейс между моделью и представлением. При действиях клиента, контроллер передает запрос между
              представлением и моделью.
"""

class Model(object):
    def logic(self):
        data = 'Got it!'

        print("Model: Crunching data as per business logic")
        return data


class View(object):
    def update(self, data):
        print("View: Updating the view with results: ", data)


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: Relayed the Client asks")

        data = self.model.logic()
        self.view.update(data)


class Client(object):
    print("Client: asks for certain information")
    controller = Controller()
    controller.interface()