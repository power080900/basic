# print사용법
print(3 + 4)
a = 1
b = 2
print(a + b)

s = '서울'
d = '대전'
g = '대구'
b = '부산'
print(s, d, g, b, sep=' 찍고 ')

a = '강아지'
b = '고양이'
print(a, end='')
print(b)

# 입력
age = input('몇살이세요? ')
print(age)

price = int(input('가격을 입력하세요 :'))
num = int(input('수량을 입력하세요 :'))
print('총액은', price * num, '원 입니다')

# 변수
# 변수명 첫 글자에 숫자 사용 불가
# /, +, - 등 연산자 사용 불가
# 공백 사용 불가
# 대 소문자 구분 필수
