# Uses python3
# from statistics import mode
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return 1
    #if(a.count(max(set(a), key = a.count))>right/2):
    #    return 1
    #if(a.count(mode(a))>right/2):
    #    return 1
    index = 0
    count = 1
    for i in range(1, right):
        if a[i] == a[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1
    count = 0
    for i in range(right):
        if a[i] == a[index]:
            count += 1
    if count > right // 2:
        return a[index]
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
