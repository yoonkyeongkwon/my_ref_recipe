from django.db import models
from django.forms import IntegerField
# account 
from account.models import Userinfo

# Create your models here.
class Recipe(models.Model):
    # 1. 레시피일련번호(RCP_SNO)
    rcp_sno = models.IntegerField()
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

    class Meta:
        db_table = 'recipe'
        app_label = 'ref'
        managed = False

class UserRef(models.Model):
    # 유저 닉네임
    username = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    # 보유한 재료
    ingredients = models.CharField(max_length=50)
    # 유통기한
    expiry_date = models.DateField(null=True)
    
    class Meta:
        db_table = 'user_ref'
        app_label = 'ref'
        managed = False

class UserCheck(models.Model):
    # 유저 닉네임
    username = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    # 찜한 게시판 아이디
    board_id = models.IntegerField()

    class Meta:
        db_table = 'check'
        app_label = 'ref'
        managed = False

class Board(models.Model):
    # 보드 아이디
    board_id = models.IntegerField()
    # rcp_sno
    rcp_sno = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # title
    board_title = models.CharField(max_length=50)
    # contents
    board_contents = models.TextField()

    class Meta:
        db_table = 'board'
        app_label = 'ref'
        managed = False

