# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers, pagination
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # tree = serializers.SerializerMethodField('get_tree')
    # self__tree = serializers.SerializerMethodField('get_self_tree')
    # children = serializers.SerializerMethodField('get_childrens')
    # data = serializers.SerializerMethodField('get_data')


    class Meta:
        model = User
        # fields = [
        # 'id', 'name', 'user_id',  'parent_id', 'source_id', 'children', 'data',
        # ]

    # def get_childrens(self, obj):
    #     childerens = Folder_AL.objects.filter(parent__id=obj.id)
    #     return (self.get_data(child) for child in childerens)
    #
    #
    # def get_tree(self, obj):
    #     return Folder_AL.dump_bulk()
    #
    # def get_self_tree(self, obj):
    #     return Folder_AL.dump_bulk(parent=obj)
    #
    # def get_data(self, obj):
    #     data = dict((i.name, obj.__dict__[i.column]) for i in obj._meta.local_fields)
    #     return data