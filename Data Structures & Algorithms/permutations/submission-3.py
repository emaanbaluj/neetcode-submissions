class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
    
        def bt_dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 


            for num in nums:
                if num in path:
                    continue 

                path.append(num)

                bt_dfs(path)

                path.pop()

        bt_dfs([])

        return res