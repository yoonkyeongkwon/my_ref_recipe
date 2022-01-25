from django.db import models

# Create your models here.
class Userinfo(models.Model):
    
    # 유저 id
    id = models.IntegerField(db_column='id', primary_key=True)
    # 비밀번호
    password = models.CharField(db_column='password', max_length=128)
    # 이름
    name = models.CharField(db_column='username', max_length=150)
    # 이메일
    email = models.CharField(db_column='email', max_length=254)

    access_latest = models.DateTimeField(db_column='access_latest', )
    

    '''
    # 성
    last_name = models.CharField(max_length=150)
    # 관리자
    is_staff = models.IntegerField()
    # 활성화
    is_active = models.IntegerField()
    # 가입일자
    date_joined = models.DateTimeField()
    '''

    class Meta:
        db_table = 'auth_user'
        app_label = 'account'
        managed = False
