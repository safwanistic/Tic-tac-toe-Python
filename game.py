from player import HumanPlayer, RandomComputerPlayer
import time
import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #Using single list to represent a 3x3 board
        self.current_winner = None

    def print_board(self):
        #For the rows
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range (3)]
        for row in number_board:
            print('| ' + ' | '. join(row) + ' |' )

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves=[]
        # for (i,spot) in enumerate(self.board):
        #     ['x','x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Checking Rows
        row_index = square // 3  
        row =self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Checking column possibility of winning
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Checking diagonal
        if square%2 == 0 :
            diagonal1 =[self.board[i] for i in [0, 4, 8]] #left to right diagonal  ' / '
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 =[self.board[i] for i in [2, 4, 6]] #Right to left diagonal ' \ '
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all the conditions of diagonals are not met    
        return False
        
def play(game, x_player, o_player, print_game = True):
    #returnng the winner of the game, even if it is a tie
    if print_game: 
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter +' WON!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter ='O'
            # else:
            #     letter ='X'
        #Smol break for computer move
        time.sleep(0.8)
    if print_game:
            print('MATCH DRAWN')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)