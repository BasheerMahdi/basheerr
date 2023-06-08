from django.http import HttpResponse
from rest_framework import serializers
from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from order.models import *

Coustmer = get_user_model()






from rest_framework import serializers
from django.contrib.auth import authenticate



from rest_framework import serializers
from django.contrib.auth.models import User
##1
class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # confirm_password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     if data.get('password') != data.get('confirm_password'):
    #        raise serializers.ValidationError("Passwords do not match")
    #     return data

    def create(self, validated_data):
        user = Coustmer.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            TypeUser=validated_data.get('TypeUser'),
            PhonNumber=validated_data.get('PhonNumber'),
         
        )
        return user

    class Meta:
        model = Coustmer
        fields = ('id','username', 'password', 'TypeUser', 'PhonNumber')
        extra_kwargs = {
            'id': {'read_only': True},
        }











########################



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)

class CustomUserSerializer(serializers.ModelSerializer):
    # auth_token = TokenSerializer()

    class Meta:
        model =Coustmer
        fields = ('PhonNumber', 'passwoed')






# class CustomUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = Coustmer
#         fields = ('PhonNumber', 'password')

#     def create(self, validated_data):
#         user = Coustmer.objects.create_user(
#             PhonNumber=validated_data['PhonNumber'],
#             password=validated_data['password']
#         )
#         return user

class LoginSerializer(serializers.Serializer):
    PhonNumber = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        PhonNumber = data.get('PhonNumber', None)
        password = data.get('password', None)

        if PhonNumber is None:
            raise serializers.ValidationError('An PhonNumber  is required to log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(email=PhonNumber, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid PhonNumber/password combination.')

#         if not user.is_active:
#             raise serializers.ValidationError('This user has been deactivated.')
        
#         return {'user': user}



























###########################################
class TypeCoustSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields ='__all__'


class CoustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coustmer
        fields ='__all__'
        # ("username", "PhonNumber", "TypeUser", "password")

    def create(self, validated_data, **kwargs):
        """
        Overriding the default create method of the Model serializer.
        """
        print(validated_data)
        coustmer = Coustmer(
            username=validated_data["username"],
            TypeUser=validated_data["TypeUser"],
            PhonNumber=validated_data["PhonNumber"],
        )
        password = validated_data["password"]
        coustmer.set_password(password)
        coustmer.save()
        return coustmer

# class UserLoginSerializer(serializers.Serializer):
#     """
#     Serializer class to authenticate users with email and password.
#     """
#     # username = None
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
 



# class AuthUserSerializer(serializers.ModelSerializer):
#     auth_token = serializers.SerializerMethodField()

#     class Meta:
#          model = User
#          fields = ('PhonNumber', 'password')
         
    
#     def get_auth_token(self, obj):
#         token = Token.objects.create(user=obj)
#         return token.key


# class LoginSerializer(TokenObtainPairSerializer):
#     PhonNumber = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     class Meta:
#           model = Coustmer
#         #   fields = '__all__'
#     def validate(self, attrs):
       
#         data = super(LoginSerializer, self).validate(attrs)
     
#         data.update()
#         token = Token.objects.get(user=self.user)
        
#         respons={
#             'data':data,
#             'token':token.key,
#             'msg':'Login Succsful'
#         }
       
#         return respons 

class CoustemSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoustemSections
        fields ='__all__'


class OhdatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ohdat
        fields ='__all__'

class MyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPrice
        fields ='__all__'

class ProdectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodect
        fields ='__all__'
        
# class OrdersDetiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetiles
#         fields ='__all__'

class OrdersiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ='__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'





# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coustmer
#         fields = ('username', 'PhonNumber', 'password')
        

#     def create(self, validated_data):
#         user = Coustmer.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user


##############
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email",)
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password.', code='authorization')
        else:
            raise serializers.ValidationError('Email and password are required.', code='authorization')
        attrs['user'] = user
        return attrs
