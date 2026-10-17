class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])
        rows = [set() for _ in range(r)]
        cols = [set() for _ in range(c)]
        boxes = [set() for _ in range(9)]

        for i in range(r):
            for j in range(c):
                num = board[i][j]
                if num == '.':
                    continue
                
                box = (i//3) * 3 + (j//3)

                if num in rows[i] or num in cols[j] or num in boxes[box]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)
        return True