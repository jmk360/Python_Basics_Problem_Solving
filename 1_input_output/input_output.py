# 파이썬 입력과 출력

# Exercise 1. 문자열 출력하기
# 화면에 "Hello World"를 출력하라.

# sol)
# print("Hello World")

# Exercise 2. 문자열 출력하기
# 화면에 "Mary's cosmetics"를 출력하라. (중간에 '가 있음에 주의.)

# sol)
# print("Mary's cosmetics")
# print("Mary\'s cosmetics")

# Exercise 3. 포맷 연산자
# print 함수를 사용하여 3.141592의 값을 출력하라. 단, 출력된 값이 소수점 아래로 두 자리 숫자까지만 표시되도록 하라.
# 실행 예: 3.14

# sol)
# print("%.2f" % 3.141592)
# print("%.2f" % (3.141592))

# print("{:.2f}".format(3.141592))

# print(f"{3.141592:.2f}")

# Exercise 4. 사용자 입력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 출력하는 프로그램을 작성하라.
# 실행 예: first: 3 second: 4 합: 7

# sol)
# a = int(input("first: "))
# b = int(input("second: "))
# result = a + b
# print(f"합: {result}")

# Exercise 5. 사용자 입력 (반복문을 배우는 이유)
# 사용자로부터 출력하고자 하는 문자열과 반복 횟수를 4로 입력받았다고 가정하기, 문자열을 반복 횟수(4번)만큼 출력하는 프로그램을 작성하라.
# 실행 예: 문자열: hello 반복횟수: 4 "hellohellohellohello"

# sol1)
# strinput = input("문자열: ")
# count = int(input("반복횟수: "))
# print(strinput*count)

# sol2)
# strinput = input("문자열: ")
# count = int(input("반복횟수: "))
# for i in range(count):
#     print(strinput)

# Exercise 6. 형 변환
# 문자열 '720'를 정수형으로 변환하라. 정수 100을 문자열 '100'으로 변환하라.

# sol)
# str_tmp = '720'
# print(int(str_tmp))

# a = 100
# print(str(a))

# Exercise 7. 사칙 연산
# 사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.

# sol)
# a = int(input(">> "))
# b = int(input(">> "))

# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b}")

# Exercise 8. 거듭제곱
# 사용자로부터 밑과 지수를 입력 받은 후 거듭제곱 값을 출력하라.
# 실행 예: 밑: 3 지수: 2 3^2 = 9

# sol1)
# a = int(input("밑: "))
# b = int(input("지수: "))
# result = a ** b
# print(result)

# sol2)
# a = int(input("밑: "))
# b = int(input("지수: "))
# result = pow(a, b)
# print(result)

# Exercise 9. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값, 나눈 값, 나눈 몫, 나머지 값을 각각 출력하는 프로그램을 작성하세요.

# sol)
# a = int(input(">> "))
# b = int(input(">> "))

# print(f"{a} + {b} = {a + b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b}")
# print(f"{a} // {b} = {a // b}")
# print(f"{a} % {b} = {a % b}")

# Exercice9와 10은 동일한 문제이기 때문에, Exercice10은 생략한다.

# Exercise 11. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 나눈 값을 다음 조건에 맞추어 출력하는 프로그램을 작성하세요.
# format() 함수를 사용해서 출력하세요
# 단, 나눈 값은 소숫점 첫번째 자리까지만 출력하세요.

# sol)
# a = int(input(">> "))
# b = int(input(">> "))

# result = a / b
# print("{:.1f}".format(result))