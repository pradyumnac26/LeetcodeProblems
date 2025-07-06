class FindSumPairs:
    # nums1 len is less than nums2 length okay, and we are ading a value to nums2[ind].can we calculate sum of all pairs and store it somewheere. 
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.x = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val 
        self.x[old_val]-=1 
        if self.x[old_val] == 0:
            del self.x[old_val]
        self.x[new_val]+=1
        self.nums2[index]= new_val
        
        

    def count(self, tot: int) -> int:
        cnt = 0 
        for i in self.nums1 : 
            cnt += self.x[tot-i]
        return cnt

                    


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)