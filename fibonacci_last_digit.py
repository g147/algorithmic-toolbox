# Uses python3
fibs={
    0:0,
    1:1
}
def get_fibonacci_last_digit_naive(n):
    if n in fibs:
        return fibs.get(n)
    for i in range(2,n+1):
        fibs.update({i: (fibs.get(i-1)+fibs.get(i-2))%10})
    return fibs.get(n)

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))

