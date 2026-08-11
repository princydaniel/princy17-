#sum of even number

n=int(input("Enter the number"))

even_s=0
count=0
if n>=0:
 for i in range(1,n+1):
       if i%2==0:
        even_s= even_s+i
        count=count+1
print("Sum of even number is:",even_s)
print("number of even numbers: ",count)
