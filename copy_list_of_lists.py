## python is so annoying in treating lists...

def copy_of_board(board):
    visited = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board[0])):
            temp.append(board[i][j])
        visited.append(temp)
    return visited
