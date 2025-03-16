class GameXo:
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        print('-'*7)
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print('\n-------')

    def is_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def make_move(self, player):
        row, col = map(int, input(f'Игрок {player} - Выберите клетку для хода (0-2): ').split())
        if self.board[row][col] == ' ':
            self.board[row][col] = player
        else:
            print('Неверный ход. Попробуй еще раз...')
            self.make_move(player)


    def play(self):
        self.current_player = 'X'
        is_game_over = False
        
        while not is_game_over:
            self.display_board()
            self.make_move(self.current_player)
            if self.is_winner(self.current_player):
                print(f'Игрок {self.current_player} выиграл!')
                is_game_over = True
            elif self.is_board_full():
                print('Это ничья')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    
if __name__ == '__main__':
    myGame = GameXo()
    while input('Желаете сыграть в крестики-нолики? (д/н)').lower() in 'дДLl':
        myGame.play()