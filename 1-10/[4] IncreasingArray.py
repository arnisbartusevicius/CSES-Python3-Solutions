size = int(input())
nums = [int(i) for i in input().split()]
prev_num = nums[0]
moves = 0

for i in nums:
    if i < prev_num:
        moves += prev_num - i
        i = prev_num
    prev_num = i
print(moves)