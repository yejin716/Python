# -*- coding: utf-8 -*-
"""python_07_method.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekyvi7MDlj-_gLVRGO2eVjTB8JutR9U7

append():list에서 추가
"""

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)

print(list_)

#.sort()정렬
list_2 = ['banana','apple','caramel']

list_2.sort()
print(list_2) # a,b,c 순서

list_3 = [5,4,3,2,1]
list_3.sort()

print(list_3)

"""sequence의 indexing 과 slicing
- indexing : sequence에서 한 원소를 가져오는 것
- slicing : sequence에서 일부분을 가져오는 것
"""

my_str = 'impossible'
my_list = ['Apple', 'Banana','Chamae','Durian']

my_str[2] # indexing

my_list[2:] # slicing

"""sequence 길이와 멤버 조사하기"""

my_str = 'abc'
print(len(my_str))
print('d' in my_str)

"""Dictionary 추가 연습"""

my_dict = {"사과" : "apple", "바나나" : "banana", "당근" : "carrot"}
my_dict['당근']

my_dict["망고"] = 'mango'
print(my_dict)

{[1,2,3] : "num"}
#TypeError: unhashable type: 'list'
#리스트는 KEY로 사용하지 못함

{(1,2,3) : "num"}
#tuple(상수) : immutable(변경불가) >> 고정된 값 >> dict가능







