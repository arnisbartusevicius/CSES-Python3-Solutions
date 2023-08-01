size = int(input())
 
if size == 2 or size == 3:
    print("NO SOLUTION")
else:
    upper_bound = int(size/2)
    for i in range(1, upper_bound+1):
        print(2*i, end=" ")
    for i in range(1, upper_bound+1):
        print(2*i-1, end=" ")
    if size % 2 == 1:
        print(size)