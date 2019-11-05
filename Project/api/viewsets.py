from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProjectSerializer
from Project.models import Project


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def create(self, request):
        if request.user.st_project:
            return Response({"msg": "Already Submitted Project"})
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user)
            return Response({
                "message": "Project Submitted"
            })
        else:
            return Response({
                "message": "Fields required"
            })

    def update(self, request, pk=None):
        queryset = Project.objects.get(id=pk)
        serializer = ProjectSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Project Updated"
            })

    def list(self, request):
        queryset = Project.objects.all()
        if not queryset:
            return Response({
                "message": "No Project Submitted"
            })
        serializer = ProjectSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            queryset = Project.objects.filter(id=id)
            queryset.delete()
            return Response({
                "message": "deleted"
            })
        except Exception as error:
            return Response({
                "error": error
            })

    @action(detail=False, methods=['get'])
    def project(self, request):
        """
            To obtain the project assigned to the Examiner
        :param request:
        :return:
        """
        # Set Validation for anonymous user
        user = request.user
        queryset = user.project
        if queryset is None:
            return Response({"msg": "No project assigned"})
        user.project.objects.get()
        serializer = ProjectSerializer(instance=queryset)
        return Response(serializer.data)

    # def get_permissions(self):
    #     pass
