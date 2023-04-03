import sys

input = sys.stdin.readline

n = int(input())
nums = []
cnt = {}
for _ in range(n):
    num = int(input())
    cnt[num] = cnt.get(num, 0) + 1
    nums.append(num)

nums.sort()

print(int(round(sum(nums) / len(nums), 0)))
print(nums[len(nums) // 2])

mode_value = max(cnt.values())
modes = []
for key, value in cnt.items():
    if value == mode_value:
        modes.append(key)
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]
print(mode)

print(nums[n - 1] - nums[0])

