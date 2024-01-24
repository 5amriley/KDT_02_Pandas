# [Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기]

# DEBUG 불 리스트 초기화
DEBUG = [False for i in range(20)]

if DEBUG[0]:
    # 35.1.1 클래스 속성 사용하기
    class Person:
        bag = []

        def put_bag(self, stuff):
            self.bag.append(stuff)


    james = Person()
    james.put_bag('책')

    maria = Person()
    maria.put_bag('열쇠')

    print(james.bag)
    print(maria.bag)


if DEBUG[1]:
    # 35.1.2 인스턴스 속성 사용하기
    class Person:
        def __init__(self):
            self.bag = []

        def put_bag(self, stuff):
            self.bag.append(stuff)


    james = Person()
    james.put_bag('책')

    maria = Person()
    maria.put_bag('열쇠')

    print(james.bag)
    print(maria.bag)

if DEBUG[2]:
    # 35.2 정적 메서드 사용하기
    class Calc:
        @staticmethod
        def add(a, b):
            print(a + b)

        @staticmethod
        def mul(a, b):
            print(a * b)


    Calc.add(10, 20)
    Calc.mul(10, 20)

if DEBUG[3]:
    # 35.3 클래스 메서드 사용하기
    class Person:
        count = 0

        def __init__(self):
            Person.count += 1

        @classmethod
        def print_count(cls):
            print(f'{cls.count}명 생성되었습니다.')


    james = Person()
    maria = Person()

    Person.print_count()

if DEBUG[4]:
    # 35.5 연습문제 : 날짜 클래스 만들기
    class Date:
        @staticmethod
        def is_date_valid(date_string):
            year, month, day = map(int, date_string.split('-'))
            return (1 <= month <= 12) and (1 <= day <= 31)


    if Date.is_date_valid('2000-12-31'):
        print('올바른 날짜 형식입니다.')
    else:
        print('잘못된 날짜 형식입니다.')

# 35.6 심사문제 : 시간 클래스 만들기
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def from_string(original_string):
        h, m, s = map(int, original_string.split(':'))
        return Time(h, m, s)

    @staticmethod
    def is_time_valid(time_string):
        h, m, s = map(int, time_string.split(':'))
        return (0 <= h <= 23) and (0 <= m <= 59) and (0 <= s <= 60)

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
