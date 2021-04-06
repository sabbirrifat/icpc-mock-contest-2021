testCase = int(input())

for i in range(testCase):
    ss = input()
    values = list(map(int, input().split()))
    values.sort()
    if len(values) == 1:
        print("Case {}: {}".format(i+1, values[0]*values[0]))
    else:
        result = values[0] * values[len(values) - 1]
        print("Case {}: {}".format(i+1, result))
