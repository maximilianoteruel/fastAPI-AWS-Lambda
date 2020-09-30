# GraphQL
import graphene

# Create Note
class NoteCreate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, id):
        return NoteCreate(status=True)


# Update Note
class NoteUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, id):
        return NoteUpdate(status=True)


# Delete Note
class NoteDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, id):
        return NoteDelete(status=True)
