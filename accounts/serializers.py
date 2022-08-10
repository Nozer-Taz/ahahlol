from rest_framework import serializers

from accounts.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'phone_number')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Password do not match!')
        return validated_data
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number')
        
