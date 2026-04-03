class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store = {}

        def helper(amount):
            if amount == 0:
                return 0
            if amount in store:
                return store[amount]

            res = math.inf
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    res = min(res, 1+helper(amount-coins[i])) # so we get the smallest total
            store[amount] = res
            return store[amount]
        
        total = helper(amount)

        return -1 if total >= math.inf else total
        

