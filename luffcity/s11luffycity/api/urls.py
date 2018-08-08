from django.conf.urls import url
from api import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', views.CourseViewSet)
urlpatterns += router.urls
