#!/usr/bin/python3
"""0. Prime Game - Ben and Maria playing with primes!"""


def is_prime(number):
    """
    number - the number to check if prime
    """
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def detect_multiples(num, list):
    """
    num - number to detect its multiples
    list - the list of numbers
    """
    for i in range(num, len(list) + 1):
        try:
            list[num * i] = True
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """
    x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    n_max = max(nums)
    list = [False] * (n_max + 1)

    for i in range(2, (n_max + 1)):
        if is_prime(i):
            list[i] = True

    for i in list:
        if i:
            detect_multiples(i, list)

    ben, maria = 0, 0

    prime_counts = [0] * (n_max + 1)
    for i in range(1, n_max + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime(i) else 0)

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"

    return None
