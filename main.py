from utility import get_tution_fee

class Student:
    def __init__(self, n):
        self.n = n
    def tution_fees(self):
        return get_tution_fee(10)

s = Student("abc")
p = Student("Def")
q = Student("xyz")
x = Student("nahid")
