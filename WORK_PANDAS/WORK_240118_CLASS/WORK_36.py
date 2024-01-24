# [Unit 36. 클래스 상속 사용하기]

# DEBUG 불 리스트 초기화
DEBUG = [False for i in range(20)]

if DEBUG[0]:
    # 36.1 사람 클래스로 학생 클래스 만들기
    class Person:
        def greeting(self):
            print('안녕하세요.')

    class Student(Person):
        def study(self):
            print('공부하기')

    james = Student()
    james.greeting()
    james.study()

if DEBUG[1]:
    # 36.2.2 포함 관계
    class Person:
        def greeting(self):
            print('안녕하세요.')

    class PersonList:
        # 상속을 사용하지 않고, 속성에 인스턴스를 넣어서 관리
        # PersonList가 Person을 포함하고 있다.
        # 이를 포함 관계. (PersonList has a Person)
        def __init__(self):
            self.person_list = []

        def append_person(self, person):
            # person으로 Person 객체를 받는다.
            self.person_list.append(person)

if DEBUG[2]:
    # 36.3 기반 클래스의 속성 사용하기
    class Person:
        def __init__(self):
            print('Person __init__')
            self.hello = '안녕하세요.'

    class Student(Person):
        def __init__(self):
            # Person __init__ 메서드 호출 안 함
            print('Student __init__')
            self.school = '파이썬 코딩 도장'

    james = Student()
    print(james.school)
    # print(james.hello)    # AttributeError: 'Student' object has no attribute 'hello'

if DEBUG[3]:
    # 36.3.1 super()로 기반 클래스 초기화하기
    class Person:
        def __init__(self):
            print('Person __init__')
            self.hello = '안녕하세요.'

    class Student(Person):
        def __init__(self):
            print('Student __init__')
            super().__init__()
            self.school = '파이썬 코딩 도장'

    james = Student()
    print(james.school)
    print(james.hello)

if DEBUG[4]:
    # 36.3.2 기반 클래스를 초기화하지 않아도 되는 경우
    class Person:
        def __init__(self):
            print('Person __init__')
            self.hello = '안녕하세요.'

    class Student(Person):
        pass

    james = Student()
    print(james.hello)

if DEBUG[5]:
    # 36.4 메서드 오버라이딩 사용하기
    class Person:
        def greeting(self):
            print('안녕하세요.')

    class Student(Person):
        def greeting(self):
            print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

    james = Student()
    james.greeting()

if DEBUG[6]:
    # 36.4 메서드 오버라이딩 사용하기
    class Person:
        def greeting(self):
            print('안녕하세요.')

    class Student(Person):
        def greeting(self):
            super().greeting()
            print('저는 파이썬 코딩 도장 학생입니다.')

    james = Student()
    james.greeting()
