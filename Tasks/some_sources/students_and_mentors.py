class Mentor:
    def __init__(self, name, surname, attached_courses):
        self.name = name
        self.surname = surname
        self.attached_courses = attached_courses

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nКурсы: {self.attached_courses}'

class Lecturer(Mentor):
    def __init__(self, name, surname, attached_courses):
        super().__init__(name, surname, attached_courses)
        self.grades = {}

        for course in self.attached_courses:
            self.grades[course] = []

    def get_avg_grade(self):
        total = 0
        grade_counter = 0
        avg = 0

        for course in self.grades:
            for grade in self.grades[course]:
                total += grade
                grade_counter += 1

        if grade_counter != 0:
            avg = total / grade_counter

        return avg

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__get_avg_grade()}'

    def __le__(self, other):
        if self.get_avg_grade() <= other.get_avg_grade():
            return True

    def __lt__(self, other):
        if self.get_avg_grade() < other.get_avg_grade():
            return True

    def __gt__(self, other):
        return not(self.__le__(other))

    def __ge__(self, other):
        return not(self.__lt__(other))

class Reviewer(Mentor):
    def __init__(self, name, surname, attached_courses):
        super().__init__(name, surname, attached_courses)

    def rate_student(self, student, course, grade):
        if ((course in student.courses_in_process)
                and (course in self.attached_courses)
                and (course in student.grades)):
            student.grades[course].append(grade)
            print('Студент оценен')
        else:
            print('Данный преподаватель не может оценить этого студента')

class Student:
    def __init__(self, name, surname):
        self.name    = name
        self.surname = surname
        self.grades  = {}
        self.courses_in_process = []
        self.finished_courses   = []

        for course in self.courses_in_process:
            self.grades[course] = []
        for course in self.finished_courses:
            self.grades[course] = []

    def rate_lecturer(self, lecturer, course, grade):
        if (course in lecturer.grades.keys()
                and course in self.courses_in_process):
            lecturer.grades[course].append(grade)
            print('Преподаватель оценен')
        else:
            print('Данный студент не может оценить этого лектора')

    def add_course_in_process(self, course):
        self.courses_in_process.append(course)

    def get_avg_grade(self):
        total = 0
        grade_counter = 0
        avg = 0
        for course in self.grades:
            for grade in self.grades[course]:
                total += grade
                grade_counter += 1
        if grade_counter != 0:
            avg = total / grade_counter
        return avg

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__get_avg_grade()}\nКурсы в процессе изучения: {self.courses_in_process}\nЗавершенные курсы: {self.finished_courses}'

    def __le__(self, other):
        if self.__get_avg_grade() <= other.__get_avg_grade():
            return True

    def __lt__(self, other):
        if self.__get_avg_grade() < other.__get_avg_grade():
            return True

    def __gt__(self, other):
        return not (self.__le__(other))

    def __ge__(self, other):
        return not (self.__lt__(other))

def get_avg_students_grade(students_list, course):
    total = 0
    grade_counter = 0
    avg = 0

    for student in students_list:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                total += grade
                grade_counter += 1

    if grade_counter != 0:
        avg = total / grade_counter

    return avg

def get_avg_lecturers_grade(lecturers_list, course):
    total         = 0
    grade_counter = 0
    avg           = 0

    for lecturer in lecturers_list:
        if course in lecturer.grades.keys():
            for grade in lecturer.grades[course]:
                total += grade
                grade_counter += 1

    if grade_counter != 0:
        avg = total / grade_counter

    return avg

ivan_student = Student('Иван', 'Иванов')
alexey_student = Student('Алексей', 'Алексеев')

andrey_lecturer = Lecturer('Андрей', 'Андреев',
                           ['Математический анализ', 'Линейная алгебра'])
vladislav_lecturer = Lecturer('Владислав', 'Петров',
                              ['Математический анализ', 'Информатика', 'Программирование'])

oleg_reviewer = Reviewer('Олег', 'Сидоров',
                         ['Математический анализ', 'Линейная алгебра'])
sergey_reviewer = Reviewer('Сергей', 'Козлов',
                           ['Информатика', 'Программирование'])

ivan_student.add_course_in_process('Информатика')
ivan_student.add_course_in_process('Математический анализ')
alexey_student.add_course_in_process('Математический анализ')

ivan_student.rate_lecturer(andrey_lecturer, 'Информатика', 5)
ivan_student.rate_lecturer(andrey_lecturer, 'Математический анализ', 5)

oleg_reviewer.rate_student(ivan_student, 'Информатика', 3)
oleg_reviewer.rate_student(ivan_student, 'Линейная алгебра', 3)
oleg_reviewer.rate_student(ivan_student, 'Математический анализ', 3)
oleg_reviewer.rate_student(alexey_student, 'Математический анализ', 5)

alexey_student.rate_lecturer(andrey_lecturer, 'Математический анализ', 2)
alexey_student.rate_lecturer(vladislav_lecturer, 'Математический анализ', 2)
ivan_student.rate_lecturer(vladislav_lecturer, 'Математический анализ', 5)

print(get_avg_students_grade([ivan_student, alexey_student],'Математический анализ'))
print(get_avg_lecturers_grade([andrey_lecturer, vladislav_lecturer], 'Математический анализ'))

print('')
print(andrey_lecturer)
print(ivan_student)

print('')
print(dir(Student))