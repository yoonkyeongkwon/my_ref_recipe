from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField


class Community_Board(models.Model):
    #커뮤니티 게시판의 게시글 번호
    community_board_id = models.IntegerField()

    #요리 제목
    title = models.CharField(max_length=45)

    #요리 만드는 법 내용
    contents = models.TextField()

    #게시글 조회수
    views = models.IntegerField()

    #게시글 날짜
    regdate = models.DateTimeField()

    #게시글 좋아요 수
    like = models.IntegerField()

    #게시글 작성자 이름
    write_id = models.CharField(max_length=45)

    #게시글 좋아요한 사람의 아이디
    post_like_id= models.CharField(max_length=45)

    class Meta:
        db_table = 'community_board'
        managed = False
        app_label = 'community'

