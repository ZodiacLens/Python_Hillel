class GroupOverflowError(Exception):
    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years, {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name}, "
                f"{self.age} years, {self.gender}, "
                f"record book №: {self.record_book}")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = {}

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError("Cannot add more than 10 students to the group")
        self.group[student.record_book] = student

    def delete_student(self, last_name):
        for record_book, student in list(self.group.items()):
            if student.last_name == last_name:
                del self.group[record_book]
                return student
        return None

    def find_student(self, last_name):
        for student in self.group.values():
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group.values())
        return f'Group Number: {self.number}\n{all_students}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False


if __name__ == "__main__":

    st1 = Student('Male', 95, 'Stan', 'Lee', 'AN1')
    gr = Group('AV1')
    gr.add_student(st1)

    try:
        gr.add_student(Student('Male', 35, 'Tony', 'Stark', 'AN2'))
        gr.add_student(Student('Female', 34, 'Natasha', 'Romanoff', 'AN3'))
        gr.add_student(Student('Male', 34, 'Steve', 'Rogers', 'AN4'))
        gr.add_student(Student('Male', 35, 'Bruce', 'Banner', 'AN5'))
        gr.add_student(Student('Male', 32, 'Thor', 'Odinson', 'AN6'))
        gr.add_student(Student('Male', 31, 'Clint', 'Barton', 'AN7'))
        gr.add_student(Student('Female', 28, 'Wanda', 'Maximoff', 'AN8'))
        gr.add_student(Student('Female', 27, 'Carol', 'Danvers', 'AN9'))
        gr.add_student(Student('Male', 24, 'Peter', 'Parker', 'AN10'))
        gr.add_student(Student('Male', 29, 'Clark', 'Kent', 'AN11'))


    except GroupOverflowError as e:
        print(f"Error: {e}")

    print(gr)

    assert gr.find_student('Lee') == st1
