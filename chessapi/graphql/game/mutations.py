from typing import Coroutine
import graphene

from ...game import models

from .types import Piece
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