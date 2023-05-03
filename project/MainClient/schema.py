import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.views import GraphQLView

class GraphQLView(GraphQLView):
    schema = schema

class CustomerProfileSchema(DjangoObjectType):
    class Meta:
        model = CustomerProfile
        fields='__all__'

class Query(graphene.ObjectType):
    """
  Queries for the CustomerProfile model
    """
    my_model = graphene.Field(CustomerProfileSchema)

    def resolve_my_model(self, info,**kwargs):
        return CustomerProfile.objects.all()

schema = graphene.Schema(query=Query)