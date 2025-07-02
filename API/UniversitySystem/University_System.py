class Person:
    def __init__(self, name, age):
        self._set_name(name)
        self._set_age(age)

    def _set_name(self, name):
        self.name = name

    def _set_age(self, age):
        self.age = age

    def display_info(self):
        details = f"Name: {self.name}, Age: {self.age}"
        print(details)


class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self._assign_id(student_id)

    def _assign_id(self, sid):
        self.student_id = sid

    def display_info(self):
        Person.display_info(self)
        print(f"Student ID: {self.student_id}")


class Lecturer(Person):
    def __init__(self, name, age, department):
        super(Lecturer, self).__init__(name, age)
        self.department = department

    def display_info(self):
        Person.display_info(self)
        print(f"Department: {self.department}")


class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        Person.display_info(self)
        print(f"Role: {self.role}")


# Example usage
def demo_display():
    print("=== Student ===")
    s = Student("Alice", 20, "S12345")
    s.display_info()

    print("\n=== Lecturer ===")
    l = Lecturer("Dr. John", 45, "Computer Science")
    l.display_info()

    print("\n=== Staff ===")
    st = Staff("Mr. Paul", 38, "Administrator")
    st.display_info()


# Run the display demo
demo_display()
