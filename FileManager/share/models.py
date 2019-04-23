from django.db import models
from datetime import datetime

class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name="访问次数", default=0)
    code = models.CharField(max_length=8, verbose_name="code")
    Datatime = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    path = models.CharField(max_length=32, verbose_name="下载路径")
    name = models.CharField(max_length=32, verbose_name="文件名", default="")
    Filesize = models.CharField(max_length=10, verbose_name="文件大小")
    PCIP = models.CharField(max_length=32, verbose_name="IP地址", default="")

    class Meta:
        verbose_name = "download"
        db_table = "download"

    def __str__(self):
        return self.name