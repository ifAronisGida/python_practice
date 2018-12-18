def generate_tribonacci(signature, n):
    trib = []
    [trib.append(i) for i in signature]
    trib = trib[::-1]
    for i in range(n-3):
        j = trib[0] + trib[1] + trib[2]
        trib.insert(0, j)
    trib = trib[::-1]
    return trib


signature = [0, 0, 1]

print(generate_tribonacci(signature, 10))










