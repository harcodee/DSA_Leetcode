class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # last[j] = latest index in word1 where word2[j]
        # can be matched while matching word2[j:] from right to left.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        mismatch_used = False

        # Greedily choose the smallest possible index.
        for i in range(n):
            if j == m:
                break

            # Exact match: always take it.
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch.
            elif not mismatch_used:
                # After choosing i as word2[j], the remaining
                # word2[j+1:] must be matched exactly.
                #
                # i < last[j+1] guarantees that.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        return ans if j == m else []