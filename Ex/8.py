def spy_game(nums):
    for i in nums:
        if i == 7:
            num = nums[:nums.index(i)]
    if len(num) == len(nums):
        return False
    cnt = 0
    for j in num:
        if j == 0:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))