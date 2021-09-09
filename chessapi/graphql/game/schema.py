import graphene

from ...game import models

from .types import Piece
from .mutations import PieceCreate


class GameQueries(graphene.ObjectType):
    pieces = graphene.List(Piece)
    piece = graphene.Field(Piece, id=graphene.Argument(graphene.ID))

    def resolve_pieces(root, info):
        return models.Piece.objects.all()

    def resolve_piece(root, info, id):
        return models.Piece.objects.filter(id=id).first()


class GameMutations(graphene.ObjectType):
    piece_create = PieceCreate.Field()