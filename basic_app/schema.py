# schema.py

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Model1, Mark


class MarkType(DjangoObjectType):
    class Meta:
        model = Mark
        # filter_fields = {
        #     'title': ['exact', 'icontains'],
        #     'author': ['exact', 'icontains'],
        #     'published_date': ['exact', 'icontains'],
        # }
        # interfaces = (graphene.relay.Node,)
        fields = ('id', 'mark_name')


class CreateMark(graphene.Mutation):
    class Arguments:
        mark_name = graphene.String(required=True)

    model1 = graphene.Field(MarkType)

    def mutate(self, info, mark_name):
        marks = Mark(mark_name=mark_name)
        marks.save()
        return CreateMark(mark_name=mark_name)


class UpdateMark(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        mark_name = graphene.String()

    mark = graphene.Field(MarkType)

    def mutate(self, info, id, mark_name=None):
        mark = Mark.objects.get(pk=id)
        if mark_name:
            mark.mark_name = mark_name
        mark.save()
        return UpdateMark(mark=mark)


class DeleteMark(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    mark = graphene.Field(MarkType)

    def mutate(self, info, id):
        mark = Mark.objects.get(pk=id)
        mark.delete()
        return DeleteMark(mark=None)


class Query(graphene.ObjectType):
    mark = graphene.relay.Node.Field(MarkType)
    # marks = DjangoFilterConnectionField(BookType)


class Mutation(graphene.ObjectType):
    create_mark = CreateMark.Field()
    update_mark = UpdateMark.Field()
    delete_mark = DeleteMark.Field()


schema = graphene.Schema(query=Query)
