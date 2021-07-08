from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from utils.myMOdels import BaseModel


class User(AbstractUser):
    """
    用户表
    """
    nickname = models.CharField(max_length=15, verbose_name='昵称', default='')
    gender = models.CharField(max_length=6, verbose_name='性别', choices=(('male', '男'),
                                                                        ('female', '女'),
                                                                        ('secret', '保密'),
                                                                        ), default='secret')
    # city_addr = models.CharField(max_length=6, verbose_name='居住地代码', default='410302')
    default_address = models.ForeignKey('Address', related_name='users', null=True, blank=True,
                                        on_delete=models.SET_NULL, verbose_name='默认地址')
    birthday = models.DateField(default='1970-01-01', verbose_name='生日')
    signature = models.CharField(max_length=300, verbose_name='个人签名', default='')
    # portrait = models.ImageField(upload_to=user_directory_path, default='image/default.jpg', max_length=100)
    default_image = models.ImageField(max_length=200, default='', null=True, blank=True, verbose_name='头像')
    integral = models.IntegerField(default=0, verbose_name='积分')
    check_time = models.DateField(default='1970-01-01', verbose_name='签到时间')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = 'tb_users_'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username







"""地址模型类"""
class Address(BaseModel):
    """用户地址"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    province = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='province_addresses', verbose_name='省')
    city = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='district_addresses', verbose_name='区')
    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    tel = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']


class Banner(BaseModel):
    """
    首页轮播图
    """
    title = models.CharField(max_length=100, verbose_name='标题')
    default_image_url = models.ImageField(max_length=200, default='', null=True, blank=True, verbose_name='轮播图')
    url = models.CharField(max_length=200, verbose_name='访问地址')
    status = models.BooleanField(default=True, verbose_name='是否展示')


    class Meta:
        db_table = 'tb_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
