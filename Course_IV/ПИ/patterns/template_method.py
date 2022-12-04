"""
Основное назначение паттерна Template Method:
• Определяет "скелет" алгоритма состоящий из примитивных операций
• В подклассах переопределяет детали алгоритма не меняя общей структуры
• Позволяет переиспользовать код
• Позволяет использовать общий интерфейс и реализацию
Основные абстракции Template Method
AbstractClass,
ConcreteClass,
Template Method,
Client:
• AbstractClass: Определяет интерфейс и шаги алгоритма
• ConcreteClass: Определяет частную специфическую реализацию
• template_method(): определяет алгоритм состоящий из шагов
"""


from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()

        self.compile_to_object()
        self.run()


class IosCompiler(Compiler):
    def collect_source(self):
        print("Collecting Swift Source Code")

    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


iOS = IosCompiler()
iOS.compile_and_run()