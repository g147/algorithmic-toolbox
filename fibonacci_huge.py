# Uses python3

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        if (previous == 0 and current == 1): 
            return i + 1

def get_fibonacci_huge_naive(n, m):
    pisano_period = pisanoPeriod(m) 
    n = n % pisano_period 
    previous, current = 0, 1
    if n==0: 
        return 0
    elif n==1: 
        return 1
    for i in range(n-1): 
        previous, current = current, previous + current           
    return (current % m) 

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
