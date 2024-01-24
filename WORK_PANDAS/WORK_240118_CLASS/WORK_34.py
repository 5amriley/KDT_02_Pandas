# [Unit 34. 클래스 사용하기]

# DEBUG 불 리스트 초기화
DEBUG = [False for i in range(20)]

if DEBUG[0]:
    # 34.1.1 메서드 호출하기
    class Person:
        def greeting(self):
            print('Hello')

    james = Person()
    james.greeting()

if DEBUG[1]:
    # 34.1.3 인스턴스와 객체의 차이점
    # 참고) 메서드 안에서 메서드 호출하기
    class Person:
        def greeting(self):
            print('Hello')

        def hello(self):
            self.greeting()

    james = Person()
    james.hello()

if DEBUG[2]:
    # 34.1.3 인스턴스와 객체의 차이점
    # 참고) 특정 클래스의 인스턴스인지 확인하기
    class Person:
        pass
    james = Person()
    print(isinstance(james, Person))

if DEBUG[3]:
    # 34.2 속성 사용하기
    class Person:
        def __init__(self):
            self.hello = '안녕하세요.'

        def greeting(self):
            print(self.hello)


    james = Person()
    james.greeting()

if DEBUG[4]:
    class Person:
        def __init__(self, name, age, address):
            self.hello = '안녕하세요.'
            self.name = name
            self.age = age
            self.address = address

        def greeting(self):
            print(f'{self.hello} 저는 {self.name}입니다.')


    maria = Person('마리아', 20, '서울시 서초구 반포동')
    maria.greeting()

    print('이름:', maria.name)
    print('나이:', maria.age)
    print('주소:', maria.address)

if DEBUG[5]:
    # 34.3 비공개 속성 사용하기
    class Person:
        def __init__(self, name, age, address, wallet):
            self.name = name
            self.age = age
            self.address = address
            self.__wallet = wallet

        def pay(self, amount):
            self.__wallet -= amount
            print(f'이제 {self.__wallet}원 남았네요.')


    maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
    # maria.__wallet -= 10000   # 비공개 속성이라 클래스 바깥에서 접근 불가
    maria.pay(3000)

if DEBUG[6]:
    # 참고) 비공개 메서드 사용하기
    class Person:
        def __greeting(self):
            print('Hello')

        def hello(self):
            self.__greeting()

    james = Person()
    # james.__greeting()    # 에러 : 클래스 바깥에서는 비공개 메서드를 호출할 수 없음


if DEBUG[7]:
    # 34.5 연습문제
    class Knight:
        def __init__(self, health, mana, armor):
            self.health = health
            self.mana = mana
            self.armor = armor

        def slash(self):
            print('베기')


    x = Knight(health=542.4, mana=210.3, armor=38)
    print(x.health, x.mana, x.armor)
    x.slash()

if DEBUG[8]:
    # 34.6 심사문제: 게임 캐릭터 클래스 만들기
    class Annie:
        def __init__(self, health, mana, ability_power):
            self.health = health
            self.mana = mana
            self.ability_power = ability_power

        def tibbers(self):
            damage = self.ability_power * 0.65 + 400
            print(f'티버 : 피해량 {damage}')


    health, mana, ability_power = map(float, input().split())

    x = Annie(health=health, mana=mana, ability_power=ability_power)
    x.tibbers()
