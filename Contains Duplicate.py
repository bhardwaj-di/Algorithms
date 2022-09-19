def containsDuplicate(self, nums: List[int]) -> bool:
    int_dict = {}
    for i in nums:
        if i in int_dict:
            return True
        else:
            int_dict[i] = 0
    return False