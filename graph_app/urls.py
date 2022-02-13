from django.urls import path
from graphene_django.views import GraphQLView
from .schema import *

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=my_schema)),
    path('graphql2', GraphQLView.as_view(graphiql=True, schema=my_schema2 ))
]