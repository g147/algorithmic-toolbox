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

def fibonacci_sum_squares_naive(n):
    if n<=1:
        return n
    current = calc_fib(n%60)
    next = calc_fib((n+1)%60)
    return ((current % 10) * (next % 10) % 10)

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
