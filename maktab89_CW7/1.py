from random import randint
import shelve


class Employee:
    def __init__(self, name, famili, phone, email):
        self.name = name
        self.famili = famili
        self.phone = phone
        self.email = email


class Student(Employee):
    def __init__(self, name, famili, phone, email):
        self.sid = randint(1111, 9999)
        super().__init__(name, famili, phone, email)

    def __repr__(self):
        return f'id {self.sid}: {self.name} {self.famili}'


class Teacher(Employee):
    def __init__(self, name, famili, phone, email):
        self.tid = randint(1111, 9999)
        super().__init__(name, famili, phone, email)

    def __repr__(self):
        return f'id {self.tid}: {self.name} {self.famili}'


class Klas:
    def __init__(self, name, teacher, student_list):
        self.name = name
        self.teacher = teacher
        self.student_list = student_list
        self.kid = randint(1111, 9999)


class University():
    def __init__(self, name, city, ostan, kodposti, web, id):
        self.name = name
        self.city = city
        self.ostan = ostan
        self.kodposti = kodposti
        self.web = web
        self.id = id

    @staticmethod
    def register_class(klas):
        shelve_file = shelve.open('class_database')
        if not shelve_file.get(str(klas.kid)):
            shelve_file[str(klas.kid)] = {
                'klas': klas.name,
                'teacher': f'{klas.teacher.name} {klas.teacher.famili}',
                'students': klas.student_list
            }
            print(f'{klas.name} id: {klas.kid}')
            shelve_file.close()
        else:
            print(f'klas {klas.name} currently exist.')

    @staticmethod
    def register_teacher(teacher):
        shelve_file = shelve.open('teacher_database')
        if not shelve_file.get(f'{teacher.tid}'):
            shelve_file[f'{teacher.tid}'] = teacher
            shelve_file.close()
            print(f'{teacher.name} {teacher.famili} id: {teacher.tid}')
        else:
            print(f'teacher {teacher.name} {teacher.famili} currently exist')

    @staticmethod
    def register_student(student):
        shelve_file = shelve.open('student_database')
        if not shelve_file.get(f'{student.sid}'):
            shelve_file[f'{student.sid}'] = student
            shelve_file.close()
            print(f'{student.name} {student.famili} id: {student.sid}')
        else:
            print(f'student {student.name} currently exist')

    @staticmethod
    def get_teacher_by_id(id):
        shelve_file = shelve.open('teacher_database')
        data = shelve_file.get(str(id))
        shelve_file.close()
        if not data:
            print(f'teacher with id:{id} not found')
        else:
            print(data)
            return data

    @staticmethod
    def get_klas_by_id(id):
        shelve_file = shelve.open('class_database')
        data = shelve_file.get(str(id))
        shelve_file.close()
        if not data:
            print(f'klas with id:{id} not found')
        else:
            print(data)
            return data

    @staticmethod
    def get_student_by_id(id):
        shelve_file = shelve.open('student_database')
        data = shelve_file.get(str(id))
        shelve_file.close()
        if not data:
            print(f'student with id:{id} not found')
        else:
            print(data)
            return data

    @staticmethod
    def get_student_list():
        shelve_file = shelve.open('student_database')
        for item in shelve_file:
            print(shelve_file[item])
        shelve_file.close()

    @staticmethod
    def get_teacher_list():
        shelve_file = shelve.open('teacher_database')
        for item in shelve_file:
            print(shelve_file[item])
        shelve_file.close()

    @staticmethod
    def get_klas_list():
        shelve_file = shelve.open('class_database')
        for item in shelve_file:
            print(shelve_file[item])
        shelve_file.close()



# run program
if __name__ == '__main__':

    u = University('Maktab', 'Tehran', 'Tehran', '123456789', 'www.maktab', 123)

    teacher1 = Teacher('sina', 'mobarez', '09360000', 'email@mail.com',)
    teacher2 = Teacher('mohamad', 'rezai', '09221523', 'mohamad@mail.com',)

    student1 = Student('mojtaba', 'aminzadeh', '091123456', 'email@,com')
    student2 = Student('jafar', 'aminzadeh', '0935556', 'gmail@,com')
    student3 = Student('akbar', 'ahmadi', '091254556', 'email@gmail.com')
    student4 = Student('mostafa', 'asilian', '091254556', 'email@gmail.com')
    student5 = Student('mohamad', 'rabie', '091254556', 'email@gmail.com')

    k1 = Klas('python-django', teacher1, [student1, student2, student3])
    k2 = Klas('html', teacher2, [student1, student4, student5])



    """ Drive Code for make object and write to file"""
    # print("""\nremember id for "get_item_by_id(id)" method\n""")
    # print('=== register teacher ===')
    # u.register_teacher(teacher1)
    # u.register_teacher(teacher2)
    #
    # print('\n=== register klas ===')
    # u.register_class(k1)
    # u.register_class(k2)
    #
    # print('\n=== register student ===')
    # u.register_student(student1)
    # u.register_student(student2)
    # u.register_student(student3)
    # u.register_student(student4)
    # u.register_student(student5)



    """ test functionality """
    print("\n========== teachers by id ==========")
    u.get_teacher_by_id(5074)
    u.get_teacher_by_id(1234)

    print("\n========== klas by id ==========")
    u.get_klas_by_id(2851)
    u.get_klas_by_id(1234)

    print("\n========== student by id ==========")
    u.get_student_by_id(9837)
    u.get_student_by_id(1506)
    u.get_student_by_id(1234)

    print("\n========== all klas list ==========")
    u.get_klas_list()

    print("\n========== all teachers list ==========")
    u.get_teacher_list()

    print("\n========== all students list ==========")
    u.get_student_list()
