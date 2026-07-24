class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Customers already satisfied
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # Extra customers we can satisfy using the technique
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        # Sliding window
        for j in range(minutes, len(customers)):
            if grumpy[j] == 1:
                extra += customers[j]

            if grumpy[j - minutes] == 1:
                extra -= customers[j - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra