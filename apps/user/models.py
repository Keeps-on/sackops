from django.db import models


# Create your models here.
###################################
#          用户表                  #
###################################

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    username = models.CharField(max_length=12, verbose_name='用户名')
    password = models.CharField(max_length=36, verbose_name='密码')

    def __str__(self):
        return "<{}>".format(self.username)

    class Meta:
        db_table = "UserProfile"


###################################
#          角色表                  #
###################################
class Role(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    name = models.CharField(max_length=12, verbose_name="角色名称")

    def __str__(self):
        return "<{}>".format(self.name)

    class Meta:
        db_table = "Role"


###################################
#          权限表                  #
###################################
class Permission(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    name = models.CharField(max_length=12, verbose_name="权限名称")

    def __str__(self):
        return "<{}>".format(self.name)

    class Meta:
        db_table = "Permission"


###################################
#         用户角色关联表            #
###################################
class UserRole(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键自增')
    uid = models.IntegerField(verbose_name='用户id')
    rid = models.IntegerField(verbose_name='角色id')

    def __str__(self):
        return "<{}>".format(self.uid)

    class Meta:
        db_table = "User_Role"
