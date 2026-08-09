class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones the current player
        # can collect starting from index i with M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # Can take all remaining piles
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                # Try taking X piles
                for X in range(1, 2 * M + 1):

                    if i + X > n:
                        break

                    new_M = max(M, X)

                    # Current player gets everything remaining
                    # except what the opponent can optimally get
                    current = suffix[i] - dp[i + X][new_M]

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]