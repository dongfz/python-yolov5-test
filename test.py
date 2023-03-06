
class Test:

    @staticmethod
    def newinstance(class_name, **kwargs):
        import importlib
        module = importlib.import_module('train')
        class_ = getattr(module, class_name)
        return class_(**kwargs)


if __name__ == '__main__':
    cls = Test.newinstance('Train1', test1='123')
    cls.test()



