import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import *
from django.views.decorators.csrf import csrf_exempt


class UserGraph(DjangoObjectType):
    class Meta:
        model = myUser
        fields = ('name', 'mail', 'mobile_no', 'id', 'strength')
    

class SchoolGraph(DjangoObjectType):
    class Meta:
        model = School
        fields = ('school_name', 'id')


class SClassGraph(DjangoObjectType):
    class Meta:
        model = SClass
        fields = ('standard', 'section','id', 'school')


class StrengthGraph(DjangoObjectType):
    class Meta:
        model = Strength
        fields = ('strength', 'class_n', 'id')


class myQuery(graphene.ObjectType):
    all_class = DjangoListField(SClassGraph)
    all_school = DjangoListField(SchoolGraph)
    def resolve_all_class(root, info):
        return SClass.objects.all()
    def resolve_all_school(root, info):
        return School.objects.all()


class myQuery2(graphene.ObjectType):
    all_class = DjangoListField(SClassGraph, school_id=graphene.Int())
    def resolve_all_class(root, info, school_id):
        return SClass.objects.filter(school_id=school_id)


my_schema = graphene.Schema(query=myQuery)
my_schema2 = graphene.Schema(query=myQuery2)
