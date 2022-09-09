from csv import DictWriter
from typing import List, Dict, Type
import inspect


class Messages:
    messages_list = []

    def __init__(self, title, sender, receiver, message, time_stamp):
        print("------------------")
        self.title = title
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time_stamp = time_stamp
        Messages.messages_list.append(self)
        print("------------------")

    def display_content_message(self):
        print(
            f"Title of message : {self.title}\nSender name : {self.sender.fullname_email()}\nReceiver name : {self.receiver.fullname_email()}\nTime stamp : {self.time_stamp}\nContent message: {self.message}"
        )

    @classmethod
    def display_all_messages(cls):
        for message in cls.messages_list:
            print("------------------")
            message.display_content_message()
            print("------------------")

    @classmethod
    def find_messages_sent(cls, sender):
        print("==============")
        messages_returned = []
        for message in cls.messages_list:
            if message.sender.first == sender.first:
                messages_returned.append(message)
        return messages_returned


class Degree:
    def __init__(self, name: str, subjects: List, degree_leader, students: List):
        self.name = name
        self.subjects = subjects
        self.degree_leader = degree_leader
        self.students = students

    def add_degree_leader(self, teacher):
        self.degree_leader = teacher
        print(f"Degree leader for {self.name} updated.")

    def add_subjects(self, subjects):
        self.subjects = self.subjects + subjects
        print(f"Subjects for {self.name} updated.")

    def add_students(self, students: List):
        self.students = self.students + students
        print(f"Students enrolled on {self.name} updated.")


class Subject:
    def __init__(self, name: str, teachers, teaching_assistants: List, students: List):
        self.name = name
        self.teachers = teachers
        self.teaching_assistants = teaching_assistants
        self.students = students

    def add_teachers(self, teachers):
        if isinstance(teachers, list):
            self.teachers = self.teachers + teachers
        elif isinstance(teachers, Teacher):
            self.teachers.append(teachers)
        else:
            raise
        print(f"Teacher list for {self.name} updated.")

    def add_teaching_assistants(self, teaching_assistants):
        self.teaching_assistants = self.teaching_assistants + teaching_assistants
        print(f"Teaching assistant list for {self.name} updated.")

    def add_students(self, students: List):
        self.students += students
        print(f"Student list for {self.name} updated.")


class Person:
    def __init__(self, first: str, last: str, id: str):
        self.first = first
        self.last = last
        self.email = (first + "." + last).lower() + "@university.com"
        self.id = id

    # display name and email of person
    def fullname_email(self):
        return f"{self.first} {self.last} | {self.email}"

    def send_message(self, receiver):
        title = "Default title"
        message = "Default message"
        sender = self
        receiver = receiver
        time_stamp = "Default time_stamp"
        Messages(title, sender, receiver, message, time_stamp)
        print()
        print("Message sent.")


class Teacher(Person):
    def __init__(self, first: str, last: str, id: str):
        super().__init__(first=first, last=last, id=id)


class TeachingAssistant(Person):
    def __init__(self, first, last, id):
        super().__init__(first=first, last=last, id=id)


class Student(Person):
    def __init__(self, first, last, id):
        super().__init__(first=first, last=last, id=id)


