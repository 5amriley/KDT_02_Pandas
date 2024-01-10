# -------------------------------------------------------------------
# 파일 입출력 => 출력, 즉, 읽기 (Read)
# - 사용 내장함수 : open(file, mode='rt[기본]', encoding='시스템기본기')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야 한다.
# -------------------------------------------------------------------
# (1) open
file = open('message.txt', encoding='utf8')  # <class '_io.TextIOWrapper'> 객체 반환
print(f'file => {type(file)}, {file}')

# (2) IO => read() : 파일 안의 모든 내용 읽어오기
# fdata = file.read()
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기
# fdata = file.read(5)    # 5바이트만큼 문자 읽기
# print(f'fdata => {type(fdata)}, {fdata}')
#
# fdata = file.read(5)    # 5바이트만큼 문자 읽기
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => readline() : '\n' 기준으로 한 줄씩 읽어오기
datas = []
while True:
    fline = file.readline()     # 줄바꿈문자도 함께 읽어 온다.
    if not fline: break
    print(f'fline => {type(fline)}, {fline}', end='')
    datas.append(fline)     # fline[:-1] 을 저장하면 '\n'를 빼고 저장한다.
print(datas)

# (3) close
file.close()
