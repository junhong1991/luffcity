from rest_framework import serializers
from api import models


class CoursesCarModelSerializer(serializers.SerializerMetaclass):  # 课程购物车
    degreecourse_price_policy = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['name', 'degreecourse_price_policy']

    def get_degreecourse_price_policy(self, row):
        scholarships = row.scholarship_set.all()
        return [{'id': item.id, 'time_percent': item.time_percent, 'value': item.value} for item in scholarships]