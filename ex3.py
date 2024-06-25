class A:
    def __init__(self, num):
        self.num = num

    def show(self):
        print(self.num)

class B(A):
    def show(self):
        print(self.num*self.num)

ins_B = B(3)
ins_B.show()