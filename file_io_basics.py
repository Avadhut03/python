star=int(input("How many rows do yo want:\n"))
print("Type  1 or 0")
two=int(input())
bolean=bool(two)
if bolean==True:
    for i in range(1,star+1):
        for j in range(1,i+1):
          print("*",end=" ")
        print()  
else :
    for i in range(star,0,-1):
        for j in range(1,i+1):
             print("*",end=" ")
        print()     
