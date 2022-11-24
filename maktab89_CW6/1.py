class Student:
    pass


class Mark:
    pass


s1 = Student()

m1 = Mark()

print(type(s1))
print(type(m1))

print(isinstance(s1, Student))
print(isinstance(s1, Mark))
print(isinstance(s1, object))
print(Mark.__mro__)
