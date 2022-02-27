number = int(input("Enter the number : "))
n2 = 1
sum = 0
count = 1

print("Fibonacci Number : ", end = "")
while(count <= number):
    print(sum, end=",")
    count = count + 1
    n1 = n2
    n2 = sum
    sum = n1 + n2
