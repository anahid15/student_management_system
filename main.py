from utility import get_tution_fee

class Student:
    def __init__(self, name, marks=0):
        """
        Initialize a Student object.
        
        Args:
            name (str): The name of the student.
            marks (float): The student's total marks (default is 0).
        """
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade(marks)
    
    def get_tuition_fee(self):
        """
        Retrieve the tuition fee using the utility function.
        
        Returns:
            float: Tuition fee for the student.
        """
        return get_tution_fee(10)  # Example: fixed value, can be dynamic later
    
    def calculate_grade(self, marks):
        """
        Calculate the student's grade based on their marks.
        
        Args:
            marks (float): The student's marks (0–100).
        
        Returns:
            str: The letter grade.
        """
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"


if __name__ == "__main__":
    student1 = Student("Nahid", 88)
    student2 = Student("Ayesha", 74)
    student3 = Student("Kamal", 59)

    print(f"{student1.name} got grade {student1.grade}")
    print(f"{student2.name} got grade {student2.grade}")
    print(f"{student3.name} got grade {student3.grade}")

    # Tuition fee example
    print(f"Tuition Fee for {student1.name}: {student1.get_tuition_fee()}")
