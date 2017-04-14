"""
Coin sums: Project Euler Problem 31

https://projecteuler.net/problem=31

Takes 0.4s on my computer.
"""
TARGET = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
memo = [0 for i in range(TARGET+1)]
memo[0] = 1

for coin in COINS:
	for j in range(coin, TARGET+1):
		memo[j] += memo[j - coin]

print(memo[TARGET])
