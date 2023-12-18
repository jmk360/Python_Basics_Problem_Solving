# 파이썬 조건문과 문자열

# Exercise 12. 기본 자료형
# 10, 2.2, "fun-coding" 각각을 변수에 넣고, 각 데이터 타입을 출력하세요.

# sol)
# a = 10
# b = 2.2
# c = "fun-coding"

# print(type(a))
# print(type(b))
# print(type(c))

# Exercise 13. 기본 자료형
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명하세요.
# code = '000660\n00000102\t12312312'
# print (code)

# sol)
# \t: 커서를 다음 탭의 위치로 이동시킨다.
# \n: 개행문자이다. 커서를 다음 줄로 이동시킨다.

# Exercise 14. 조건문
# 사용자로부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면에 출력하세요.

# sol)
# a = int(input(">> "))
# b = int(input(">> "))

# if a > b:
#     print(a)
# else:
#     print(b)

# Exercise 15. 조건문
# 사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력하세요.

# sol)
# a = int(input(">> "))

# if a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# Exercise 16. 조건문
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 작은 숫자를 출력하세요.

# sol)
# a = int(input(">>"))
# b = int(input(">>"))
# c = int(input(">>"))

# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)

# Exercise 17. 조건문
# 사용자로부터 점수를 입력 받은 후 등급을 출력하라.
# (A: 100 ~ 81, B: 80 ~ 61, C: 60 ~ 0)

# sol)
# score = int(input(">> "))
# if 80 < score:
#     print('A')
# elif 60 < score:
#     print('B')
# else:
#     print('C')

# Exercise 18. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아 출생 연도를 출력하세요.
# 예) 800001-1231231 주민번호를 입력받으면 80을 출력하면 됨

# sol)
# num = input("주민번호: ")
# print(num[:2])

# Exercise 19. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아 뒷자리 맨 앞의 숫자를 출력하세요.
# 주민등록번호 뒷자리 맨 앞자리는 성별을 나타냄
# 예) 800001-1231231 주민번호를 입력받으면 1을 출력하면 됨
# 1은 남성을 의미, 2는 여성을 의미, 최근 아이들은 3과 4를 사용함

# sol)
# num = input("주민번호: ")
# print(num[7])

# Exercise 20. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아, 성별을 '남성' 또는 '여성'으로 출력하세요.
# 주민등록번호 뒷자리 맨 앞자리는 성별을 나타냄
# 예) 800001-1231231 주민번호를 입력받으면 1을 출력하면 됨
# 1이면 남성, 2이면 여성을 출력하면 됨 (최근 아이들은 3과 4를 사용하지만 이 경우는 고려하지 않기로 함)

# sol)
# num = input("주민번호: ")
# if int(num[7]) == 1:
#     print("남성")
# else:
#     print("여성")

# Exercise 21. 문자열 다루기 (strip)
# 다음 문자열에서 ...를 제거하라.
# mystr = "a man goes into the room..."
# 출력 예: 'a man goes into the room'

# sol1)
# mystr = "a man goes into the room..."
# print(mystr)
# result = mystr.replace("...", "")
# print(result)

# sol2)
# mystr = "a man goes into the room..."
# print(mystr)
# result = mystr[:-3]
# print(result)

# sol3)
# mystr = "a man goes into the room..."
# print(mystr)
# result = mystr.strip('.')
# print(result)

# Exercise 22. 문자열 다루기 (strip)
# 주식 종목을 나타내는 종목코드에 공백과 줄바꿈 기호가 포함되어 있다. 공백과 줄바꿈 기호를 제거하고 종목코드만을 추출하라.
# code = '         000660\n            '
# 출력: '000660'

# sol)
# code = '         000660\n            '
# result = code.strip() # strip 함수는 인자를 주지 않으면 기본적으로 문자열 좌우의 화이트스페이스(스페이스, 탭, 개행)문자를 지운다.
# print(result)

# Exercise 23. 문자열 다루기 (count)
# 다음 문자열에서 'Python' 문자열의 빈도수를 출력하라.
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# 출력 예: 2

# sol)
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# result = python_desc.count("Python")
# print(result)

# Exercise 24. 문자열 다루기 (count)
# 다음 문자열에서 'p' 문자가 몇번 나오는지 빈도수를 출력하라.
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# 출력 예: 9

# sol)
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# result = python_desc.count('p')
# print(result)

# Exercise 25. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 들어 있는 문자열에서 두 번째와 네 번째 문자를 출력하라

# letters = "python"

# sol)
# letters = "python"
# print(letters[1], letters[3])

# Exercise 26. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 사용자로부터 문자열을 입력받아서 문자 n 이 들어있는지를 출력하라 ( n 이 들어 있으면 0, 안들어있으면 -1을 출력하라)

# sol)
# letters = input(">> ")
# if 'n' in letters:
#     print(0)
# else:
#     print(-1)

# Exercise 27. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 사용자로부터 문자열을 입력받아서 문자 n 이 들어있는지를 출력하라
# n 이 들어 있으면 'n 이 들어있습니다.', 안들어있으면 'n 이 안들어있습니다.' 를 출력하라

# sol)
# letters = input(">> ")
# if 'n' in letters:
#     print("n 이 들어있습니다.")
# else:
#     print("n 이 안들어있습니다.")

# Exercise 28. 문자열 다루기 (문자열 인덱싱)와 조건문
# 주민등록번호의 뒷 자리 7자리 중 두번째부터 세번째는 출생 지역 코드입니다.
# 다음 표를 참조하여 사용자로부터 주민 등록 번호를 입력 받은 후 출생지를 출력하세요.
# 지역 코드	출생 지역
# 00 ~ 08	서울
# 09 ~ 12	부산

# sol)
# num = input("주민번호: ")
# code = int(num[8:10])
# if code <= 8:
#     print("서울")
# elif code <= 12:
#     print("부산")

# Exercise 29. 문자열 다루기 (split)
# letters 라는 변수에 Dave,David,Andy 가 들어있다. 해당 변수값을 , 를 기준으로 분리해서 출력하라
# 출력 예: ['Dave', 'David', 'Andy']

# sol)
# letters = "Dave,David,Andy"
# print(letters.split(','))

# Exercise 30. 문자열 다루기 (split)
# 다음과 같은 파일 이름(확장자 포함)에서 확장자를 제거한 파일 이름만 출력하세요.
# filename = 'exercise01.docx'

# sol)
# filename = 'exercise01.docx'
# result = filename.split('.')[0]
# print(result)