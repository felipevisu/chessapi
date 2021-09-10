import re

from ...game.game import get_piece_builder
from ...game.models import Piece, Board

def get_movements(id, position):
    # check if exists
    obj = Piece.objects.filter(id=id).first()
    if not obj:
        raise Exception('Invalid piece')

    # validade the position with regex expression
    if not validate_position(position):
        raise Exception('Invalid position')

    board = Board.load()
    piece = get_piece_builder(obj, position)
    movements = piece.get_movements(board.cols, board.rows)

    second_turn = []
    for movement in movements:
        piece = get_piece_builder(obj, movement)
        second_turn += piece.get_movements(board.cols, board.rows)

    return list(dict.fromkeys(second_turn))


def validate_position(position):
    pattern = re.compile(r"[a-z][0-9]")
    result = pattern.match(position)
    return bool(result)