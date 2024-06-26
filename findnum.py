            # find the position of duplicate numbers in the list

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
num = int(input("Enter number: "))

positions = []
for index in range(len(L)):
    if L[index] == num:
        positions.append(index)

if positions:
    print(f"Number {num} found at positions: {positions}")
else:
    print("Invalid--!")


            # or


l=[1,2,3,4,5,6,7,6]
num = int(input("Enter number: "))
c=l.count(num)
pos=0
while c>0:
    p=l.index(num,pos)
    print(p)
    pos=p+1
    c-=1




