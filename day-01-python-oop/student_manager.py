class Student:

    def __init__(self, Id, Name, Age, Marks):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.Marks = Marks
        self.average = 0

    def get_average(self):
        self.average = self.Marks / 5
        return self.average

    def is_passed(self):
        self.average = self.get_average()
        if self.average >= 50:
            return True
        return False

    def update_marks(self, marks):
        if 0 <= marks <= 500:
            self.Marks = marks
        else:
            print("Invalid input")

    def display(self):
        print("Student Details")
        print(f"Id: {self.Id}")
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Marks: {self.Marks}")


def topper(students):
    maxi = float('-inf')
    rno = 0

    for student in students:
        if student.Marks > maxi:
            maxi = student.Marks
            rno = student

    return rno


def find_student(students, ids):
    for student in students:
        if student.Id == ids:
            return student

    return None


def update_marks(students, ids, marks):
    for student in students:
        if student.Id == ids:
            student.update_marks(marks)
            return

    print("Student Not found")


def delete(students, ids):
    for student in students:
        if student.Id == ids:
            students.remove(student)
            print("Student removed successfully")
            return

    print("Student Not Found")


def add_students(students):
    try:
        Id = int(input("Enter User Id: "))
        Name = input("Enter the user name: ")
        Age = int(input("Enter the age: "))
        Marks = int(input("Enter the marks: "))

        exists = find_student(students, Id)

        if exists is None:
            if 0 <= Marks <= 500:
                s = Student(Id, Name, Age, Marks)
                students.append(s)
                print("Student added successfully")
            else:
                print("Invalid mark input")
        else:
            print("Student Already Exists")
    except ValueError:
        print("Invalid Input")


def display_students(students):

    ids = int(input("Enter student id to display details: "))

    student = find_student(students, ids)

    if student is not None:
        student.display()
    else:
        print("Invalid student id")


students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Find Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Exit")
    try:
        choice = int(input("\nEnter Choice: "))
    
    
        if choice == 1:
            add_students(students)

        elif choice == 2:
            display_students(students)

        elif choice == 3:
            ids = int(input("Enter student id: "))

            s1 = find_student(students, ids)

            if s1 is not None:
                print("\nStudent:")
                print(f"Name: {s1.Name}")
                print(f"Marks: {s1.Marks}")
            else:
                print("Student Not Found")

        elif choice == 4:
            try:
                ids = int(input("Enter Student id: "))
                mark = int(input("Enter mark: "))

                update_marks(students, ids, mark)
            except ValueError:
                print("Invalid Input")

        elif choice == 5:
            ids = int(input("Enter student id: "))

            delete(students, ids)

        elif choice == 6:

            if len(students) == 0:
                print("No students available")
            else:
                s1 = topper(students)

                print("\nTopper:")
                print(f"Name: {s1.Name}")
                print(f"Marks: {s1.Marks}")

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice")
    except ValueError:
            print("Invalid Input")