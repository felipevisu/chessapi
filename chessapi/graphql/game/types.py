from typing import Coroutine
from graphene_django import DjangoObjectType

from ...game import models

from .enums import ColorEnum, PieceTypeEnum


class Piece(DjangoObjectType):
    color = ColorEnum()
    piece_type = PieceTypeEnum()

    class Meta:
        model = models.Piece
        fields = ["id", "color", "piece_type"]


class Board(DjangoObjectType):
    
    class Meta:
        model = models.Board
        fields = ['id', 'rows', 'cols']