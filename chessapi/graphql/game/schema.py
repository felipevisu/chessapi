import graphene
from graphene.types.generic import GenericScalar

from ...game import models

from .types import Piece, Board
from .resolvers import get_movements
from .mutations import PieceCreate, BoardUpdate


class GameQueries(graphene.ObjectType):
    board = graphene.Field(Board)
    pieces = graphene.List(Piece)
    piece = graphene.Field(Piece, id=graphene.Argument(graphene.ID))
    movements = GenericScalar(
        id=graphene.Argument(graphene.ID), 
        position=graphene.Argument(graphene.String)
    )

    def resolve_board(root, info):
        return models.Board.load()

    def resolve_pieces(root, info):
        return models.Piece.objects.all()

    def resolve_piece(root, info, id):
        return models.Piece.objects.filter(id=id).first()

    def resolve_movements(root, info, id, position):
        return get_movements(id, position)


class GameMutations(graphene.ObjectType):
    piece_create = PieceCreate.Field()
    board_update = BoardUpdate.Field()