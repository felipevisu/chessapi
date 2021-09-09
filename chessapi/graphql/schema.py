import graphene

from .game.schema import GameQueries, GameMutations

class Query(
    GameQueries
):
    pass


class Mutation(
    GameMutations
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)