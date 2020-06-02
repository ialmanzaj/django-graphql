import graphene

from movies.schema import Query as SchemeQuery
from movies.mutation import Mutation as SchemeMutation

class Query(SchemeQuery, graphene.ObjectType):
    pass

class Mutation(SchemeMutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)