from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from base.response import json_api_response
# import logging
# logger = logging.getLogger('views')

from django.shortcuts import get_object_or_404 as _get_object_or_404

from rest_framework import mixins, views
from rest_framework.settings import api_settings


class BaseModelNoListViewSet(viewsets.ModelViewSet):

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        data = {}
        if hasattr(self.queryset.model(), 'get_table_info'):
            data = self.queryset.model().get_table_info()

        return Response(data)


class BaseModelViewSet(viewsets.ModelViewSet):
    '''
        list排序 需要重新定义排序情况
    '''

    def list(self, request):
        try:
            ordering = request.query_params.get('ordering', '')
            ordering = ordering.replace('+', '').strip()
            if ordering:
                if self.serializer_class is None:
                    queryset = self.filter_queryset(self.get_serializer_class().Meta.model.objects.order_by(ordering))
                else:
                    queryset = self.filter_queryset(self.serializer_class.Meta.model.objects.order_by(ordering))
            else:
                queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return json_api_response(data=serializer.data)
        except Exception as e:
            return json_api_response(code=-1, message=str(e), data='error')

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        data = {}
        if hasattr(self.get_queryset().model(), 'get_table_info'):
            data = self.get_queryset().model().get_table_info()

        return json_api_response(data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_api_response(data=serializer.data)
        except Exception as e:
            return json_api_response(code=-1, message=str(e), data='error')

    def update(self, request, *args, **kwargs):

        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return json_api_response(data=serializer.data)
        except Exception as e:
            return json_api_response(code=-1, message=str(e), data='error')

    def retrieve(self, request, *args, **kwargs):
        # 封装的 get_object 拿对象
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return json_api_response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return json_api_response()
        except Exception as e:
            return json_api_response(code=-1, data='eroor', message=f'ERROR: {str(e)}')


class BaseGenericViewSet(viewsets.GenericViewSet):
    pass
