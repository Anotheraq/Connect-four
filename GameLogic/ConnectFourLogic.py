from Exceptions.ImpossibleMoveException import ImpossibleMoveException


class ConnectFourSkeleton:
    def __init__(self):
        self.current_player = 1
        self.next_player = 2
        self.row_count = 6
        self.column_count = 7
        self.board = self.generate_board()

    def generate_board(self):
        '''Zwraca plansze 6x7 uzupełnioną zerami'''
        return [[0 for i in range(self.column_count)] for i in range(self.row_count)]

    def get_board(self):
        '''Zwraca plansze'''
        return self.board

    def reset(self):
        '''Reset gry'''
        self.board = self.generate_board()
        self.current_player = 1

    def is_board_full(self):
        '''Zwraca True jeżeli plansza jest pełna'''
        return not any(0 in rows for rows in self.board)

    def change_turns(self):
        '''Czyni potocznego gracza następnym graczem'''
        self.current_player = self.next_player
        self.next_player = 1 if self.next_player == 2 else 2

    def drop_move(self, column):
        '''Dodaje monete do określonej kolumny'''
        raise NotImplementedError('drop_move is not implemented')

    def is_valid_drop(self, column):
        '''Zwraca true jezeli drop w określonej kolumnie jest możliwy'''
        raise NotImplementedError('is_valid_drop is not implemented')

    def kto_wygral(self, player):
        '''Zwraca True jeżeli określony gracz spełnia warunki dla tego żeby wygrać '''
        raise NotImplementedError('kto_wygral is not implemented')


class ConnectFourClassic(ConnectFourSkeleton):
    def __init__(self):
        super().__init__()

    def drop_move(self, col):
        '''Dodaje monete do określonej kolumny'''
        if self.is_valid_drop(col):
            for row in self.board:
                if row[col] == 0:
                    row[col] = self.current_player
                    return
        else:
            raise ImpossibleMoveException(col)

    def is_valid_drop(self, col):
        '''Zwraca true jezeli drop w określonej kolumnie jest możliwy'''
        return self.board[self.row_count - 1][col] == 0

    def kto_wygral(self, player):
        '''Zwraca True jeżeli określony gracz spełnia warunki dla tego żeby wygrać '''
        for cols in range(self.column_count - 3):
            for rows in range(self.row_count):
                if (self.board[rows][cols] == player
                        and self.board[rows][cols + 1] == player
                        and self.board[rows][cols + 2] == player
                        and self.board[rows][cols + 3] == player):
                    return True

        for cols in range(self.column_count):
            for rows in range(self.row_count - 3):
                if (self.board[rows][cols] == player
                        and self.board[rows + 1][cols] == player
                        and self.board[rows + 2][cols] == player
                        and self.board[rows + 3][cols] == player):
                    return True

        for cols in range(self.column_count - 3):
            for rows in range(3, self.row_count):
                if (self.board[rows][cols] == player
                        and self.board[rows - 1][cols + 1] == player
                        and self.board[rows - 2][cols + 2] == player
                        and self.board[rows - 3][cols + 3] == player):
                    return True

        for cols in range(self.column_count - 3):
            for rows in range(self.row_count - 3):
                if (self.board[rows][cols] == player
                        and self.board[rows + 1][cols + 1] == player
                        and self.board[rows + 2][cols + 2] == player
                        and self.board[rows + 3][cols + 3] == player):
                    return True

        return False


class ConnectFourPopOut(ConnectFourSkeleton):
    def __init__(self):
        super().__init__()

    def drop_move(self, col):
        '''Dodaje monete do określonej kolumny'''
        if self.is_valid_drop(col):
            for rows in self.board:
                if rows[col] == 0:
                    rows[col] = self.current_player
                    return
        else:
            raise ImpossibleMoveException(col)

    def is_valid_drop(self, column):
        '''Zwraca true jezeli drop w określonej kolumnie jest możliwy'''
        return self.board[self.row_count - 1][column] == 0

    def pop_move(self, col):
        '''Zrzuca monetę bieżącego gracza z określonej kolumny'''
        if self.is_valid_pop(col):
            for i in range(self.row_count - 1):
                self.board[i][col] = self.board[i + 1][col]
            self.board[self.row_count - 1][col] = 0
        else:
            raise ImpossibleMoveException(col)

    def is_valid_pop(self, column):
        '''Zwraca true jezeli pop w określonej kolumnie jest możliwy'''
        return self.board[0][column] == self.current_player

    def kto_wygral(self, player):
        '''Zwraca True jeżeli określony gracz spełnia warunki dla tego żeby wygrać '''

        for cols in range(self.column_count - 3):
            for rows in range(self.row_count):
                if (self.board[rows][cols] == player
                        and self.board[rows][cols + 1] == player
                        and self.board[rows][cols + 2] == player
                        and self.board[rows][cols + 3] == player):
                    return True

        for cols in range(self.column_count):
            for rows in range(self.row_count - 3):
                if (self.board[rows][cols] == player
                        and self.board[rows + 1][cols] == player
                        and self.board[rows + 2][cols] == player
                        and self.board[rows + 3][cols] == player):
                    return True

        for cols in range(self.column_count - 3):
            for rows in range(3, self.row_count):
                if (self.board[rows][cols] == player
                        and self.board[rows - 1][cols + 1] == player
                        and self.board[rows - 2][cols + 2] == player
                        and self.board[rows - 3][cols + 3] == player):
                    return True

        for cols in range(self.column_count - 3):
            for rows in range(self.row_count - 3):
                if (self.board[rows][cols] == player
                        and self.board[rows + 1][cols + 1] == player
                        and self.board[rows + 2][cols + 2] == player
                        and self.board[rows + 3][cols + 3] == player):
                    return True



        return False
