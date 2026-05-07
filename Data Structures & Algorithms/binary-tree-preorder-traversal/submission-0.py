class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        resultList = [];

        def dfs(x):
            if not x:
                return

            resultList.append(x.val)

            dfs(x.left)
            dfs(x.right)
        
        dfs(root)
        return resultList
    
     