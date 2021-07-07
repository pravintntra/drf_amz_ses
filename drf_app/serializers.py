from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User
from django.utils.timezone import now


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    updated_date = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = "__all__"

    def get_updated_date(self, obj):
        obj = now()
        return obj

    def validate_first_name(self, value):
        if value != value.capitalize():
            raise serializers.ValidationError("Please enter first name in capital")
        return value

    def validate(self, data):
        f_name = data.get("first_name")
        l_name = data.get("last_name")
        if f_name == l_name:
            raise serializers.ValidationError(
                "please enter diffrent first name and last name"
            )
        return data

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        super(EmployeeSerializer, self).update(instance, validated_data)

        return instance


class UserSerializer(serializers.ModelSerializer):
    user_employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "user_employee",
        ]
        extra_kwargs = {"password": {"write_only": True}}
