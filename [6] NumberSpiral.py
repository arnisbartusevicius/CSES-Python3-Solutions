tests = int(input())
 
for test in range(tests):
    coords = [int(i) for i in input().split()]
    n = None
    if coords[0] > coords[1]:
        if coords[0] % 2 == 0:
            n = pow(coords[0],2)
            n = n - coords[1] + 1
        else:
            n = pow(coords[0]-1, 2)+1
            n = n + coords[1] - 1
    else:
        if coords[1] % 2 == 1:
            n = pow(coords[1],2)
            n = n - coords[0] + 1
        else:
            n = pow(coords[1]-1, 2)+1
            n = n + coords[0] - 1
    print(n)