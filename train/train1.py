from train.base import BaseTrain


class Train1(BaseTrain):


    def __init__(self, test1: str) -> None:
        print("__init__")
        self.test1 = test1

    def test(self):
        print("Train1" + self.test1)

