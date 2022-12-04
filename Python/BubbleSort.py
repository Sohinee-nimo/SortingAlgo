def bubble(a):#defining method to perform bubble sort
    for i in range(len(a)):
        for j in range(len(a)):
            if(j+1<len(a)):
                if(a[j]>a[j+1]):
                    b = a[j]
                    a[j] = a[j+1] 
                    a[j+1] = b
        #print(a)
    return a #return sorted array
                
n = int(input("Enter the length of an array"))#Length of array
print("Enter the elements of an array")
arr=[]#defining the array for which we are using lists
for i in range(n):
    arr.append(int(input()))#Array elements are being updated
    #in python we use lists as arrays and to insert an element we use append method which adds an element at the end of the list
print(bubble(arr))#calling method to perform bubble sort
