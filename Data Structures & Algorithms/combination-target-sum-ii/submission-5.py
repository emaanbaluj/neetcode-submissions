class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def bt_dfs(index, total, path):

          
            if total == target:
                res.append(path.copy())
                return

            if index >= len(candidates) or total > target:
                return    

            path.append(candidates[index])

            total += candidates[index]

            bt_dfs(index+1, total, path)
            
            total -= candidates[index]
            path.pop()
            

            # exclude candidates[index] — skip all duplicates of it, add nothing
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
           
                next_index += 1
                
            bt_dfs(next_index, total, path)
                    









            




        bt_dfs(0, 0 , [])


        return res




            