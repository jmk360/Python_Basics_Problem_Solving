# 파이썬 반복문과 리스트

# Exercise 31. 반복문
# 1 ~ 10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하세요.

# sol)
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)

# Exercise 32. 반복문
# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단을 출력하세요.

# sol)
# a = int(input(">> "))

# for i in range(1, 10):
#     print(f"{a} * {i} = {a * i}")

# Exercise 33. 반복문과 문자열 다루기 (split)
# 사용자로부터 , 로 구분된 여러 이름을 입력받아서, 한 줄에 하나씩 이름을 출력하세요
# 사용자 입력: Dave,David,Andy,Arthor
# 출력 예:
# Dave
# David
# Andy
# Arthor

# sol)
# strinput = input(">> ")
# for name in strinput.split(','):
#     print(name)

# Exercise 34. 반복문과 문자열 다루기 (split)
# 사용자로부터 [이름1],[이름2],[이름3] 과 같은 형식으로 데이터를 입력받아서, 한 줄에 하나씩 이름을 출력하세요
# 사용자 입력: [Dave],[David],[Andy],[Arthor]
# 출력 예:
# Dave
# David
# Andy
# Arthor

# sol1)
# strinput = input(">> ")
# list_input = strinput.split(',')
# for name in list_input:
#     print(name[1:-1])

# sol2)
# strinput = input(">> ")
# list_input = strinput.split(',')
# for name in list_input:
#     print(name.strip('[]')) # 문자열 좌우에 '[' 나 ']' 이놈이 있으면 없애버린다.

# Exercise 35. 반복문과 조건문
# 1부터 30까지의 숫자 중 3의 배수만 출력하세요.

# sol1)
# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)

# sol2)
# a = [n for n in range(1, 31) if n % 3 == 0]
# print(a)

# Exercise 36. 반복문 (while)
# 1부터 100까지 숫자를 모두 더한 값을 출력하세요.
# 단 while 구문을 사용해서 작성하세요.

# sol1)
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# sol2)
# print(sum(range(1, 101)))

# Exercise 37. 반복문 (while)
# 사용자로부터 4자리의 숫자로 구성된 데이터를 입력받아서
# 비밀번호와 같으면 '비밀번호가 맞습니다.'를 출력하고 종료하세요.
# 비밀번호와 다르면 '비밀번호가 틀렸습니다.'를 출력하고 다시 사용자로부터 데이터를 입력받으세요.
# 비밀번호는 4312 입니다.

# sol)
# pw = 4312
# num = int(input(">> "))
# while num != pw:
#     print("비밀번호가 틀렸습니다.")
#     num = int(input(">> "))
# print("비밀번호가 맞습니다.")

# Exercise 38. 데이터 구조와 반복문 (리스트)
# 다음 리스트 변수에서 음수 데이터를 삭제하고, 양수만 가진 리스트 변수로 만들고, 해당 변수를 출력하세요.
# num_list = [0, -11, 31, 22, -11, 33, -44, -55]

# sol1)
# num_list = [0, -11, 31, 22, -11, 33, -44, -55]
# result = [num for num in num_list if num >= 0]
# print(result)

# sol2)
# num_list = [0, -11, 31, 22, -11, 33, -44, -55]
# result = []
# for num in num_list:
#     if num >= 0:
#         result.append(num)
# print(result)

# Exercise 39. 데이터 구조와 반복문 (리스트)
# 다음 리스트에 있는 데이터의 길이를 한 라인에 하나씩 출력하세요.
# list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]

# sol1)
# list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
# result = [len(x) for x in list_data]
# print(result)

# sol2)
# list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
# for word in list_data:
#     print(len(word), end=', ')
# print('\b\b ')

# Exercise 40. 데이터 구조와 반복문 (리스트)
# 다음 리스트에 있는 숫자를 역 방향으로 출력하세요.
# 단, 리스트에 있는 숫자들은 한 라인에 하나씩 출력하세요.
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sol1)
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(reversed(data)))

# sol2)
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(data[::-1])

# sol3)
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data.reverse()
# print(data)

