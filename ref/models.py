from email.policy import default
from django.db import models
from django.forms import IntegerField
# account 
from account.models import Userinfo

# Create your models here.

# 레시피 테이블
class Recipe(models.Model):
    # 1. 레시피일련번호(RCP_SNO)
    rcp_sno = models.IntegerField(primary_key=True)
    ## 현재 나는 에러는 mysql id 문제
    # 2. **요리명(CKG_NM)**
    ckg_nm = models.TextField()
    # 3. 조회수(INQ_CNT)
    inq_cnt = models.IntegerField(null=True)
    # 4. 추천수 RCMM_CNT
    rcmm_cnt = models.IntegerField(null=True)
    # 5. 요리방법별명(CKG_MTH_ACTO_NM)
    ckg_mth_acto_nm = models.TextField()
    # 6. 요리상황별명(CKG_STA_ACTO_NM)
    ckg_sta_acto_nm = models.TextField()
    # 7. **요리재료별명(CKG_MTRL_ACTO_NM)**
    ckg_mtrl_acto_nm = models.TextField()
    # 8. 요리종류별명(CKG_KND_ACTO_NM)
    ckg_knd_acto_nm = models.TextField()
    # 9. 요리재료내용(CKG_MTRL_CN)
    ckg_mtrl_cn = models.TextField()
    # 10. 요리시간명(CKG_TIME_NM)
    ckg_time_nm = models.TextField()
    # 11. 재료 수(MTRL_CNT)
    mtrl_cnt = models.TextField(default='')
    # 10. 재료(MTRL)
    mtrl = models.TextField(default='')
    

# 유저 냉장고 테이블
class Mine(models.Model):
    # id
    seq = models.IntegerField(primary_key=True)
    # 유저 닉네임
    # username = models.ForeignKey(Userinfo, on_delete=models.CASCADE ,db_column='username')
    username = models.CharField(max_length=100)
    # 보유한 재료
    ingredients = models.CharField(max_length=50)
    # 유통기한
    expiry_date = models.DateField(null=True)    

# 찜 테이블(체크 테이블)
class Jim(models.Model):
    # 유저 닉네임
    nickname = models.ForeignKey(Userinfo, on_delete=models.CASCADE,db_column='nickname')
    # 찜한 게시판 아이디
    board_id = models.IntegerField()

# 요리 게시판 테이블
class Board(models.Model):
    # 보드 아이디
    board_id = models.IntegerField()
    # rcp_sno
    rcp_sno = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='rcp_sno')
    # title
    board_title = models.CharField(max_length=50)
    # contents
    board_contents = models.TextField()






