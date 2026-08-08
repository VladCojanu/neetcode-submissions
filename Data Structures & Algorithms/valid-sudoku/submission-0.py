class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_to_set = [None] * len(board) # col[idx] : set
        for i in range(len(board)): 
            col_to_set[i] = set()

        row_set = set() 
        square_to_set = dict() # (idx, ydx) : set


        for i in range(len(board)):
            row_set = set()

            for j in range(len(board)): 
                value = board[i][j]
                # empty check
                if value == ".":
                    continue

                # row_check
                if value in row_set:
                    return False
                else:
                    row_set.add(value)
                # col_check
                if  value in col_to_set[j]:
                    return False
                else:
                    col_to_set[j].add(value)

                # square_check
                si = i // 3
                sj = j // 3 
                if (si, sj) not in square_to_set:
                    print('not in', (si, sj))
                    square_to_set[(si, sj)] = set()
                if value in square_to_set[(si, sj)]:
                    return False
                else: 
                    (square_to_set[(si, sj)]).add(value)
                
        return True