# Exercise 41. 데이터 구조 (리스트), 반복문, 문자열 다루기
# 다음과 같이 파일 이름(확장자 포함) 저장하고 있는 리스트가 있을 때 확장자를 제거하고 파일 이름만 출력하세요.
# filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']

# sol)
# filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
# file_name_list = [file_name.split('.')[0] for file_name in filelist]
# print(file_name_list)

# Exercise 42. 데이터 구조 (리스트), 반복문, 조건문, 문자열 다루기
# 파일 이름이 다음과 같은 리스트에 저장되어 있을 때 확장자가 .txt 인 파일에 대한 리스트를 출력하라
# filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']

# sol)
# filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']
# file_name_list = [file_name for file_name in filelist if file_name.endswith(".txt")]
# print(file_name_list)

# Exercise 43. 문자열 다루기와 조건문
# prices 변수에 입력된 값을 원 화로 바꿔서 계산하세요.
# prices = '100 달러'
# 환율은 다음과 같음
# 통화단위	원화 환율
# 달러	1112
# 출력:
# 111200 원

# sol)
# prices = input(">> ")
# data = int(prices.split()[0])
# print(f"{data * 1112} 원")

# Exercise 44. 문자열 다루기와 조건문
# 사용자로부터 달러 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
# 사용자는 100 달러, 100 위안 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
# 각 통화별 환율은 다음과 같습니다.
# 통화단위	원화 환율
# 달러	1112
# 위안	171
# 출력:
# 111200 원

# sol)
# strinput = input(">> ")
# data, type = strinput.split()
# if type == "달러":
#     print(f"{int(data) * 1112} 원")
# elif type == "위안":
#     print(f"{int(data) * 171} 원")
# else:
#     print("잘못 입력")

# Exercise 45. 문자열 다루기, 조건문, 데이터 구조 (dictionary)
# 다음 통화별 환율을 통화단위와 원화 환율을 가진 딕셔너리로 만들고 사용자로부터 달러, 엔, 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
# 사용자는 100 달러, 100 위안 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
# 통화단위	원화 환율
# 달러	1112
# 위안	171
# 엔	1010

# sol)
# a = {"달러": 1112, "위안": 171, "엔": 1010}

# strinput = input(">> ")
# tmp = strinput.split()
# data = int(tmp[0])
# unit = tmp[1]
# print(f"{data * a[unit]} 원")

# Exercise 46. 이중 반복문
# 구구단을 2단부터 9단까지 다음과 같이 출력하세요
# 출력 예
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 3 X 1 = 3
# 3 X 2 = 6
# .
# .
# .
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81

# sol)
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")
#     print("="*10)

# Exercise 47. 이중 반복문과 조건문
# 구구단을 2단부터 9단까지 출력하되, 계산 값이 짝수인 경우에만 출력하세요
# 예: 3 X 3 = 9 에서 9는 홀수이므로 출력하지 않는다.
# 예: 2 X 4 = 8 에서 8은 짝수이므로 출력한다.

# sol)
# for i in range(2, 10):
#     for j in range(1, 10):
#         if (i * j) % 2 == 0:
#             print("{} * {} = {}".format(i, j, i * j))
#     print('='*10)

# Exercise 48. 이중 반복문과 데이터 구조 (리스트)
# 아파트 동호수를 다음과 같은 두 리스트 변수를 활용해서 출력하세요.
# 단, 각 동과 동 사이에는 구분이 되도록 한 라인씩 띄워서 출력하세요
# dongs = ["6209동", "6208동", "6207동"]
# hos = ["101호", "102호", "103호", "104호"]

# sol1)
# dongs = ["6209동", "6208동", "6207동"]
# hos = ["101호", "102호", "103호", "104호"]
# for dong in dongs:
#     for ho in hos:
#         print(dong, ho)
#     print()

# sol2)
# dongs = ["6209동", "6208동", "6207동"]
# hos = ["101호", "102호", "103호", "104호"]

# tmp = {}
# a = [(dong, ho) for dong in dongs for ho in hos]
# for dong, ho in a:
#     tmp.setdefault(dong, []).append(ho)
# print(tmp)
# for dong, hos in tmp.items():
#     for ho in hos:
#         print(dong, ho)
#     print()