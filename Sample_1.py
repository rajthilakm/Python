def sum67(nums):   
  while (6 in nums):
      x=nums.index(6)
      y=nums.index(7)
      del nums[x:y+1] 
  if len(nums)==0:
      return 0
  else:    
      return sum(nums) 