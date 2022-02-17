# my code
n, k = map(int, input().split())

count = 0

while True:
    if (n % k) == 0:
        n = n // k
    else:
        n -= 1
    count += 1
    if n == 1:
        break

print(count)

# example
'''
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
    
while n > 1:
    n -= 1
    result += 1
    
print(result)
'''