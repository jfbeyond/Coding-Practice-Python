

# 1 Two sum

# use hash table to store complements

def twoSum(nums, target):

    complement = {}
    
    for i,num in enumerate(nums):
    
        if target-num not in complement:
            complement[target-num] = i
        
        
    for i,num in enumerate(nums):
    
        if num in complement and num != target - num:
            return [i, complement[num]]
    

# O(n) O(n)