
from API.models import EmployeeUser
from rest_framework import serializers
from API.manager import EmployeeManager

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email','name','phone_no','designtions',]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email','name','phone_no','designtions',]
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email']
    def delete(self, instance):
        instance.delete()
        return
        
class EmployeeLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)

    class Meta:
        model = EmployeeUser
        fields = ['email','password']

class EmployeeProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = EmployeeUser
        fields = ['email','name','phone_no','designtions']


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email','phone_no','name','password','is_admin']

class CheckManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email','is_manager']

class ManagerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email','name','phone_no','password','is_manager']

class UserChangePassword(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30)
    class Meta:
        model = EmployeeUser
        fields = ['email','password']

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance

class UserForgetPassword(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ['email']