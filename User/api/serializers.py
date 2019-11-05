from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from User.models import MyUser, Grade


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for creating User: Admin,Student and Examiner"""

    class Meta:
        model = MyUser
        fields = ["username", "role", "password"]
        validate_password = make_password

    def create(self, validated_data):
        """create a User and hash the password before saving"""
        user = MyUser.objects.create(
            username=validated_data['username'],
            role=validated_data['role'],
            password=make_password(validated_data['password'])
        )
        return user


class AdminGradeSerializer(serializers.ModelSerializer):
    """This serializer is for setting the Grade System"""

    class Meta:
        model = Grade
        fields = "__all__"

    def create(self, validated_data):
        value = check_grade(validated_data)
        if Grade.objects.all().count() != 0:
            raise serializers.ValidationError("Grade already created")
        if not value:
            raise serializers.ValidationError("Sum not up to 100")
        return Grade.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if not check_grade(validated_data):
            raise serializers.ValidationError("Sum not equal to 100")

        instance.abstract = validated_data.get('abstract', instance.abstract)
        instance.literature = validated_data.get('literature', instance.literature)
        instance.method = validated_data.get('method', instance.method)
        instance.analysis = validated_data.get('analysis', instance.analysis)
        instance.conclusion = validated_data.get('conclusion', instance.conclusion)
        instance.save()
        return instance


class ExaminerSerializer(serializers.Serializer):
    """Serializer for accepting grade values and validating them with the set standard"""
    abstract = serializers.FloatField()
    literature = serializers.FloatField()
    method = serializers.FloatField()
    analysis = serializers.FloatField()
    conclusion = serializers.FloatField()
    grade = Grade.objects.all()

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        result = 0
        for grade in validated_data:
            result += validated_data[grade]
        instance.grade = result
        instance.save()
        return instance

    def validate_abstract(self, value):
        if value > self.grade[0].abstract:
            raise serializers.ValidationError("Greater than the required value")
        return value

    def validate_literature(self, value):
        if value > self.grade[0].literature:
            raise serializers.ValidationError("Greater than the required value")
        return value

    def validate_method(self, value):
        if value > self.grade[0].method:
            raise serializers.ValidationError("Greater than the required value")
        return value

    def validate_analysis(self, value):
        if value > self.grade[0].analysis:
            raise serializers.ValidationError("Greater than the required value")
        return value

    def validate_conclusion(self, value):
        if value > self.grade[0].conclusion:
            raise serializers.ValidationError("Greater than the required value")
        return value


# function that checks if the sum of each grade section is equal to 100
def check_grade(value):
    result = 0
    for val in value:
        result += value[val]
    if result != 100:
        return False
    return True
