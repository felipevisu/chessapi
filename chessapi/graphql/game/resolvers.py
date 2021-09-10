import re

from ...game.game import get_piece_builder
from ...game.models import Piece, Board

def get_movements(id, position):
    obj = Piece.objects.filter(id=id).first()
    if not obj:
        raise Exception('Invalid piece')

    if not validate_position(position):
        raise Exception('Invalid position')

    piece = get_piece_builder(obj, position)
    board = Board.load()
    movements = piece.get_movements(board.cols, board.rows)
    return movements


def validate_position(position):
    pattern = re.compile(r"[a-z][0-9]")
    result = pattern.match(position)
    return bool(result)