from abc import ABCMeta, abstractmethod
from itertools import product

from . import PieceType


class PieceInterface(metaclass=ABCMeta):
    def __init__(self, piece, position):
        self.piece = piece
        self.position = position

    def __str__(self):
        return f"{self.piece.piece_type} {self.position}"

    @abstractmethod
    def get_movements(self): 
        raise NotImplementedError


class PawnBuilder(PieceInterface):

    def get_movements(self, rows: int, cols: int):
        return []


class BishopBuilder(PieceInterface):

    def get_movements(self, rows: int, cols: int):
        return []


class KnightBuilder(PieceInterface):

    def get_movements(self, cols: int, rows: int):
        x, y = position_to_coordinate(self.position)
        if x > cols or y > rows:
            raise Exception('Invalid position')

        movements = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        movements = [(x,y) for x, y in movements if x >= 1 and y >= 1 and x < cols and y < rows]
        movements = [coordinate_to_position(movement[0], movement[1]) for movement in movements]
        return movements


class RookBuilder(PieceInterface):

    def get_movements(self, rows: int, cols: int):
        return []


class QueenBuilder(PieceInterface):

    def get_movements(self, rows: int, cols: int):
        return []


class KingBuilder(PieceInterface):

    def get_movements(self, rows: int, cols: int):
        return []


def get_piece_builder(piece, position):
    piece_type = piece.piece_type

    if piece_type == PieceType.PAWN:
        return PawnBuilder(piece, position)
    if piece_type == PieceType.BISHOP:
        return BishopBuilder(piece, position)
    if piece_type == PieceType.KNIGHT:
        return KnightBuilder(piece, position)
    if piece_type == PieceType.ROOK:
        return RookBuilder(piece, position)
    if piece_type == PieceType.QUEEN:
        return QueenBuilder(piece, position)
    if piece_type == PieceType.KING:
        return KingBuilder(piece, position)

    return None


def position_to_coordinate(position):
    col = int(ord(position[0]) - 96)
    row = int(position[1:])
    return (col, row)


def coordinate_to_position(col, row):
    return f"{chr(col + 96)}{row}"