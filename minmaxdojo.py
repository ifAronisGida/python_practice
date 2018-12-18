numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
N = len(numbers)
for i in numbers:
    j = 0
    while j <= N-2:
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        j += 1    

summ = 0
for x in numbers:
    summ = summ + x

print(numbers)
print("minimus is "+str(numbers[0]))
print("maximum is "+str(numbers[N-1]))
print("average is "+str(summ/N))