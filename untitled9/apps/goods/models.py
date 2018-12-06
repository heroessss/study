from django.db import models
from datetime import datetime
# Create your models here.
class Goods(models.Model):
    good_id = models.CharField( max_length=10,verbose_name=u"商品编码")
    user_id = models.CharField( max_length=10,verbose_name=u"设计师")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    image = models.ImageField(upload_to="media/image/%Y/%m", max_length=100)
    def  __str__(self):
        return self.good_id
    class Meta:
        verbose_name = u"商品编码"
        verbose_name_plural = verbose_name

class Shop(models.Model):
    good_id = models.ForeignKey(Goods,verbose_name="编码",on_delete=models.CASCADE)
    color = models.CharField(verbose_name=u"颜色", choices=(("hs",u"红色"),("ls",u"蓝色"),), max_length=30)
    size = models.CharField(verbose_name=u"袖长", choices=(("1",u"长款"),("0",u"短款"),), max_length=30)
    shangjia_time = models.DateTimeField(verbose_name=u"记录时间", default=datetime.now)
    image = models.ImageField(upload_to="media/image/%Y/%m", max_length=100)
    bianma=models.CharField(max_length=20, blank=True,null=True)
    def __str__(self):
        return  str(self.bianma)
    class Meta:
        verbose_name = u"商品信息"
        verbose_name_plural = verbose_name
        unique_together = (('good_id', 'color', 'size'),)
class Order(models.Model):
    bianma = models.ForeignKey(Shop,verbose_name=u"下单编码",on_delete=models.CASCADE)
    muchs =models.IntegerField(default=0, verbose_name=u'数量')
    pici=models.IntegerField( verbose_name=u'批次',blank=True)
    def __str__(self):
        return  str(self.bianma)
    class Meta:
        verbose_name = u"下单"
        verbose_name_plural = verbose_name

