class Solution(object):
    def isValidSudoku(self, board):

        def valid_boxes(board):

            for start_i in range(0, 9, 3):
                for start_j in range(0, 9, 3):

                    values = ""
                    i = start_i

                    while i < start_i + 3:
                        j = start_j

                        while j < start_j + 3:
                            if board[i][j] in values:
                                return False

                            if board[i][j] in "123456789":
                                values += board[i][j]

                            j += 1

                        i += 1

            return True

        def valid_columns(board):

            for i in range(len(board)):
                value = ""
                for l in range(len(board[i])):

                    if board[l][i] in value:
                        return False

                    if board[l][i] in "123456789":
                        value += board[l][i]


            return True

        def valid_rows(board):

            for i in range(len(board)):
                value = ""
                for l in range(len(board[i])):
                    if board[i][l] in value:
                        return False

                    if board[i][l] in "123456789":
                        value += board[i][l]

            return True

        if valid_rows(board) and valid_columns(board) and valid_boxes(board):
            return True

        return False