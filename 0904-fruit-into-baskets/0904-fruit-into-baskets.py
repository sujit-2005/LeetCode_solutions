class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len