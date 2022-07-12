# if.py

#조건문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#비교 연산자
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# x in s, x not in s
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
	print("택시를 타고가라")
elif card: 
   print("택시를 타고가라")
else:
   print("걸어가라")
