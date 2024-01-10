# --------------------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성하기
# - 예) message.txt => message_copy.txt
# --------------------------------------------------------

'''
# 원본 파일에 내용 읽은 후 저장
content = None
with open('message.txt', encoding='utf8') as f:
    content = f.read()

# f가 close() 된다고 해서 힙에서 즉시 f가 지워지는 것은 아니다.
# 파이썬 메모리 매니저가 프로그램 실행 중 적당한 시점에 한번에 처리된다.
print(type(f))

# 복사본 파일에 내용 쓰기
with open('message_copy.txt', mode='a', encoding='utf8') as f:
    f.write(content)
'''

# 원본 파일에 내용 읽은 후 저장
with open('message.txt', mode='r', encoding='utf8') as of:
    with open('message_copy.txt', mode='w', encoding='utf8') as nf:
        nf.write(of.read())
