from django.shortcuts import render, HttpResponse
from api import models
from django.http import JsonResponse
# from app01 import models
import json
from rest_framework import serializers

"""
a.查看所有学位课并打印学位课名称以及授课老师

b.查看所有学位课并打印学位课名称以及学位课的奖学金

c.展示所有的专题课
models.Course.objects.filter(degree_course__isnull=True)

d.查看id = 1
的学位课对应的所有模块名称

e.获取id = 1
的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

f.获取id = 1
的专题课，并打印该课程相关的所有常见问题

g.获取id = 1
的专题课，并打印该课程相关的课程大纲

h.获取id = 1
的专题课，并打印该课程相关的所有章节

i.获取id = 1
的专题课，并打印该课程相关的所有课时
第1章·Python
介绍、基础语法、流程控制
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
第1章·Python
介绍、基础语法、流程控制
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
01 - 课程介绍（一）
i.获取id = 1
的专题课，并打印该课程相关的所有的价格策略
"""
# from django.shortcuts import render, HttpResponse
# from django.views import View
# import json
# from api import models
#
#
# class CheckView(View):
#     degree_list = models.DegreeCourse.objects.all().values('name', 'teachers__name')
#     queryset = models.DegreeCourse.objects.all()
#     for row in queryset:
#         row.name, row.teachers.all()
#     degree_list = models.DegreeCourse.objects.all()
#     for row in degree_list:
#         print(row.name)
#         scholarships = row.scholarship_set.all()
#         for item in scholarships:
#             print('--->', item.time_percent, item.value)
#     c_obj = models.Course.objects.filter(degree_course__isnull=True)


def select(request):
    # a.查看所有学位课并打印学位课名称以及授课老师
    obj1 = models.DegreeCourse.objects.all().values('name', 'teachers__name')

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    obj2 = models.DegreeCourse.objects.all().values('name', 'total_scholarship')

    # c.展示所有的专题课
    obj3 = models.Course.objects.filter(degree_course__isnull=True)

    # d.查看id = 1的学位课对应的所有模块名称
    obj4 = models.Course.objects.filter(id=1).values('name', 'degree_course')

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    obj5 = models.Course.objects.filter(degree_course__isnull=True, id=1).values('name', 'level',
                                                                                 'coursedetail__why_study',
                                                                                 'coursedetail__what_to_study_brief',
                                                                                 'coursedetail__recommend_courses')

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    obj6 = models.Course.objects.filter(id=1)
    questions = [x.asked_question.all() for x in obj6]
    print(questions)

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    obj7 = models.CourseDetail.objects.filter(id=1).values('courseoutline__title')

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    obj8 = models.Course.objects.filter(id=1).values('coursechapters__name')

    # i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
    obj9 = models.Course.objects.filter(id=1).values('coursechapters__name', 'coursechapters__coursesections__name')

    return HttpResponse('OK')
