for i in range(1, 6):
    print(i)

    num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(student_id, name, marks)
        self.students.append(student)
        print("Student added successfully!\n")

    def view_students(self):
        if not self.students:
            print("No students found.\n")
            return
        print("\nStudent List:")
        for student in self.students:
            student.display()
        print()

    def search_student(self):
        sid = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id == sid:
                print("Student found:")
                student.display()
                print()
                return
        print("Student not found.\n")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return
        print("Student not found.\n")

    def average_marks(self):
        if not self.students:
            print("No students available.\n")
            return
        total = sum(student.marks for student in self.students)
        avg = total / len(self.students)
        print(f"Average Marks: {avg:.2f}\n")


def main():
    manager = StudentManager()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Average Marks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.average_marks()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()