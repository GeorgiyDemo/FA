"""
  пример из "реального мира" класс в котором организована проверка доступности серверов
  Можно создавать сколько угодно объектов данного класса в разных местах приложения - реально
  список серверов будет общим
"""


class HealthCheck:
    _instance = None
    _servers = []

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        pass

    def add_server(self, s):
        if self._servers.count(s) == 0:
            self._servers.append(s)

    def remove_server(self, s):
        if self._servers.count(s) == 1:
            self._servers.remove(s)

    @property
    def num_servers(self):
        return len(self._servers)

    @property
    def servers(self):
        return self._servers


hc1 = HealthCheck()  # Первый "экземпляр"
hc1.add_server("server1")
hc1.add_server("server2")
hc1.add_server("server3")
hc1.add_server("server3")  # пытаемся добавить дубли - не добавится


hc2 = HealthCheck()  # Второй "экземпляр"
hc2.add_server("server4")
hc2.add_server("server5")

print(hc1.servers)  # Мониторим одно и то же
print(hc2.servers)

hc1.remove_server("server3")  # удаляем из мониторинга существующий
hc1.remove_server("server7")

print(hc1)  # Убеждаемся что реально hc1 и hc2 - один объект
print(hc2)
