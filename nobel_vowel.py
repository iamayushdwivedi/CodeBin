n = int(input())
nums = list(map(int, input().split()))
nums_1 = []
freq = [0] * n
for i in range(n):
    freq[nums[i]] += 1

for i in range(n):
    if freq[i] == 1:
        nums_1.append(nums[i])
    else:
        while freq[nums[i]] == 1:
            freq[i] -= 1
            nums.remove(nums[i])
        nums_1.append(nums[i])
print(nums_1)