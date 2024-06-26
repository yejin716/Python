# -*- coding: utf-8 -*-
"""python_08_list_com_lamda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QWehDSIog1uTAgCHXYzRXRc0H2vSl-RQ

list_comprehension(리스트 컴프리헨션)
"""

#반복문을 사용. 0~10까지 숫자를 리스트로 만들어요

number = []

for i in range(0,11):
    number = i
    print(number)

#for문 사용 정답!
number = []

for i in range(10+1):
    number.append(i) #리스트 3줄

print (number)

#list comprehension

number = [i for i in range(10+1)] # 1줄로

print(number)

number = []
for i in range(0,11):
    number.append(i) #리스트 3줄

print (number)

"""조건문이 있는 리스트 컴프리헨션"""

#0~10까지 숫자 중에서 홀수만 되어서
odds = []

for i in number(11):
    if i % 2 == 1:
      odds.append(i)

print(odds)

#정답

odds = []

for i in range(10+1):
    if i % 2 == 1:
        odds.append(i)

print(odds)

#list comprehension

odds = [i for i in range(10+1) if i % 2 == 1]

print(odds)

"""조건이 2개 라면?"""

# 0~10까지 숫자 중 , 홀수이고 5보다 작은 수

odds = []

for i in range(10 +1):
    if (i % 2 == 1) and (i < 5):
        odds.append(i)

print(odds)

odds = [i for i in range(10+1) if i % 2 == 1 if i < 5]
print(odds)

"""이중 반복문(for문이 2개) 를 list comprehension으로 바꾼다면?


"""

가게 = ['올리브영','세븐일레븐','엘지25']
제품 = ['폰 충전기','물티슈','콜라']

살거 = [( x,y )for x in 가게 for y in 제품 ]

print(살거)

"""lambda(람다) 식"""

#람다식 : 매개변수와 매개변수가 들어갈 식(함수)를 한 줄로 표현(일회용 함수)

x =4
y =7

x +y

lambda x ,y : x + y

(lambda x,y : x + y)(8,10)

(lambda x,y : 2**x + 3)(2,3)

lambda x ,y : x + y



