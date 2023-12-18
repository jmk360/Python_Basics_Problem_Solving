# 반복문과 리스트

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

# sol)
