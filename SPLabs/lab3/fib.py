#Dazarus Chapman
import time

start_time = time.time()

# Naive recursive Fibonacci implementation
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result_naive = fibonacci(40)
end_time = time.time()
elapsed_time = end_time - start_time # This is in seconds.

print(f"Naive approach: F(40) = {result_naive}, Time taken: {elapsed_time}s")

start_time1 = time.time()
def fibonacci_memo(n: int) -> int:
    memo = {} # Hashmap -> {key: value}
    def fibonacci(n):
        
        if n not in memo:
            if n < 2:
                memo[n] = n
            else:
                memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]
    return fibonacci(n)

result_memo = fibonacci_memo(40)
end_time2 = time.time()
elapsed_time2 = end_time2 - start_time1 # This is in seconds.

print(f"Memo approach: F(40) = {result_memo}, Time taken: {elapsed_time2}s")