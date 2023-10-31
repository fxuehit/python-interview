#from lib import A, B
from lib.a import A
from lib.b import B

def main():
    a = A()
    b= B()
    a.hello()
    b.hello()


if __name__ == '__main__':
    main()
