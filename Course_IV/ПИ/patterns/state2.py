class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Состояние:', self, ' => переключаем в', state.name)

            self.__class__ = state
        else:
            print('Состояние:', self, ' => переключить в', state.name, 'невозможно.')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']


class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model

        self.state = Off()

    def change(self, state):
        self.state.switch(state)


comp = Computer()
# Включаем
comp.change(On)
# Выключаем
comp.change(Off)

# Снова включаем
comp.change(On)
# Декативация
comp.change(Suspend)
# Пытаемся в гибернацию - не получается!
comp.change(Hibernate)
# включаем снова
comp.change(On)
# выключаем
comp.change(Off)