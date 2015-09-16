def gen_fib(n):
    a,b = 0,1
    yield a
    for _ in range(n):
        a,b=b,a+b
        yield a
        
def fib(n):
    x = list(gen_fib(n))
    return x[n-1]
        
