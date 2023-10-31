#import lib.A


class B():
    def __init__(self) -> None:
        print('object of class B is created')
    
    def hello(self):
        from lib.a import A
        print('hello this is B')
        a = A()