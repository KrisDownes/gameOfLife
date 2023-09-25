import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N = 200
vals = [0,1]

board = np.random.choice(vals,N*N,p=[0.5,0.5]).reshape(N,N)



def update(data):
        global board
        rows,cols = len(board),len(board[0])
        def countNeighbor(r,c):
            nei = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j==c) or i < 0 or j< 0 or i ==rows or j == cols):
                        continue
                    if board[i][j] in [1,3]:
                        nei +=1
            return nei
        for r in range(rows):
            for c in range(cols):
                nei = countNeighbor(r,c)
                if board[r][c]:
                    if nei in [2,3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
        mat.set_data(board)
        return mat
fig,ax = plt.subplots()
mat = ax.matshow(board)
ani = animation.FuncAnimation(fig,update,interval = 50,save_count=50)
plt.show()