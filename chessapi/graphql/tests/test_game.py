import json

QUERY_PIECES = """
query {
    pieces {
        id
        color
        pieceType
    }
}
"""

QUERY_MOVEMENTS = """
query {
    movements(id: 1, position: "d4")
}
"""


def test_query_pieces(client_query, knight):
    response = client_query(QUERY_PIECES)
    content = json.loads(response.content)
    piece = content['data']['pieces'][0]

    assert 'errors' not in content
    assert piece['color'] == "BLACK"
    assert piece['pieceType'] == "KNIGHT"


# get the horse movements for "d4" position
def test_movements(client_query, knight):
    response = client_query(QUERY_MOVEMENTS)
    content = json.loads(response.content)
    movements = content['data']['movements']

    assert 'errors' not in content
    assert movements == ['c2', 'c6', 'e2', 'e6', 'b3', 'b5', 'f3', 'f5']