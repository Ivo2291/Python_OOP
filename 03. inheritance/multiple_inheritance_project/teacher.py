from employee import Employee
from person import Person


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."


new_teacher = Teacher()

print(new_teacher.teach())
print(new_teacher.sleep())
print(new_teacher.get_fired())
