fibonnaci_numbers = {0: 0, 1: 1}


def fibo(n):
    if n in fibonnaci_numbers:
        return fibonnaci_numbers[n]
    print(f"calculating {n}")
    if n <= 1:
        return n
    number = fibo(n-1) + fibo(n-2)
    fibonnaci_numbers[n] = number
    return number


print(fibo(50))


# the next fibonacci number is the sum of the previous 2
