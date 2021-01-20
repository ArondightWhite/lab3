nums = range(19, 101)
s = 0
for i in range(0, len(nums)):
    if nums[i] % 3 == 0:
        s += nums[i]
print(f"Сумма чисел от {nums[0]} до {nums[len(nums)-1]} кратных 3 = {s}")
