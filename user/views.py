from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, logout, authenticate

from user.serializers import UserSerializer, UserSignupSerializer


class UserView(APIView):
    permission_classes = [permissions.AllowAny]  # 모두 사용가능
    # parmission_classes = [permissions.IsAuthenticated] #로그인 된 사용자만
    # parmission_classes = [permissions.IsAdminUser] # 어드민 유저만

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.http_200_ok)

    def post(self, request):
        # 회원가입
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():  # 유효값인지 확인
            serializer.save()
            return Response({'message': '가입완료!!'})
        else:
            # 실패원인을 프린트 해준다
            print(serializer.errors)
            return Response({'message': '가입실패!!'})

    def put(self, request):
        # 회원 정보 수정
        return Response({'message': 'put method'})

    def delete(self, request):
        # 회원탈퇴
        return Response({'message': 'delete method'})


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]  # 모두 사용가능
    # 조회

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.http_200_ok)

    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        # 변수 user에는 인증에 성공하면 user가 담기고, 인증 실패하면 None이 담긴다.
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'message': '아이디 또는 비밀번호가 올바르지 않습니다.'})
        login(request, user)
        return Response({'message': '로그인 성공!!'})
    # 로그아웃

    def delete(self, request):
        logout(request)
        return Response({'message': '로그아웃 성공!!'})
