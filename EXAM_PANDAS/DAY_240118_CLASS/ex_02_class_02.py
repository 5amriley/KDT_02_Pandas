# ------------------------------------------------------------------------
# 자동차 클래스
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류(인스턴스속성), 제조사(클래스속성)
# 클래스 기능 : 주행한다, 정지한다, 후진한다
# ------------------------------------------------------------------------
class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메서드 => 객체(인스턴스) 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체(인스턴스) 메서드
    def driving(self, where):
        print(f'{where}으로 {self.number} 차가 주행하고 있다.')

    def stop(self, place):
        print(f'{self.number} 차가 {place}에 멈췄다.')

    def back(self):
        print(f'{self.number} 차가 후진한다.')

# ------------------------------------------------------------------------
# 자동차 인스턴스 생성
# ------------------------------------------------------------------------
myCar = Car(19, 'red', '1111', '세단')
secondCar = Car(20, 'pink', '7777', 'SUV')


# ------------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : Love
# 클래스 속성 : kind,
# 클래스 기능 : 새우까주기, 깻잎떼주기, 금융치료하기, 데려다주기, 데이트하기, 같이아프기,
#             대신죽어주기, 희생하기
# ------------------------------------------------------------------------

class Love:
    kind = None

    def shrimp(self):
        print('새우를 깐다.')

    def leaf(self):
        print('깻잎을 뗀다.')

    def flex(self, money):
        print(f'{money}원을 준다.')

    def getThere(self):
        print('데려다준다.')

    def date(self, place):
        print(f'{place}에서 데이트한다.')

    def sick_together(self):
        print('같이 아파한다.')

    def die_instead(self):
        print('대신 죽어준다.')

    def sacrifice(self):
        print('희생한다.')


# ------------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : Calc
# 클래스 속성 : 브랜드, 종류, 색상, 크기, 가격, 데이터
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 => 속성 또는 기능에서 매개변수
# ------------------------------------------------------------------------
class Calc:
    # 클래스 변수
    maker = '카시오'
    __size = (7, 15)  # 비공개 속성 __속성명 : 클래스 밖에서 속성을 읽기/쓰기 불가

    # 객체(인스턴스) 생성 메서드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.__info = info    # 인스턴스 생성 시 계산기에 각인되는 정보
        self.result = 0

    # 비공개 인스턴스 읽기/쓰기 메서드 (getter/setter)
    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info = info

    # 비공개 인스턴스 읽기/쓰기 메서드 (getter/setter) => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info = info

    # 덧셈 기능
    def plus(self, nums):
        self.result += nums

    def minus(self, nums):
        self.result -= nums

    def multi(self, nums):
        self.result *= nums

    def div(self, nums):
        if not nums:
            return '0으로 나눌 수 없습니다'
        self.result = self.result/nums

    def result(self):
        if True:
            if True:
                return self.__info



# ------------------------------------------------------------------------
# Calc 클래스로 인스턴스 생성 => 힙에 생성: 인스턴스 변수 + 클래스 변수
# ------------------------------------------------------------------------
c1 = Calc('공학용', '블랙', 10000, '홍길동계산기')

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
print(c1.result, c1.color)

# 인스턴스 속성 변경 => 공개 속성만 읽기 가능
c1.color = '빨강색'

# 인스턴스 비공개 속성 읽기 => 전용 메서드 getter/setter 통해서 읽기/쓰기
print(c1.getInfo(), c1.info)

# 인스턴스 비공개 속성 변경 => 전용 메서드 getter
c1.setInfo('내꺼')
c1.info = '내꺼야~~~'

# ------------------------------------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
# ------------------------------------------------------------------------
print(Calc.maker)
