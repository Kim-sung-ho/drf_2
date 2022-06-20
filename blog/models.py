from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField("카테고리명", max_length=50, default="")
    description = models.TextField("설명")

    def __str__(self):
        return self.category_name


class Article(models.Model):
    user = models.ForeignKey(
        'user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")
    # 노출 시작 일자
    # 노출 종료 일자

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."


class Comment(models.Model):
    article = models.ForeignKey(
        Article, verbose_name="글", on_delete=models.CASCADE)  # 아티클이 사라질때 사라질때 같이사라짐
    user = models.ForeignKey(
        'user.User', verbose_name="작성자", on_delete=models.CASCADE)  # 유저가 사라질때 같이사라짐
    contents = models.TextField("내용", default=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 댓글입니다."
