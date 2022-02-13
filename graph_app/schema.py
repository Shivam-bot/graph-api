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


class SchoolMutation(graphene.Mutation):
    class Arguments:
        school_name =  graphene.String(required=True)
    
    school = graphene.Field(SchoolGraph)
    @classmethod
    def mutate(cls, root, info, school_name):
        school = School(school_name=school_name)
        school.save()
        return SchoolMutation(school=school)

class Mutation(graphene.ObjectType):
    
    add_school = SchoolMutation.Field()


my_schema = graphene.Schema(query=myQuery, mutation=Mutation)
my_schema2 = graphene.Schema(query=myQuery2)
