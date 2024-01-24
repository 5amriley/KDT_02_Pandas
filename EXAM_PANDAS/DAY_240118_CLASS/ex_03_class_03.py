# ------------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Point2D
# 클래스 속성 : x, y, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# ------------------------------------------------------------------------
class Point2D:
    # 클래스 속성 => 없음

    # 객체 생성
    def __init__(self, x, y, color, shape, size):
        print('Point2D')
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    # 객체 메서드
    def draw(self):
        print(f'좌표 : {self.x}, {self.y}에 {self.shape} 그리기')

    def printInfo(self):
        print('2D')
        print(f'위치 : {self.x}, {self.y}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')

# ------------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Point3D
# 클래스 속성 : x, y, z, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# ------------------------------------------------------------------------
class Point3D(Point2D):
    # 클래스 속성 => 없음

    # 객체 생성
    def __init__(self, x, y, z, color, shape, size):
        # 부모 객체 생성
        super().__init__(x, y, color, shape, size)
        print('Point3D')
        self.z = z

    # 상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩(overriding)
    def printInfo(self):
        print('3D')
        print(f'위치 : {self.x}, {self.y}, {self.z}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')


p3 = Point3D(5, 5, 5, 'yellow', 'rectangle', (3, 3, 3))
p3.printInfo()
