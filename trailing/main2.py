def trailing(n) -> int:
    count = 0
    while n:count+= n/=5
    return count

print(trailing(150))
print(trailing(9227))
