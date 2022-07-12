#Function.py

# 입력값이 없는 함수
def say():
	return 'Hi'
a = say()
print(a)

# 결과 값이 없는 함수
def add(a,b):
	print("%d, %d의 합은 %d입니다." %(a,b, a+b))

add(3,4)

# 입력값과 결과값이 없는 함수
def say():
	print('Hi')
say()

# 매개변수 지정하여 호출하기
def add(a,b):
	return a+b
result = add(a=3, b=7)
print(result)

# 입력값이 다수일 때

def add_many(*args):
	result = 0
	for i in args:
		result += i
	return result

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
	if choice == "add":
		result = 0
		for i in args:
			result += i
	elif choice == "mul" :
		result = 1
		for i in args:
			result *= i
	return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)
