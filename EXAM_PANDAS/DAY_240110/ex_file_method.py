# ------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# ------------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode='r', encoding='utf8') as f:
    f.seek(5)   # 파일 읽기 시작점 지정
    print(f.read(10))
    print(f'현재 위치 : {f.tell()}')
    f.seek(0)
    print(f'현재 위치 : {f.tell()}')

print(f.name, f.closed)
