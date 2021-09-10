import pytest
from graphene_django.utils.testing import graphql_query

from ...game.models import Piece, Board
from ...game import PieceType, Color


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.fixture
def knight(db):
    return Piece.objects.create(
        color=Color.BLACK,
        piece_type=PieceType.KNIGHT
    )


@pytest.fixture
def board(db):
    return Board.objects.create(rows=8, cols=8)