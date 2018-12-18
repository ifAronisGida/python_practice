def Fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)

new = input('How many of the Fibonacci numbers you want to see? ')
i = 0
while i < int(new):
    line = str(i+1) + ". " + str(Fib(i))
    print(line)
    i += 1
