def has_33():
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i-1] == 3:
            print ("True")
            break
    else:
        print ("False")
has_33()