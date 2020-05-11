# Uses python3
def gcd_naive(a, b):
    if(b==0):
        return a
    return gcd_naive(b,a%b)

def lcm_naive(a, b):
    return int((max(a,b)/gcd_naive(a,b))*min(a,b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

