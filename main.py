# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def __init__(self):
        pass

    def coin_change(self, amount, coins):
        cache = {}
        def dfs(amt, i):
            if amt == 0:
                return 1

            if i >= len(coins) or amt < 0:
                return 0

            if (amt, i) in cache:
                return cache[(amt, i)]

            res = dfs(amt - coins[i], i) + dfs(amt, i+1)

            cache[(amt, i)] = res

            return res

        return dfs(amount, 0)


obj = Solution()
coins = [1,2,5]
res = obj.coin_change(5, coins)
print(res)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
