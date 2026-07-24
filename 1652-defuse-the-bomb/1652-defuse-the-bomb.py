class Solution:
    def decrypt(self, code: List[int], k: int):
        if k == 0:
            return [0] * len(code)

        i = 0
        d = []

        while i < len(code):
            count = 0
            tot = 0

            if k > 0:
                j = i + 1

                while count < k:
                    if j >= len(code):
                        j = 0

                    tot += code[j]
                    j += 1
                    count += 1

            else:
                j = i - 1

                while count < abs(k):
                    if j < 0:
                        j = len(code) - 1

                    tot += code[j]
                    j -= 1
                    count += 1

            d.append(tot)
            i += 1

        return d