from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField


class Board(models.Model):
    #커뮤니티 게시판의 게시글 번호
    id = models.IntegerField(primary_key=True)

    #요리 만드는 법 내용
    contents = models.TextField()

    #게시글 조회수
    views = models.IntegerField(default = 0)

    #게시글 날짜
    regdate = models.DateTimeField(auto_now=True)

    #게시글 좋아요 수
    like = models.IntegerField(default = 0)

    #게시글 작성자 이름
    write_id = models.CharField(max_length=45)

    #게시글 좋아요한 사람의 아이디
    post_like_id= models.CharField(max_length=45)

    file =models.ImageField(null=True)
