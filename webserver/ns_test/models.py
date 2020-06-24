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

    ip = models.CharField(verbose_name='IP地址', max_length=20, unique=True, editable=False)
    mac = models.CharField(verbose_name='MAC地址', max_length=30, unique=True, editable=False)
    name = models.CharField(verbose_name='名称', max_length=20, null=True, editable=False)
    status = models.CharField(verbose_name='状态', max_length=2, choices=stat, default='宕机')
    comment = models.CharField(verbose_name='备注', max_length=20, blank=True)
    # c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = "IP记录"
        verbose_name_plural = "IP列表"

    def __str__(self):
        return self.ip


class Comment(models.Model):
    ip = models.CharField(verbose_name='IP地址', max_length=20, unique=True, editable=False)
    comment = models.CharField(verbose_name='备注', max_length=20, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "备注"
        verbose_name_plural = "备注列表"

    def __str__(self):
        return self.ip