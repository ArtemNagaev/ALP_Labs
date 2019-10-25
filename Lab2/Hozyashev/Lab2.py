class Person(object):

    def __init__(self, fname, sname, age):
        """Constructor"""
        self.fname = fname
        self.sname = sname
        self.age = age

    def __repr__(self):
        return 'Person({}, {}, {})'.format(self.fname, self.sname, self.age)

    def __str__(self):
        return '{} {}, {} years old'.format(self.fname, self.sname, self.age)

class Student(Person):

    def __init__(self, fname, sname, age, gnumb, tnumb):
        Person.__init__(self, fname, sname, age)
        self.gnumb = gnumb
        self.tnumb = tnumb

    def __repr__(self):
        return 'Student({}, {}, {}, {}, {})'.format(self.fname, self.sname, self.age, self.gnumb, self.tnumb)

    def __str__(self):
        return '{} {}, {} years old student\nGroup: {}\nPhone number: {}'.format(self.fname, self.sname, self.age, self.gnumb, self.tnumb)

def test():
    student = Student('Юрий', 'Жмышко', 17, 'РИС-19-1б','8-800-555-35-35')
    print(student)
    student

if __name__ == "__main__":
    test()
