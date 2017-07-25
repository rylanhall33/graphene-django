import graphene
from graphene import ObjectType, Schema, annotate, Context


class QueryRoot(ObjectType):

    thrower = graphene.String(required=True)
    request = graphene.String(required=True)
    test = graphene.String(who=graphene.String())

    def resolve_thrower(self):
        raise Exception("Throws!")

    @annotate(request=Context)
    def resolve_request(self, request):
        return request.GET.get('q')

    def resolve_test(self, who=None):
        return 'Hello %s' % (who or 'World')


class MutationRoot(ObjectType):
    write_test = graphene.Field(QueryRoot)

    def resolve_write_test(self):
        return QueryRoot()


schema = Schema(query=QueryRoot, mutation=MutationRoot)
