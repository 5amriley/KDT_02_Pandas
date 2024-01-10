# ------------------------------------------------------------------------
# 파일 입출력 => 입력, 즉, 쓰기(write)
# - 사용 내장 함수 : open(file, mode='w', encoding='지정')
# ------------------------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 삭제
# file = open(filename, mode='w', encoding='utf-8')

# (1) open => 쓰기(a) 모드의 경우 파일이 없으면 생성, 있으면 파일 제일 마지막에 추가
file = open(existfile, mode='a', encoding='utf-8')


# (2) write
file.write('123456789\n')
file.write('''2024/01/10
수요일''')

file.writelines(['a\n', 'b\n', 'c\n', 'd\n', 'e\n'])



# (3) close
file.close()