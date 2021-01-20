from base.views import BaseModelViewSet
from ..models import Department
from ..serializers import DepartmentGroupSerializer


class DepartmentViewSet(BaseModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentGroupSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('title', 'count')
