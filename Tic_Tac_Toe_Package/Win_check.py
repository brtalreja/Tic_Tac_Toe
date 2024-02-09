def win_check(board,mark):
    
    if board[1:4] == [mark, mark, mark] or board[4:7] == [mark, mark, mark] or board[7:] == [mark, mark, mark] \
        or (board[1] == mark and board[4] == mark and board[7] == mark) \
        or (board[2] == mark and board[5] == mark and board[8] == mark) \
        or (board[3] == mark and board[6] == mark and board[9] == mark) \
        or (board[1] == mark and board[5] == mark and board[9] == mark) \
        or (board[3] == mark and board[5] == mark and board[7] == mark):
            return True
    else:
        return False