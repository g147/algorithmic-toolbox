# Uses python3
fibs={
    0:0,
    1:1
}
def calc_fib(n):
    if n in fibs:
        return fibs.get(n)
    else:
        fibs.update({n:calc_fib(n-1) + calc_fib(n-2)})
        return fibs.get(n)

n = int(input())
print(calc_fib(n))
