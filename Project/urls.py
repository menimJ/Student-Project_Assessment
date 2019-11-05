from django.urls import path, include
from rest_framework import routers
from Project.api.viewsets import ProjectView

route = routers.DefaultRouter()
route.register(r'Project', ProjectView, basename="")

urlpatterns = []
urlpatterns += route.urls
