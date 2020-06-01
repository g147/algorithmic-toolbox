# Uses python3
import sys

def optimal_sequence(n):
    operations_count = [0] * (n + 1)
    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        min_count = min([operations_count[x] for x in count_index])
        operations_count[i] = min_count + 1
    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)
        current_value = min(
            [(c, operations_count[c]) for c in option_list],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    return reversed(value_trail)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
