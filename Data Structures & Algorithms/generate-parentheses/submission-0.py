class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        open_brackets = 0
        closed_brackets = 0
        res = []
        stack = []

        def bt_dfs(open_brackets, closed_brackets):

            if open_brackets == closed_brackets == n:
                res.append("".join(stack))
                return

            if closed_brackets > open_brackets:
                return

            if open_brackets < n:
                stack.append("(")
                bt_dfs(open_brackets+1, closed_brackets)
                stack.pop()


            if closed_brackets < open_brackets:
                stack.append(")")
                bt_dfs(open_brackets, closed_brackets+1)
                stack.pop()


        bt_dfs(0,0)



        return res



         
    







            

            
            