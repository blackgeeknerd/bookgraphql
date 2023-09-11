import graphene
from graphene import ObjectType, Mutation
from .models import BookDocument

class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()

class CreateBook(Mutation):
    class Arguments:
        input = BookInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, input):
        book = BookDocument(input.title, input.author)
        book.save()
        return CreateBook(success=True)

class Mutation(ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(mutation=Mutation)