numbers=[]
print("enter 10 numbers:")
for i in range(10):
    a=input("enter the number:")
    numbers.append(float(a))
total_sum=sum(numbers)
print("the sum of all elements is ",total_sum)