class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={0:1}
        prefix=0
        ans=0
        for num in nums:
            prefix+=num
            if (prefix-k) in count:
                ans+=count[prefix-k]
            count[prefix]=count.get(prefix,0)+1
        return ans