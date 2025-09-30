"""
Core Classes:
    - Player
        - Attributes: name, symbol (X or O).
        - Methods: make_move(board).
        - HumanPlayer (inherits from Player)
        - Implements make_move() by asking the user for input.
        - ComputerPlayer (inherits from Player)
        - Implements make_move() by choosing a move automatically (random or simple strategy).
    - Board
        - Attributes: 3x3 grid.
        - Methods: display(), update(position, symbol), check_winner(), is_full().
    - Game
        - Attributes: players, board, current_turn.
        - Methods: play(), switch_turns().   
"""
import random

class Player:
    """ 
    Base class for a player in the Tic-Tac-Toe game
    """
    def __init__(self, name, symbol):
        self.name = name
        if symbol not in ("X", "O"):
            raise ValueError("symbol must be either 'X' or 'O'")
        self.symbol = symbol
    def make_move(self, board):
        """ 
        abstract method to make a move on the board
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
    
class HumanPlayer(Player):
    """ 
    Human player class inheriting from Player
    """
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def make_move(self, board):
        """ 
        implements make_move() by asking the user for input
        """
        while True:
            try:
                pos = input(f" Player {self.name} ({self.symbol}) turn , enter your move (1-9): ")
                pos = int(pos)
                if pos < 1 or pos > 9:
                    print("Invalid position. Choose 1-9.")
                    continue
                if board.update(pos, self.symbol):
                    break
                else:
                    print("Position already taken. Try again.")
            except ValueError:
                print("Please enter a valid number.")
class ComputerPlayer(Player):
    """ 
    Computer player class inheriting from Player
    """
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def make_move(self, board):
        available = board.available_positions()
        pos = random.choice(available)
        print(f"{self.name} ({self.symbol}) chooses position {pos}")
        board.update(pos, self.symbol)
    
class Board:
    """
    Represents the Tic-Tac-Toe game board and provides methods to interact with it.
    Handles board state, move updates, winner checking, and available positions.
    """     
    def __init__(self):
        self._grid = [" " for _ in range(9)]

    def display(self):
        """
        Prints the current board state.
        """
        for i in range(3):
            row = self._grid[i*3:(i+1)*3]
            print(" | ".join(row))
            if i < 2:
                print("---------")


    def __str__(self):
        s = ""
        for i in range(3):
            row = self._grid[i*3:(i+1)*3]
            s += " | ".join(row) + "\n"
            if i < 2:
                s += "---------\n"
        return s

    def update(self, position, symbol):
        """
        Updates the board with the given symbol at the specified position.
        """        
        idx = position - 1
        if self._grid[idx] == " ":
            self._grid[idx] = symbol
            return True
        return False

    def check_winner(self):
        """ 
        Checks if there is a winner on the board.
        Returns the symbol of the winning player if there is a winner, otherwise returns None.
"""
        lines = [
            [0,1,2], [3,4,5], [6,7,8], # rows win conditions
            [0,3,6], [1,4,7], [2,5,8], # cols win  conditions
            [0,4,8], [2,4,6]           # diags win coniditions
        ]
        for line in lines:
            a,b,c = line
            if self._grid[a] == self._grid[b] == self._grid[c] != " ":
                return self._grid[a]
        return None

    def is_full(self):
        """ 
        Checks if the board is full.
        Returns True if there are no empty spaces left on the board, otherwise returns False.
        """
        return all(cell != " " for cell in self._grid)

    def available_positions(self):
        """
        Returns a list of available positions on the board.
        Provides the positions (1-9) that are currently empty and can be played.
        """
        return [i+1 for i, cell in enumerate(self._grid) if cell == " "]
    
class Game:
    """ 
    Manages the flow of a Tic-Tac-Toe game between two players.
    Handles player turns, game state, and determines the outcome of the game.
    """
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_turn = 0

    def switch_turns(self):
        """
        Switches the turn to the other player.
        Updates the current_turn attribute to alternate between players.
        """
        self.current_turn = 1 - self.current_turn

    def play(self):  
        """
        Runs the main game loop for Tic-Tac-Toe.
        Alternates player turns, updates the board, and determines the winner or if the game is a draw.
        """
        print("\n--- Tic-Tac-Toe ---")
        self.board.display()
        while True:
            player = self.players[self.current_turn]
            player.make_move(self.board)
            self.board.display()
            winner = self.board.check_winner()
            if winner :  
                print(f"{player.name} wins")
                break
            if self.board.is_full():
                print("It's a draw!")
                break
            self.switch_turns()

def main():
    """
    Entry point for running a Tic-Tac-Toe game session.
    Prompts the user to select the game mode, gathers player information, and starts the game.
    """
    print("\nto play with a friend write 1 to play vs computer write 2")
    user_input = input("Enter 1 or 2: ").strip()
    while user_input not in ("1", "2"):
        user_input = input("Please enter 1 or 2: ").strip()
    symbol1 = "X"
    symbol2 = "O"    
    if user_input == "1":
        name1 = input("Player 1 name: ").strip()
        name2 = input("Player 2 name: ").strip()
        p1 = HumanPlayer(name1, symbol1)
        p2 = HumanPlayer(name2, symbol2)
    else:
        name1 = input("Your name: ").strip()
        p1 = HumanPlayer(name1, symbol1)
        p2 = ComputerPlayer("Computer", symbol2)
    board = Board()
    game = Game([p1, p2], board)
    game.play()

if __name__ == "__main__":
    main()
