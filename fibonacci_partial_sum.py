# Uses python3
fibs={
    0:0,
    1:1
}

def fibonacci_partial_sum_naive(from_, to):
    from_=from_%60
    to=to%60
    if to<from_:
        to+=60
    for i in range(2,60):
    	fibs.update({i: (fibs.get(i-1)%10+fibs.get(i-2)%10)%10})
    sum=0
    for i in range(from_, to+1):
        sum += fibs.get(i%60)
    return sum%10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))