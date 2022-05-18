class Student:
    def __init__(self, name, surname, gender):

        self.grades = {}
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_student_marks(self):
        sum_ = 0
        len_sum_ = 0
        for i in self.grades:
            sum_ += sum(self.grades[i])
            len_sum_ += len(self.grades[i])
        return round(sum_ / len_sum_, 1)

    def rate_h(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self._average_student_marks()} \n' \
              f'Курсы в процессе изучение: {",".join(self.courses_in_progress)} \n' \
              f'Пройденные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        else:
            return self._average_student_marks() < other._average_student_marks()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_lecturer_marks(self):
        sum_ = 0
        len_sum_ = 0
        for i in self.grades:
            sum_ += sum(self.grades[i])
            len_sum_ += len(self.grades[i])
        return round(sum_ / len_sum_, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self._average_lecturer_marks()}'

        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        else:
            return self._average_lecturer_marks() < other._average_lecturer_marks()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} '
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

student2 = Student('Ruoy', 'Eman', 'your_gender')
student2.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(student2, 'Python', 9)
cool_mentor.rate_hw(student2, 'Python', 8)
cool_mentor.rate_hw(student2, 'Python', 6)

cool_reviewer = Reviewer('Semen', 'Andreev')

cool_student = Student('Ruo', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']

best_mentor = Lecturer('Roman', 'Petrov')
best_mentor.courses_attached += ['Python']
cool_student.rate_h(best_mentor, 'Python', 8)
cool_student.rate_h(best_mentor, 'Python', 9)
cool_student.rate_h(best_mentor, 'Python', 6)

cool_student = Student('Rul', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']

mentor2 = Lecturer('Roman', 'Petrov')
mentor2.courses_attached += ['Python']
cool_student.rate_h(mentor2, 'Python', 5)
cool_student.rate_h(mentor2, 'Python', 4)
cool_student.rate_h(mentor2, 'Python', 3)

print(best_mentor.grades)
print(student2.grades)
print(mentor2.grades)
print(best_student.grades)

print(cool_mentor)
print(cool_reviewer)
print(best_mentor)
print(best_student)
print(student2)
print(mentor2)

print(best_student > student2)
print(best_mentor < mentor2)
#
student_list = [best_student, student2]
mentor_list = [best_mentor, mentor2]


def average_marks_of_students(student_list, course_name):
    base = 0
    student_len = 0
    for student in student_list:
        if not isinstance(student, Student):
            print('Не студент')
            return
        else:
            for grade in student.grades:
                if grade == course_name:
                    for grade in student.grades:
                        base += sum(student.grades[grade])
                        student_len += len(student.grades[grade])
    print(round(base / student_len, 1))


def average_marks_of_lecturers(lector_list, course_name):
    base = 0
    lecturer_len = 0
    for lecturer in lector_list:
        if not isinstance(lecturer, Lecturer):
            print('Не студент')
            return
        else:
            for grade in lecturer.grades:
                if grade == course_name:
                    for grade in lecturer.grades:
                        base += sum(lecturer.grades[grade])
                        lecturer_len += len(lecturer.grades[grade])
    print(round(base / lecturer_len, 1))


average_marks_of_students(student_list, 'Python')
average_marks_of_lecturers(mentor_list, 'Python')
