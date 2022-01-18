"""
numbers=["3","34","64"]

for i in range(len(numbers)):
    numbers[i]= int(numbers[i])
numbers[2]= numbers[2]+1
print(numbers[2])  

numbers=list(map(int,numbers))  

numbers[2]= numbers[2]+1
print(numbers[2])

num=[2,3,4,5,6,7,89,10,122]
square=list(map(lambda x:x*x,num))
print(square)

from logging.config import valid_ident


def square(a):
    return a*a
def cube(a):
    return a*a*a   
function=[square,cube]
for i in range(5):
    val = list(map(lambda x:x(i),function))  
    print(val)   """
#filter
list_1=[1,2,3,4,5,6,7,8,9]
def is_grater_5(num):
    return num>5
gr_than_5 = list(filter(is_grater_5,list_1))
print(gr_than_5)        