import graphene
from graphene_django.types import DjangoObjectType
from graphene import ObjectType, Mutation
from .models import User, Book
import json
import bcrypt

class UserType(DjangoObjectType):
    class Meta:
        model = User

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()

class SignupMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, username, password):
        # Hash the password for storage (you can use a better hashing method)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user
        user = User(username=username, password=hashed_password)
        user.save()

        return SignupMutation(success=True)

class Mutation(graphene.ObjectType):
    signup = SignupMutation()

schema = graphene.Schema(query=Query, mutation=Mutation)