def main():
    #######
    # Create playthings
    #####
    law = Degree("Law", [], "", [])
    physics = Degree("Physics", [], "", [])
    politics = Degree("Politics", [], "", [])
    computer_science = Degree("Computer Science", [], "", [])
    data_science = Degree("Data Science", [], "", [])

    economics = Subject("Economics", [], [], [])
    maths = Subject("Maths", [], [], [])
    criminal_law = Subject("Criminal Law", [], [], [])
    sociology = Subject("Sociology", [], [], [])
    statistics = Subject("Statistics", [], [], [])
    data_protection = Subject("Data  Protection", [], [], [])

    economics_teacher = Teacher("David", "Ricardo", "0020")
    maths_teacher = Teacher("Mary", "Boole", "0010")
    law_teacher = Teacher("Ruth", "Bader Ginsburg", "0030")

    law_teaching_assistant = TeachingAssistant("Michelle", "Obama", "0090")
    politics_teaching_assistant = TeachingAssistant("Sanna", "Marin", "0099")

    physics_student_0 = Student("Albert", "Einsten", "0001")
    physics_student_1 = Student("Marie", "Curie", "0011")
    physics_student_2 = Student("Lise", "Meitner", "0021")
    physics_student_3 = Student("Maria", "Goeppert-Mayer", "0031")
    physics_student_4 = Student("Ruby", "Payne-Scott", "0041")
    physics_student_5 = Student("Rosalind", "Franklin", "0051")

    computer_science_student_0 = Student("Ada", "Lovelace", "0002")
    computer_science_student_1 = Student("Hilary", "Mason", "0012")
    computer_science_student_2 = Student("Talia", "Gershon", "0022")
    computer_science_student_3 = Student("Janna", "Levin", "0032")
    computer_science_student_4 = Student("Bettina", "Warburg", "0042")

    data_science_student_0 = Student("Margaret", "Hamilton", "0006")
    data_science_student_1 = Student("Grace", "Hopper", "0016")
    data_science_student_2 = Student("Katherine", "Johnson", "0026")
    data_science_student_3 = Student("Adele", "Goldberg", "0036")

    law_student_0 = Student("Amal", "Clooney", "0003")
    law_student_1 = Student("Christine", "Lagarde", "0013")
    law_student_2 = Student("Gisele", "Halimi", "0023")

    politics_student_0 = Student("Angela", "Merkel", "0014")
    politics_student_1 = Student("Federica", "Mogherini", "0024")

    physics_teaching_assistant = TeachingAssistant("Stephen", "Hawking", "0002")

    #######
    # Who does what
    #####
    law.add_degree_leader(law_teacher)
    criminal_law.add_teachers(law_teacher)
    criminal_law.add_teaching_assistants(
        [law_teaching_assistant, politics_teaching_assistant]
    )

    # Create lists of students per degree (computer science, data science, law, physics, politics)
    ls_degrees = [computer_science, law, data_science, physics, politics]
    computer_science.add_students(
        [
            computer_science_student_0,
            computer_science_student_1,
            computer_science_student_2,
            computer_science_student_3,
            computer_science_student_4,
        ]
    )

    data_science.add_students(
        [
            data_science_student_0,
            data_science_student_1,
            data_science_student_2,
            data_science_student_3,
        ]
    )

    law.add_students([law_student_0, law_student_1, law_student_2])

    politics.add_students([politics_student_0, politics_student_1])

    physics.add_students(
        [
            physics_student_0,
            physics_student_1,
            physics_student_2,
            physics_student_3,
            physics_student_4,
            physics_student_5,
        ]
    )

    # Add students from different degrees to relevant subjects (computer science degree --> maths).
    # Degrees are law, physics, politics, computer science, data science
    # Subjects are economics, maths, criminal_law, sociology, statistics, data_protection

    ls_subjects = [
        economics,
        maths,
        criminal_law,
        sociology,
        statistics,
        data_protection,
    ]
    economics.add_students(law.students)
    economics.add_students(politics.students)

    maths.add_students(computer_science.students)
    maths.add_students(data_science.students)
    maths.add_students(physics.students)

    statistics.add_students(data_science.students)
    statistics.add_students(politics.students)
    statistics.add_students(physics.students)

    sociology.add_students(politics.students)
    sociology.add_students(law.students)

    criminal_law.add_students(politics.students)
    criminal_law.add_students(law.students)

    data_protection.add_students(data_science.students)
    data_protection.add_students(law.students)
    data_protection.add_students(computer_science.students)

    #######
    # Start printing
    #####

    for subject in ls_subjects:
        for student in subject.students:
            print(subject.name, " ", student.fullname_email())

    for degree in ls_degrees:
        for student in degree.students:
            print(degree.name, " ", student.fullname_email())

    physics_student_0.send_message(maths_teacher)
    physics_student_1.send_message(maths_teacher)
    # physics_student_1.send_message(economics_teacher)
    # physics_student_1.send_message(law_teacher)
    # physics_student_1.send_message(physics_student_0)

    # Messages.display_all_messages()

    x = Messages.find_messages_sent(physics_student_1)
    for message in x:
        Messages.display_content_message(message)

    y = Messages.find_messages_sent(physics_student_0)
    for message in y:
        Messages.display_content_message(message)

main()
