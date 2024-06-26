# -*- coding: utf-8 -*-
"""python_05_for_while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11dyrSNzGEWNQ6O06JUdHoHv80PnOPtnl

원소로 반복하기 (for)
"""

my_sum = 0 #초기화

nums = [1,2,3]

for i in nums:
    my_sum = my_sum + i

    print(my_sum) # 1+2+3 = 6

print(my_sum) # 6

nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
    print(i)

#변수 mix에 있는 "쌀" 개수 세어보기

mix = '쌀'
mix = '쌀' * 100

count = 0 #초기화

for i in mix:
    if i == '쌀':
        count += 1

print(count)

mix = ['쌀', '보리', '쌀']

count= 0

for i in mix:
    if i == '보리':
        count += 1

print(count)

mix_100 = mix * 100

count= 0

for i in mix_100:
    if i == '쌀':
        count += 1

print(count)

"""반복할 숫자의 범위"""

range(0, 10)
#range(start, end) >> [start, start+1...end-1]

list(range(10))

for i in range(0,10):
    print(i)

for i in range(5):
    print('안녕')

"""구구단"""

for i in range(1,10):
    print('9 *', i,'=',9*i)

