from django.db import models

# Create your models here.
class Userinfo(models.Model):
    
    # 유저 id
    id = models.IntegerField(primary_key=True)
    # 유저 닉네임
    username = models.CharField(max_length=150)
    # 비밀번호
    password = models.CharField(max_length=128)
    # 마지막 로그인
    last_login = models.DateTimeField()
    # 유저 권한
    is_superuser = models.IntegerField()
    # 이름
    first_name = models.CharField(max_length=150)
    # 성
    last_name = models.CharField(max_length=150)
    # 이메일
    email = models.CharField(max_length=254)
    # 관리자
    is_staff = models.IntegerField()
    # 활성화
    is_active = models.IntegerField()
    # 가입일자
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'
        app_label = 'account'
        managed = False