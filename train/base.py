from abc import ABCMeta, abstractmethod


class BaseTrain(metaclass=ABCMeta):

    @abstractmethod
    def test(self):
        pass
