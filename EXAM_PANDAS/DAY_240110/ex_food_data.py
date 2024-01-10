file = 'food.txt'

kor_food, china_food = [], []
kind = ''

# # 저장하는 방법 1
# with open(file, mode='r', encoding='utf8') as f:
#     data = f.readline()
#     if not data.index('*'):
#         kind = '한식' if data[1:] == '한식' else '중식'
#     else:
#         if kind == '한식': kor_food.append(data)
#         else:
#             china_food.append(data)

key = ''
# 저장하는 방법 2
with open(file, mode='r', encoding='utf8') as f:
    data = f.readline()
    if not data.find('*'):
        key = data[1:]
        foods[key] = []

data ={}
key = ''
for msg in datas:
    if not msg.find('*'):
        key=msg[1:]
        data[key]=[]
    else:
        print(data[key].append(msg[:-1]))
print()