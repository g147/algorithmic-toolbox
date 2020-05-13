# Uses python3
def get_change(m):
    c=0
    curr=[10,5,1]
    for i in curr:
        if(m>=i):
            c,m=c+(m//i),(m%i)
    return c

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
