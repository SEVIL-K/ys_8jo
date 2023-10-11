from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.http import HttpResponseBadRequest

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, save= True):

            if not email:
                raise ValueError("Users must have an email address")
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            if save == True:
                user.save(using=self._db)
            return user
        
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            save=False,#밑에서 저장하니까
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField("이메일_아이디", max_length=255,unique=True)
    # 기존password는 가지고있으니 따로 안넣었습니다.
    name = models.CharField("이름", max_length=30)
    birthday = models.DateField(null=True,blank=True)
    # YYYY-MM-DD구조, 또는 드롭다운연결가능.
    profile_pic = models.ImageField(null=True,blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    # 일단 추가로 is_active 와 is_admin도 추가하겠습니다!
    is_admin = models.BooleanField(default=False)
    # is_active는 일시적으로 사용 중지되었거나 관리자에 의해 비활성화 된 경우에 사용
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin #true랑 같은거
    


#일부러 후의 복잡성떄매 상속 받지않았는데 받는게 나았을까요?
class DeleteUser(models.Model):
    email = models.EmailField("이메일_아이디", max_length=255, unique=True)
    password = models.CharField(max_length=128)#가져옴
    name = models.CharField("이름", max_length=30)
    birthday = models.DateField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    withdraw_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(null=True,blank=True)