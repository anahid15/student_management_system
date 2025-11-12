from utility import get_tution_fee

class Student:
    def __init__(self, marks: int) -> None:
        self.marks = marks

    def tution_fees(self):
        return get_tution_fee(10)

student1 = Student("abc")
student2 = Student("Def")
student3 = Student("xyz")
student4 = Student("nahid")
