from user_module import UserAnalyserClass

#TODO
class ComputerAnalyserClass(UserAnalyserClass):
    """Класс ограничений и выявление некорректного хода со стороны компьютера"""
    pass


#TODO
class ComputerGameClass:
    def __init__(self, board, user_color):
        #Используется для контроля тупикового хода со стороны компьютера
        self.result = False
        self.board = board
        self.user_color = user_color
        """Класс с основной логикой автоматического хода компьютера"""
        pass
