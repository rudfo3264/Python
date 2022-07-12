#Q1
#3의 배수의 합
num = 0
result = 0

while(num<1000):
	num = num +1
	if(num%3 ==0):
		result = result + num
	else:
		print("%d는 3의 배수가 아님" %num)

print("3의 배수의 합 : %d" %result)


#Q2
# * 출력

# *
# **
# ***
# ****
# *****

a = '*'

for i in range(0,6):
	print(a*i)
	
#Q3
#1부터 100까지 숫자 출력

n=0
while(n<100) :
	n+=1
	print(n)
	
# Q4
# 평균

Marks = [70,60,55,75,95,90,80,80,85,100]
number = 0
result = 0
avg = 0
for mark in Marks:
	result += Marks[number]
	number += 1
	#print(result)

avg = result/number

print("평균 : %d" %avg)

# Q5
# 리스트 내포  리스트 홀수만 두배수 출력
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)

