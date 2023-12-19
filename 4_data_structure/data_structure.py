# 파이썬 데이터 구조

# Exercise 49. 데이터 구조 (튜플)
# a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.

# sol)
# tmp = ('a', 'b', 'c', 'd', 'e')
# print(tmp[0], tmp[-1])

# Exercise 50. 데이터 구조 (튜플)
# 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.

# 실행코드
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'

# sol)
# 튜플은 불변(immutable)이기 때문에, 값을 변경(수정)할 수 없다.

# Exercise 51. 데이터 구조 (튜플)
# 다음 코드를 읽고, 최종적으로 var1과 var2의 값이 어떤 값이될지 확인해보고, 왜 이렇게 동작하는지 튜플을 기반으로 설명하세요.
# 실행코드
# var1, var2 = 1, 2
# var1, var2 = var2, var1

# sol)
# var1, var2 = 1, 2
# print(var1, var2) # 1 2
# var1, var2 = var2, var1
# print(var1, var2) # 2 1

# Exercise 52. 데이터 구조 (튜플)
# 다음 코드에서 두번째 데이터부터 마지막 데이터를 다음과 같이 출력하세요
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
# 출력:
# ('fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

# sol)
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
# print(tupledata[1:])

# Exercise 53. 데이터 구조 (튜플과 리스트)
# 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고, 다시 튜플 데이터로 변환하세요.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

# sol)
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
# listdata = list(tupledata)
# listdata.append("fun-coding4")
# tupledata = tuple(listdata)
# print(tupledata)

# Exercise 54. 데이터 구조 (튜플, 리스트, 딕셔너리)
# 비어 있는 튜플, 리스트, 딕셔너리 변수를 하나씩 각각 만드세요.

# sol)
# a = () # tuple()
# b = [] # list()
# c = {} # dict()
# print(type(a))
# print(type(b))
# print(type(c))

# Exercise 55. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들고, 딕셔너리 변수의 key 값인 영어단어, value 값인 의미 만을 가진 리스트 변수를 각각 만들고, 두 리스트 변수를 출력하세요.
# 영어단어	의미
# environment	환경
# company	회사
# government	정부, 정치
# face	얼굴
# 출력 예
# {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'}
# ['environment', 'company', 'government', 'face']
# ['환경', '회사', '정부, 정치', '얼굴']

# sol)
# word = {"environment": "환경", "company": "회사", "government": "정부, 정치", "face": "얼굴"}
# en = list(word.keys())
# ko = list(word.values())
# print(word)
# print(en)
# print(ko)

# Exercise 56. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들어서 다음과 같이 출력하세요.
# 단, 반복문을 사용하세요.
# environment : 환경
# company : 회사
# gonernment : 정부, 정치
# face : 얼굴
# 영어단어	의미
# environment	환경
# company	회사
# government	정부, 정치
# face	얼굴

# sol) # TODO: 여기 부터 시작하기
# word = {"environment": "환경", "company": "회사", "government": "정부, 정치", "face": "얼굴"}
# # print("영어단어", "\t\t", "의미")
# print("%15s" % "데이브")
# # for k, v in word.items():
# #     print(k, "\t\t", v)