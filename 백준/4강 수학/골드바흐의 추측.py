max = 10000000
s = [False, False] + [True]*max
prime = []

for i in range(int(len(s)**0.5)+1):
	if s[i] == True:
		for j in range(i+i, len(s), i):
		    s[j] = False
prime = [i for i in range(2, max) if s[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(len(prime)):
        if s[n - prime[i]] == True:
            print(f"{n} = {prime[i]} + {n-prime[i]}")
            break