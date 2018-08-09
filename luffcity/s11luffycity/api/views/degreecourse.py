from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from api import models
from rest_framework.pagination import PageNumberPagination
from api.serializers.degreecourse import DegreeCourseTeachersModelSerializer, DegreeCourseScholarshipModelSerializer, \
    DegreeCourseModelSerializer
from api.utils.response import BaseResponse


class DegreeCourseTeacherView(APIView):  # 查看所有学位课对应的老师

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.DegreeCourse.objects.order_by('id')
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            # 分页之后的结果执行序列化
            ser = DegreeCourseTeachersModelSerializer(instance=course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class DegreeCourseScholarshipView(APIView):  # 学位课对应的奖学金

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.order_by('id')
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            ser = DegreeCourseScholarshipModelSerializer(instance=course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class DegreeCourseView(APIView):  # 查看所有的学位课

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            ser = DegreeCourseModelSerializer(instance=course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)
