import abc

class IConfigurable():
    def __init__(self):
        pass

    def speak(self):
        self.duck()

    @abc.abstractmethod
    def duck(self):
        pass


class A(IConfigurable):
    def __init__(self):
        self.name='duck1'

    def duck(self):
        print(self.name)

class B(IConfigurable):
    def __init__(self):
        self.name='duck2'

    def duck(self):
        print(self.name)

if __name__ == '__main__':
    A().speak()
    B().speak()

