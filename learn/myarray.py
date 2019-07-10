class MyArray:
    def __IsNumber(self, n):
        if not isinstance(n,(int,float,complex)):
            return False
        return True

    def __init__(self,*args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print("all elements must be numbers")
                    return
            self.__value = list(args)

    def __del__(self):
        del self.__value

    def __add__(self,n):
        if self.__IsNumber(n):
            b = MyArray()
            b.__value = [item+n for item in self.__value]
            return b
        elif isinstance(n,MyArray):
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value=[i+j for i in zip(self.__value,n.__value)]
                return c
            else:
                print("length not equal")
        else:
            print("not supported!")
    def lenofArray(self):
        return len(self.__value)
    def PrintArray(self):
        for num in self.__value:
            print(num)
if __name__=="__main__":
    x = MyArray(1,2,3,4,5,6)
    print(x.lenofArray())
    y = MyArray(6,5,4,3,2,1)
    z = x + y
    z.PrintArray()