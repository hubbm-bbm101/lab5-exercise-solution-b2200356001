N = int(input('write N as a input: '))

oddsum = 0
evensum = 0

for i in range(1, N + 1):
    if i%2 == 1:
        oddsum += i

    else:
        evensum += i 

print("sum of odd numbers: ",oddsum)
print("average of even numbers: ",evensum/N)