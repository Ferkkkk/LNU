import os
from abc import ABC, abstractmethod


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def move(player: str, position_from: tuple, position_to: tuple):
    map = Board.get_map(Board)

class Game(ABC):
    def start(self):
        clear_terminal()
        board = Board()
        board.get()
        close_game = False
        while close_game == False:
            
            board.update()
            board.get()
            close_game = True
            
    """Base class for game logic (can be extended for specific games)."""
    pass

class Board(Game):
    """Represents the game board with its structure and functionalities."""

    map_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    map_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    empty_space = ' '  # Clearer naming for empty space representation
    map = {(symbol + number): ' ' for symbol in map_symbols for number in ['1', '2', '3', '4', '5', '6', '7', '8']}

    def __init__(self):
        """Creates the map initiation array with all positions for objects."""
        self.init_positions = {
            Pawn: [(symbol + number) for number in ['2', '7'] for symbol in self.map_symbols],
            Rook: [(symbol + number) for number in ['1', '8'] for symbol in ['a', 'h']],
            Knight: [(symbol + number) for number in ['1', '8'] for symbol in ['b', 'g']],
            Bishop: [(symbol + number) for number in ['1', '8'] for symbol in ['c', 'f']],
            Queen: [(symbol + number) for number in ['1', '8'] for symbol in ['d']],
            King: [(symbol + number) for number in ['1', '8'] for symbol in ['e']]
        }

        self.setup_pieces()

    def setup_pieces(self):
        """Creates and places pieces on the board."""
        for piece_type, positions in self.init_positions.items():
            for i, position in enumerate(positions):
                piece_name = f"{piece_type.__name__.lower()}_{i + 1}"
                num_pieces_per_color = len(self.init_positions[piece_type]) // 2  # Assuming Pawn is the reference piece type
                piece_color = 'white' if i < num_pieces_per_color else 'black'
                piece = piece_type(position=position, color=piece_color)
                setattr(self, piece_name, piece)


        

    def get_board(self):
        """Prints the formatted game board to the console."""
        symbols_lane = '    A   B   C   D   E   F   G   H    '
        top_border = '  ┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓ '
        bottom_border = '  ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛ '
        middle_border = '  ┣───┼───┼───┼───┼───┼───┼───┼───┫ '

        print(symbols_lane)
        print(top_border)

         # Loop through rows (assuming 8 rows based on map_numbers)
        for row_number in range(1, 9)[::-1]:
            row_string = f"{row_number} ┃ "
            for symbol in self.map_symbols:
                cell_value = self.map[symbol + str(row_number)]
                if symbol is not 'h':
                    row_string += f"{cell_value} | "
                else:
                    row_string += f"{cell_value} ┃ {row_number}"
            row_string += f" ┃ {row_number}"
            
            if row_number is not 8:
                print(middle_border)
            print(row_string[:-3])  # Remove trailing whitespace and pipe

        print(bottom_border)
        print(symbols_lane)
        
    def get_map(self):
        """Prints the internal map dictionary representation (for debugging purposes)."""
        print(self.map)
        
    def get(self):
        self.get_map()
        self.get_board()
        
    def update(self):
        piece_types = [Pawn, Rook, Knight, Bishop, Queen, King]
        
        for piece_type in piece_types:
            for piece in piece_type.get_all():
                self.map[piece.position] = piece


class Piece(Game):
    obj = True
    
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
    def move_on_map_validation(self, result_position):
        if result_position in list(Board.map.keys()):
            return True
        elif result_position not in list(Board.map.keys()): 
            return False
        else: raise Exception('Unepxected issue in this move')
    
    def __repr__(self) -> str:
        return self.symbol
    
    @abstractmethod
    def move(self, result_position):
        self.position = result_position
    

class Pawn(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Pawn.all) + 1
        Pawn.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♙'
        elif self.color is 'black':
            self.symbol = '♟'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Pawn.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
            return True 
        else:
            return False
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')

class Rook(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Rook.all) + 1
        Rook.all.append(self)
        self.position = position
        self.color = color
        if self.color is 'white':
            self.symbol = '♖'
        elif self.color is 'black':
            self.symbol = '♜'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Rook.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
        else: raise ValueError('It is not possible to move to this position')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')

class Knight(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Knight.all) + 1
        Knight.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♘'
        elif self.color is 'black':
            self.symbol = '♞'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Knight.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
        else: raise ValueError('It is not possible to move to this position')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')

class Bishop(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Bishop.all) + 1
        Bishop.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♗'
        elif self.color is 'black':
            self.symbol = '♝'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Bishop.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
        else: raise ValueError('It is not possible to move to this position')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')

class Queen(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Queen.all) + 1
        Queen.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♕'
        elif self.color is 'black':
            self.symbol = '♛'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Queen.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
        else: raise ValueError('It is not possible to move to this position')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')

class King(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(King.all) + 1
        King.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♔'
        elif self.color is 'black':
            self.symbol = '♚'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return King.all

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            self.position = result_position
        else: raise ValueError('It is not possible to move to this position')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [(self.position[0] + number) for number in range(3,4)]
            elif self.position[1] is not '8':
                expected_positions += [(str(int(self.position[1]) + 1))]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [(self.position[0] + number) for number in range(5,6)]
            elif self.position[1] is not '1':
                expected_positions += [(str(int(self.position[1]) - 1))]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        else: return False
        

game = Game()
game.start()