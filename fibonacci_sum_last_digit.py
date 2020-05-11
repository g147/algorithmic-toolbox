# Uses python3

fibs={
    0:0,
    1:1
}

def fibonacci_sum_naive(n):
    if n in fibs:
        return fibs.get(n)
    n=(n+2)%60
    for i in range(2,n+1):
    	fibs.update({i: (fibs.get(i-1)%10+fibs.get(i-2)%10)%10})
    if(fibs.get(n) == 0):
        return 9
    return (fibs.get(n) % 10) - 1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
