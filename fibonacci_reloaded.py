def gen_fib(n):
    a,b = 0,1
    yield a
    for _ in range(n):
        a,b=b,a+b
        yield a
        
def fib(n):
    x = list(gen_fib(n))
    return x[n-1]
        
#OR
def good fibonacci(n):
”””Return pair of Fibonacci numbers, F(n) and F(n-1).””” if n <= 1:
return (n,0) else:
(a, b) = good fibonacci(n−1) return (a+b, a)
