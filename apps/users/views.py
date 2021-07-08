from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from apps.users.models import User
from apps.users.serializers import CreateUserSerializer


"""手机号查询类"""


class MobileCountView(APIView):
    def get(self, request, mobile):
        print("手机号查询", mobile)
        count = User.objects.filter(mobile=mobile).count()
        return Response({"count": count, "code": "0", "errmsg": "ok"})


"""用户名查询"""


class UsernameCountView(APIView):
    def get(self, request, username):
        print("用户名查询", username)
        count = User.objects.filter(username=username).count()
        return Response({"count": count, "code": "0", "errmsg": "ok"})


class IndexView(APIView):
    pass


"""注册"""
class RegisterView(CreateAPIView):
    # 指定序列化类
    serializer_class = CreateUserSerializer


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

"""登录"""
class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            response = Response(response_data)
            print("........")
            print(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            # 账号登录时合并购物车
            # merge_cart_cookie_to_redis(request, user, response)

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)