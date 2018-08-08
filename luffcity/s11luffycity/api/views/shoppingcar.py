from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from api import models
import json


class CoursesCarView(APIView):  # 课程购物车
    """
    1, 接受用户选中的课程ID和价格策略ID
    2. 判断合法性
        - 课程是否存在？
        - 价格策略是否合法？
    """
    def create(self, request, *args, **kwargs):
        return Response(data)