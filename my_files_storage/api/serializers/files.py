# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import datetime
import magic
from copy import deepcopy
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import serializers, pagination
from my_files_storage.models import File, Photo, UserFile
from my_files_storage.utils import get_exif_dict

logger = logging.getLogger(__name__)

try:
    MAX_DAYS_TO_OLD = settings.MAX_DAYS_TO_OLD
except AttributeError:
    MAX_DAYS_TO_OLD = 365



class FileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_my_file_url')
    title = serializers.SerializerMethodField('get_file_title')

    class Meta:
        model = File

    def get_file_title(self, obj):
        try:
            return obj.userfiles.first().title
        except (AttributeError, ObjectDoesNotExist):
            return

    def get_my_file_url(self, obj):
        try:
            return obj.file.url
        except AttributeError:
            return


class PhotoSerializer(FileSerializer):

    class Meta:
        model = Photo

    def validate(self, data):
        if not 'create_data' in data and not self.photo_create_data:
            raise serializers.ValidationError('cant find photo create time')
        if not 'create_data' in data:
            data['create_data'] = self.photo_create_data
        return data

    def validate_file(self, value):
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(value.read())
        if 'image' not in mime_type:
            raise serializers.ValidationError('its not image its %s'%mime_type)
        else:
            value.seek(0, 0)
        exif = get_exif_dict(value)
        if 'DateTime' not in exif:
            raise serializers.ValidationError('cannot take photo create time')
        else:
            create_data = exif['DateTime']
            foto_created_time = datetime.datetime.strptime(create_data, '%Y:%m:%d %H:%M:%S')
            self.validate_create_data(foto_created_time)
            return value

    def validate_create_data(self, value):
        naive_time = value.replace(tzinfo=None)
        time_delta = datetime.datetime.now() - naive_time
        if time_delta.days > MAX_DAYS_TO_OLD:
            raise serializers.ValidationError('photo so old')
        self.photo_create_data = naive_time #foto_created_time_to_django
        return naive_time

