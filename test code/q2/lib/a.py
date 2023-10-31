#import lib.B

class A():
    def __init__(self) -> None:
        print("ojbect of class A is created")

    def hello(self):
        from lib.b import B
        print('hello, i am A')
        b = B()
