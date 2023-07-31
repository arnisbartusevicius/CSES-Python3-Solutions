num = int(input())
expectedSum = (num*(num+1)) / 2
actualSum = 0
 
nums = input().split()
for i in nums:
    actualSum += int(i)
    
print(int(expectedSum-actualSum))