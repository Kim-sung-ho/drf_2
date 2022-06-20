from importlib.resources import contents
from unicodedata import category
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from ai.permissions import RegisteredMoreThanThreeDaysUser
from blog.models import Article as ArticleModel


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [RegisteredMoreThanThreeDaysUser]

    def get(self, request):
        user = request.user
        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles]  # list 축약 문법
        titles = []
        for article in articles:
            titles.append(article.title)
        return Response({"article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get("title", '')
        contents = request.data.get("contents", '')
        categorys = request.data.get("category", [])

        if len(title) <= 5:
            return Response({"message": "제목은 5자 이상이어야 합니다."}, status=status.http_400_bad_request)
        if len(contents) <= 20:
            return Response({"message": "내용은 20자 이상이어야 합니다."}, status=status.http_400_bad_request)
        if not categorys:
            return Response({"message": "카테고리가 지정 되지 않았습니다."}, status=status.http_400_bad_request)
        article = ArticleModel(user=user, title=title, contents=contents)
        article.save()
        article.category.add(*categorys)
        return Response({"message": "게시글이 작성되었습니다."}, status=status.http_201_created)
