from django.conf.urls import url
from api.views import course
from api.views import degreecourse
from api.views import shoppingcar

urlpatterns = [
    url(r'shoppingcar/$',
        shoppingcar.ShoppingCarView.as_view({'post': 'create', 'get': 'list', 'delete': 'destroy', 'put': 'update'})),
    # url(r'shoppingcar/$', shoppingcar.CoursesCarView.as_view()),
    url(r'courses/$', course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),
    url(r'courses/thematic/$', course.CourseThematicView.as_view()),
    url(r'courses/module/(?P<pk>\d+)/$', course.CourseModuleView.as_view()),
    url(r'courses/faq/(?P<pk>\d+)/$', course.CourseFAQView.as_view()),
    url(r'courses/outline/(?P<pk>\d+)/$', course.CourseOutlineView.as_view()),
    url(r'courses/chapter/(?P<pk>\d+)/$', course.CourseChapterView.as_view()),  # 获取数据失败
    # url(r'degreecourse/(?P<pk>\d+)/$', degreecourse.DegreeCourseTeacherView()),
    url(r'degreecourse/$', degreecourse.DegreeCourseView.as_view()),
    url(r'degreecourse/teachers/$', degreecourse.DegreeCourseTeacherView.as_view()),
    url(r'degreecourse/scholarship/$', degreecourse.DegreeCourseScholarshipView.as_view()),
]
