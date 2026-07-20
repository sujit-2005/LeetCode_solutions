class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        freq = dict(sorted(freq.items(),key=lambda item: item[1],reverse=True))

        l = []

        for num in freq:
            l.append(num)
            if len(l) == k:
                break

        return l