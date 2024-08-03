# use dp to slove fibonacci series
dp = []

def fibo(n):
    
    # base case
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

n = int(input())

for i in range(n+1):
    dp.append(-1)

print(fibo(n-1))

