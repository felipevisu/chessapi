from typing import Coroutine
import graphene

from ...game import models

from .types import Piece, Board
from .enums import ColorEnum, PieceTypeEnum


class PieceCreate(graphene.Mutation):
    piece = graphene.Field(Piece)

    class Arguments:
        color = ColorEnum()
        piece_type = PieceTypeEnum()

    @classmethod
    def mutate(cls, root, info, color, piece_type):
        piece = models.Piece.objects.create(color=color, piece_type=piece_type)
        return PieceCreate(piece=piece)


class BoardUpdate(graphene.Mutation):
    board = graphene.Field(Board)

    class Arguments:
        rows = graphene.Int()
        cols = graphene.Int()

    @classmethod
    def mutate(cls, root, info, rows, cols):
        board = models.Board.load()
        board.rows = rows
        board.cols = cols
        board.save()
        return BoardUpdate(board=board)