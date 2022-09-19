def twoSum(self, nums: List[int], target: int) -> List[int]:
    difference = {}
    for i in range(len(nums)):
        if (nums[i]) in difference:
            return [i,difference[nums[i]]]
        else:
            difference[target-nums[i]]=i