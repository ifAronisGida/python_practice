N = int(input("How long the list should be?"))
numbers = []

i = 0
while i < N:
    numbers.append(int(input("Enter the next number:")))
    i += 1

print(numbers)

i = 1
while i < N:
    j = 0
    while j <= N-2:
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        j += 1    
    i += 1
    

print(numbers)