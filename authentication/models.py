from trace import Trace

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=32)


class Group(models.Model):
    name = models.CharField(max_length=130, unique=True)


class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)


class UserGroup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "group"))


class GroupPermission(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("permission", "group"))

class UserPermission(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("user", "permission"))

class AccessToken(models.Model):
      accesstoken= models.TextField()

