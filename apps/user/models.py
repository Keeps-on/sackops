from django.db import models


# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    username = models.CharField(max_length=12, verbose_name='用户名')
    password = models.CharField(max_length=36, verbose_name='密码')

    def __str__(self):
        return "<{}>".format(self.username)

    class Meta:
        db_table = "UserProfile"


class Role(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    name = models.CharField(max_length=12, verbose_name="角色名称")

    def __str__(self):
        return "<{}>".format(self.name)

    class Meta:
        db_table = "Role"


class Permission(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    name = models.CharField(max_length=12, verbose_name="权限名称")

    def __str__(self):
        return "<{}>".format(self.name)

    class Meta:
        db_table = "Permission"
