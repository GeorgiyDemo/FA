from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
         self.__latestNews = news

    def get_news(self):
        return "Got News:", self.__latestNews



class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher

        self.publisher.attach(self)


    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


news_publisher = NewsPublisher()

for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
    Subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers())

news_publisher.add_news('Hello World!')
news_publisher.notify()

print("\nDetached:", type(news_publisher.detach()).__name__)
print("\nSubscribers:", news_publisher.subscribers())

news_publisher.add_news('My second news!')
news_publisher.notify()
