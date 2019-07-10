class MyQuene:
    def __init__(self,size=10):
        self._content = []
        self._size = size
        self._current = 0

    def __del__(self):
        del self._content

    def setSize(self,size):
        if size < self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def put(self,v):
        if self._current == self._size:
            print("this is full")
        else:
            self._content.append(v)
            self._current = self._current + 1

    def get(self):
        if self._current==0:
            print("this is empty")
        else:
            self._content.pop(0)
            self._current = self._current - 1

    def show(self):
        if self._content:
            print(self._content)
        else:
            print("the quene is empty")

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        if self._current == 0:
            return True
        else:
            return False

    def ifFull(self):
        if self._current == self._size:
            return True
        else:
            return False

if __name__=="__main__":
    quene = MyQuene()
    for i in range(5):
        quene.put(i)

    quene.show()
    quene.put(9)
    quene.get()
    print(quene.ifFull())
    quene.show()