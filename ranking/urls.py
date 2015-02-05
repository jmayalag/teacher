from django.conf.urls import patterns, url, include
from ranking.views import TeacherList, TeacherDetail, index, TeacherViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)


urlpatterns = patterns('',
                   url(r'^$', index, name='index'),
                   url(r'^teacher/$', TeacherList.as_view(), name='teacher_list'),
                   url(r'^teacher/(?P<pk>[\d+])/$', TeacherDetail.as_view(), name='teacher_detail'),
                   url(r'^api/', include(router.urls)),
                   )