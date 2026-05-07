class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen =  set()

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue

                row_k = ('row',i, val)
                col_k = ('col',j, val)
                box_k = ('box',i//3,j//3, val)

                if row_k in seen or col_k in seen or box_k in seen:
                    return False

                
                seen.add(row_k)
                seen.add(col_k)
                seen.add(box_k)
        
        return True

        