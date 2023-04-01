def recursive_sum(n):
    if n == 0:
        return n
    else:
        return n % 10 + recursive_sum(n//10)


print(recursive_sum(12345))
