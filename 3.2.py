n = int(input())
sum = 0
for i in range(1,n+1):
    if(i == 1):
        sum = i
    sum *= i
print(sum)