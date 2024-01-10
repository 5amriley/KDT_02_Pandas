# -----------------------------------------------------------------
# 입력받은 내용을 파일에 저장하는 프로그램
# - 조건 : 'X', 'x' 입력 시 입력받기 중단
# -----------------------------------------------------------------
# 모듈 로딩 --------------------------------------------------------
import time
from datetime import date, datetime

# print(time.time())
# print(time.ctime(time.time()))  # ctime : converts time(secs)

# td = date.today()
# print(td.year, td.month, td.day)
# print(td)
# print(td.strftime("%y/%m/%d"))
#
# td2 = datetime.today()
# print(td2.year, td2.month, td2.day, td2.hour, td2.minute, td2.second)

# 관련 변수 --------------------------------------------------------
filename = 'test.txt'

# 프로그램 기능 구현 부분
with open(filename, mode='a', encoding='utf8') as f :
    while True:
        # 종료 검사
        data = input("메시지 입력 (종료: X, x) : ")

        if data in ('X', 'x'):
            print('종료합니다.')
            break

        # 파일에 쓰기, 즉, 저장
        f.write(data + '\n')

        # 일정 시간 일시정지 후 반복
        time.sleep(1)
    # 입력 종료 시간 파일에 기록
    today = date.today()
    f.write(f'저장 시간 : {today.strftime("%y/%m/%d")}\n')
