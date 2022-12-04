# creating an empty list
lst = []
tmp = 0 
min = 0
c = 0 
my = 0
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
print("Enter elements : \n")
for i in range(0, n):
    n1 = int(input())
  
    lst.append(n1) # adding the element
      
#print(lst)
for i in range(0,n):
    #for j in range(0,n):
    tmp = lst[i]
    for j in range(0,n):
        if(tmp<lst[j]):
            min = lst[j]
            c= j
            a = lst[c]
            lst[c] = lst[my]
            lst[my] = a
    my = my +1
    print(lst)
