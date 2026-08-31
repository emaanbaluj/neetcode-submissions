class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def bt_dfs(index, comb_sum, path):
            if comb_sum == target:
                res.append(path.copy())
                return
            if comb_sum > target or index >= len(nums):
                return

            for j in range(index, len(nums)):
                if comb_sum + nums[j] > target:
                    break
                path.append(nums[j])
                bt_dfs(j, comb_sum + nums[j], path)
                path.pop()

        bt_dfs(0, 0, [])
        return res