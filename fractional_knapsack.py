# Uses python3
from collections import OrderedDict 

def get_optimal_value(capacity, weights, values):
    value = 0.0
    amounts={}
    capacities={}
    for weight,val in zip(weights,values):
        amounts.update({val/weight:val})
        capacities.update({val/weight:weight})
    amounts = OrderedDict(sorted(amounts.items(), reverse=True))
    for ind,val in amounts.items():
        if(capacity==0):
            break
        if(capacities.get(ind)<=capacity):
            capacity-=capacities.get(ind)
            value+=val
        else:
            value+=val/capacities.get(ind)*capacity
            break
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
