from django.db import models

# Create your models here.
class Ips(models.Model):
    """用户表"""
    stat = (
        ('0', '宕机'),
        ('1', '正常'),
        ('2','高延迟'),
        ('3','不稳定'),
    )

    ip = models.CharField(verbose_name='IP地址', max_length=128, unique=True)
    mac = models.CharField(verbose_name='MAC地址', max_length=128, unique=True)
    name = models.CharField(verbose_name='名称', max_length=128, null=True)
    status = models.CharField(verbose_name='状态', max_length=32, choices=stat, default='宕机')
    comment = models.CharField(verbose_name='备注', max_length=128, null=True)
    # c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "IP列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip