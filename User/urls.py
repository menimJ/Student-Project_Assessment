from django.urls import path, include
from rest_framework import routers
from User.api.viewsets import UserView, StudentView, ExaminerView, GradeView

router = routers.DefaultRouter()
# router.register(r'Grade', GradeView)
router.register(r'Examiner', ExaminerView, basename="exam")
# router.register(r'Student', StudentView, basename="")
# router.register(r'create', UserView, basename="user")
urlpatterns = router.urls
#     [
#     url(r'^', include(router.urls)),
#
# ]
