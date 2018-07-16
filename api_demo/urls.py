from django.conf.urls import url
from api_demo.views import markAttendance, getStudents

urlpatterns = [
    url(r'^mark_att/$', markAttendance),
    url(r'^getStudents/$', getStudents),
]

