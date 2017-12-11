class GravityPuzzleEasy:
    def solve(self, board):
            R = len(board)
            C = len(board[0])
            res_board = [['.'] * C for _ in range(R)]

            box_count = [0] * C
            for r, row in enumerate(board):
                for c, cell in enumerate(row):
                    if cell == '#':
                        box_count[c] += 1


            for c in range(C):
                for i in range(box_count[c]):
                    r = R - i - 1
                    res_board[r][c] = '#'

            res_board = [''.join(r) for r in res_board]
            return res_board

G = GravityPuzzleEasy()
#res =G.solve(["..#.#", "#.#..", "...##"])
res =G.solve(["#",'.','.'])

for r in res:
    print(r)

