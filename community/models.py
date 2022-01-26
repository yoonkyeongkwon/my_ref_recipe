from importlib.resources import contents
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
    regdate = models.DateField(auto_now_add=True)

    #게시글 좋아요 수
    like = models.IntegerField(default = 0)

    #게시글 작성자 이름
    write_id = models.CharField(max_length=45)

    file =models.ImageField(null=True)

    class Meta:
        managed=False
        db_table = "community_board"
        app_label = "community_board"

# 댓글
class Comment(models.Model):
    com_id = models.IntegerField(primary_key=True)

    #댓글 작성자
    author = models.CharField(max_length=45)
    
    #댓글 내용
    contents = models.TextField()

    #작성날짜
    createdTime = models.DateTimeField(auto_now_add=True)

    id = models.ForeignKey(Board, on_delete = models.CASCADE)

    class Meta:
        managed=False
        db_table = "comment"
        app_label = "comment"