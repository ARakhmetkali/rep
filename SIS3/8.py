def spy_game(nums): 
    l=0  
    index = 0 
    for i in range(len(nums)): 
        if nums[i]==7: 
            index = i 
    for i in range(index): 
        if nums[i]==0: 
            l+=1   
    if(l>=2):      
        return True 
    else: 
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))