from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin, \
    UpdateModelMixin
from User.models import MyUser, Grade
from .serializers import CreateUserSerializer, ExaminerSerializer, AdminGradeSerializer


class StudentView(viewsets.GenericViewSet):
    # @permission_classes
    @action(detail=False, methods=["get"])
    def grade(self, request, pk=None):
        """ API for Student to access his/her grade """
        user = request.user
        grade = user.grade
        if grade is None:
            return Response({"msg": "Check Later"})
        return Response({"Grade": grade})

    """
        Things to add later
        permission classes
    """


class GradeView(viewsets.ModelViewSet):
    serializer_class = AdminGradeSerializer
    queryset = Grade.objects.all()


# #     add permission classes later


class ExaminerView(viewsets.GenericViewSet):
    # @permission_classes

    @action(detail=False, methods=["put"])
    def grade_all(self, request, pk=None):
        project = request.user.project
        if project is None:
            return Response({"msg": "Project not assigned"})
        if not Grade.objects.all():
            return Response({"msg": "Grade not created"})
        serializer = ExaminerSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            count = MyUser.objects.filter(grade__isnull=True, project=project).count()
            print(count)
            if count == 0:
                # Serializer might be needed in this area
                grade = MyUser.objects.filter(project=project)
                value = Grading.calculate_project(grade)
                student = project.created_by
                student.grade = int(value)
                student.save()
                return Response({"msg": "Success"})
        return Response({"mg": serializer.errors})

    """
        Things to add later
        permission classes
    """


class UserView(CreateModelMixin, viewsets.GenericViewSet):
    """
        This view for creating Student,Examiner and Admin
    """
    serializer_class = CreateUserSerializer

    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            value = serializer.data['role']
            return Response({
                "msg": 1,
                "success": "{} is created".format(value)
            })
        return Response({"msg": serializer.errors})


class Grading(object):
    def __init__(self):
        pass

    @staticmethod  # To get the sum of each individual value
    def calculate_project(grade):
        result = 0
        for val in grade:
            result += val.grade
        return result / len(grade)

    @staticmethod
    def check_grade(value):
        result = 0
        for val in value:
            result += val
        if result != 100:
            return False
        return True
