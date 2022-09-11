import json


class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()
    __person_type = 'Person'

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def set_person_type(self, person_type: str):
        self.__person_type = person_type

    def get_person_type(self):
        return self.__person_type

    def __str__(self):
        # Добавил наименования вводимых данных
        return f'Firstname: {self.__firstname} -- ' \
               f'Lastname: {self.__lastname} -- ' \
               f'Phone: {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(f'{self.__person_type}: {self.__str__()}\n')

    def from_file(filename: str):
        res = [line for line in open(filename, 'r')]
        # for i in res:
        #     print(i, end='')
        return res


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)
        super().set_person_type('Student')

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        # Добавил наименования вводимых данных
        return f'{super().__str__()} -- ' \
               f'Group: {self.__group}'

    def from_file(filename: str):
        # т.к. Person от Student отличается наличием группы =>
        # записываем из всего файла строки с наличием "Group:"
        # как вариант можно сделать в __str__ класса Student приписку что это студент
        # и список из файла составлять не по группе а по "Студенту"
        res = [line for line in open(filename, 'r') if 'Group:' in line]
        # for i in res:
        #     print(i, end='')
        return res


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)
        super().set_person_type('Teacher')

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} -- ' \
               f'Subject: {self.__subject}'

    def from_file(filename: str):
        # т.к. Person от Teacher отличается наличием Subject=>
        # записываем из всего файла строки с наличием "Subject:"
        # как вариант можно сделать в __str__ класса Teacher приписку что это учитель
        # и список из файла составлять не по предмету а по "Учителю"
        res = [line for line in open(filename, 'r') if 'Subject:' in line]
        # for i in res:
        #     print(i, end='')
        return res


li = []
# для удобства перепроверки все имена поменял на Student
li.append(Student('Anton', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Stepan', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Lidia', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Denis', 'Fedorov', '0991234756', 'C++17'))
# для удобства перепроверки все имена поменял на Teacher
li.append(Teacher('Petro', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Teacher('Georgii', 'Terkin', '+387415874165', 'Python21'))
li.append(Teacher('Tatianna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Teacher('Valentina', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Teacher('Sergey', 'Fedorov', '0991234756', 'C++17'))
# для удобства перепроверки все имена поменял на Person
li.append(Person('Fedor', 'Bulkin', 'trinolyatrulyalya'))
li.append(Person('Aleksey', 'Terkin', '+387415874165'))
li.append(Person('Aleksandra', 'Chechetkina', '+04478451235'))
li.append(Person('Maria', 'Bulkina', 'trinolyatrulyalya2'))
li.append(Person('Semen', 'Fedorov', '0991234756'))

print(li)
# Записываем все введеные данные из списка в файл
for i in li:
    print(i)
    i.to_file('test.txt')

# Можно ли создавать словарь при помощи vars? или это не верный подход?
# print(vars(Student('Anton', 'Bulkin', 'trinolyatrulyalya', 'Python11')))
# print(vars(Teacher('Sergey', 'Fedorov', '0991234756', 'C++17')))
# print(vars(Person('Maria', 'Bulkina', 'trinolyatrulyalya2')))

# получаем из файла список всех персон
# person_from_file = Person.from_file('test.txt')
# print(f'Все записи из файла:\n{person_from_file}')
# # получаем из файла только студентов
# student_from_file = Student.from_file('test.txt')
# print(f'Только студенты из файла:\n{student_from_file}')
# # получаем из файла только учителей
# teacher_from_file = Teacher.from_file('test.txt')
# print(f'Только учителя из файла:\n{teacher_from_file}')


# в виде функции работает, если делаю как на паре класс Group не выходит никак
def li_from_file(filename: str = 'test.txt'):
    li = []
    persons = [line.split() for line in open(filename, 'r')]
    for person in persons:
        if person[0] == 'Person:':
            li.append(Person(person[2], person[5], person[8]))
        if person[0] == 'Student:':
            li.append(Student(person[2], person[5], person[8], person[11]))
        if person[0] == 'Teacher:':
            li.append(Teacher(person[2], person[5], person[8], person[11]))
    return li


# создаем список объектов
li = li_from_file('test.txt')
# print(li)
for i in li:
    print(i)


def dic_from_file(filename: str = 'test.txt'):
    dic = {}
    persons = [line.split() for line in open(filename, 'r')]
    i = 1
    for person in persons:
        if person[0] == 'Person:':
            dic[f'Person: {i}'] = {
                    'Firstname': person[2],
                    'Lastname': person[5],
                    'Phone': person[8],
                }
            i += 1
    i = 1
    for person in persons:
        if person[0] == 'Student:':
            dic[f'Student {i}'] = {
                    'Firstname': person[2],
                    'Lastname': person[5],
                    'Phone': person[8],
                    'Group': person[11],
                }
        i += 1
    i = 1
    for person in persons:
        if person[0] == 'Teacher:':
            dic[f'Teacher {i}'] = {
                    'Firstname': person[2],
                    'Lastname': person[5],
                    'Phone': person[8],
                    'Subject': person[11],
                }
            i += 1
    return dic


# словарь из файла
dict = dic_from_file('test.txt')
print(dict)
# for i in dict:
#     print(i)


# сериализируем полученный словарь и записываем в файл
with open('serialize.txt', 'w') as file:
    json.dump(dict, file, indent=2)

# десериализируем словарь
with open('serialize.txt', 'r') as file:
    dict_deserialize = json.load(file)

print(dict_deserialize)

