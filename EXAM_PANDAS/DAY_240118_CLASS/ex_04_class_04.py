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

class AutoCar(Car):
    # 자율주행자동차
    auto_mode = False

    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)

    def auto_driving_on(self):
        self.auto_mode = True
        print('자율주행을 시작합니다.')

    def auto_driving_off(self):
        self.auto_mode = False
        print('자율주행이 종료되었습니다.')

c20 = AutoCar(20, 'yellow', '8888', '세단')

c20.driving('경북대학교')
c20.auto_driving_on()
c20.auto_driving_off()
c20.stop('경북대학교')

print('-----------------------------------------------------------')

class AutoFlyingCar(AutoCar):
    flying_mode = False

    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)

    def flying_on(self):
        self.flying_mode = True
        print('비행을 시작합니다. 이륙합니다.')

    def flying_off(self):
        self.flying_mode = False
        print('비행을 종료합니다. 착륙합니다.')

c30 = AutoFlyingCar(30, 'white', '9999', '세단')

c30.driving('경북대학교')
c30.auto_driving_on()
c30.flying_on()
c30.flying_off()
c30.auto_driving_off()
c30.stop('경북대학교')
