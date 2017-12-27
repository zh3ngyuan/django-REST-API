from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^$', views.ListCreateCourse.as_view(), name='course_list')
]
