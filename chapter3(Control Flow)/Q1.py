#Q1.py
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
